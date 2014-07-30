#!/usr/bin/env python
'''Check that a given provn file is consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

from rdflib import Namespace, RDF, term
from rdflib.graph import Graph

PROV = Namespace('http://www.w3.org/ns/prov#')
NIDM = Namespace('http://www.incf.org/ns/nidash/nidm#')
SPM = Namespace('http://www.incf.org/ns/nidash/spm#')
FSL = Namespace('http://www.incf.org/ns/nidash/fsl#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
CRYPTO = Namespace('http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#')
# This is a workaround to avoid issue with "#" in base prefix as 
# described in https://github.com/RDFLib/rdflib/issues/379,
# When the fix is introduced in rdflib this line will be replaced by:
# OWL = Namespace('http://www.w3.org/2002/07/owl#')
OWL = Namespace('http://www.w3.org/2002/07/owl')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')

common_attributes = set([   
                        RDFS['label'], 
                        RDF['type'],
                        PROV['value'], PROV['atTime'], PROV['used'], PROV['wasAssociatedWith'],
                        PROV['qualifiedGeneration'], PROV['wasGeneratedBy'], PROV['atLocation'], 
                        PROV['wasDerivedFrom'], 
                        CRYPTO['sha512']])  

def get_sub_class_names(my_graph):
    sub_types = set()

    prov_types = set([PROV['Entity'], PROV['Activity'], PROV['Agent']])
    for prov_type in prov_types:
        for instance_id in my_graph.subjects(RDF.type, prov_type):
            for class_name in my_graph.objects(instance_id, RDF.type):
               if not class_name == prov_type:
                    sub_types.add(class_name)

    return sub_types

def get_class_names_in_owl(my_owl_graph):
    # Add PROV sub-types
    sub_types = set([PROV['Bundle'], PROV['Location'], PROV['Collection']]);

    OWL = Namespace('http://www.w3.org/2002/07/owl')    

    for class_name in my_owl_graph.subjects(RDF['type'], OWL['Class']):
        sub_types.add(class_name)

    return sub_types

def get_attributes_from_owl(my_owl_graph):
    attributes = dict()
    # For each ObjectProperty found out corresponding range
    ranges = dict()

    # Attributes that can be found in all classes
    for data_property,p,o in my_owl_graph.triples((None, RDF['type'], None)):
        if o == OWL['DatatypeProperty'] or o == OWL['ObjectProperty']:
            for class_name in my_owl_graph.objects(data_property, RDFS['domain']):
                # Add attribute to current class
                if class_name in attributes:
                    attributes[class_name].add(data_property)
                else:
                    attributes[class_name] = set([data_property])
                # Add attribute to children of current class
                for child_class in my_owl_graph.subjects(RDFS['subClassOf'], class_name):
                    # Add attribute to current class
                    if child_class in attributes:
                        attributes[child_class].add(data_property)
                    else:
                        attributes[child_class] = set([data_property])
            # Find range
            for range_name in my_owl_graph.objects(data_property, RDFS['range']):
                if data_property in ranges:
                    ranges[data_property].add(range_name)
                else:
                    ranges[data_property] = set([range_name])
                # Add child_class to range
                for child_class in my_owl_graph.subjects(RDFS['subClassOf'], range_name):
                    # Add attribute to current class
                    if data_property in ranges:
                        ranges[data_property].add(child_class)
                    else:
                        ranges[data_property] = set([child_class])

    return list((attributes, ranges))

def get_owl_graph(owl_file):
    # Read owl (turtle) file
    owl_graph = Graph()
    # This is a workaround to avoid issue with "#" in base prefix as 
    # described in https://github.com/RDFLib/rdflib/issues/379,
    # When the fix is introduced in rdflib these 2 lines will be replaced by:
    # self.owl.parse(owl_file, format='turtle')
    owl_txt = open(owl_file, 'r').read().replace("http://www.w3.org/2002/07/owl#", 
                    "http://www.w3.org/2002/07/owl")
    owl_graph.parse(data=owl_txt, format='turtle')

    return owl_graph


def check_class_names(example_graph, example_name, class_names=None, owl_file=None):
    my_exception = dict()
    if not class_names:
        if owl_file is None:
            raise Exception("One of class_names or owl_file must be not None.")
        else:
            owl_graph = get_owl_graph(owl_file)
            class_names = get_class_names_in_owl(owl_graph)

    sub_types = get_sub_class_names(example_graph)

    for not_recognised_sub_type in (sub_types - class_names):
        # key = example_graph.qname(not_recognised_sub_type)
        key = "\n Unrecognised sub-type: "+example_graph.qname(not_recognised_sub_type)
        if key in my_exception:
            my_exception[key].add(example_name)
        else:
            my_exception[key] = set([example_name])

    return my_exception

def check_attributes(example_graph, example_name, owl_attributes=None, owl_ranges=None, owl_file=None):
    my_exception = dict()
    my_range_exception = dict()
    if not owl_attributes or not owl_ranges:
        if owl_file is None:
            raise Exception("One of class_names or owl_file must be not None.")
        else:
            owl_graph = get_owl_graph(owl_file)

            attributes_ranges = get_attributes_from_owl(owl_graph)
            owl_attributes = attributes_ranges[0]
            owl_ranges = attributes_ranges[1]   

    # Find all attributes
    for s,p,o in example_graph.triples((None, None, None)):
        # To be a DataTypeProperty then o must be a literal
        # if isinstance(o, rdflib.term.Literal):
        if p not in common_attributes:
            # *** Check domain
            # Get all defined types of current object
            found_attributes = False
            class_names = ""
            for class_name in sorted(example_graph.objects(s, RDF['type'])):
                attributes = owl_attributes.get(class_name)

                # If the current class was defined in the owl file check if current
                # attribute was also defined.
                if attributes:
                    if p in attributes:
                        found_attributes = True

                class_names += ", "+example_graph.qname(class_name)

            # if not found_attributes:
                # if attributes:
                    # if not (p in attributes):
            if not found_attributes:
                key = "\n Unrecognised attribute: "+example_graph.qname(p)+\
                            " in "+class_names[2:]
                if not key in my_exception:
                    my_exception[key] = set([example_name])
                else:
                    my_exception[key].add(example_name)

            # *** Check range for ObjectProperties and DataProperties
            if isinstance(o, term.URIRef):
                # An ObjectProperty can point to an instance, then we look for its type:
                found_range = set(example_graph.objects(o, RDF['type']))
                # An ObjectProperty can point to a term
                if not found_range:
                    found_range = set([o])
            elif isinstance(o, term.Literal):
                found_range = set([o.datatype])
            # print example_graph.qname(p)
            # print owl_ranges[term.URIRef(u'http://www.incf.org/ns/nidash/nidm#pValueFWER')]

            # print XSD['positiveInteger']
            # print type(XSD['positiveInteger'])
            correct_range = False
            if p in owl_ranges:
                # If none of the class found for current ObjectProperty value is part of the range
                # throw an error
                if found_range.intersection(owl_ranges[p]):
                    correct_range = True
                # FIXME: we should be able to do better than that to check that XSD['positiveInteger'] is 
                # in owl_ranges[p]
                elif (XSD['positiveInteger'] == next(iter(owl_ranges[p]))) &\
                     (next(iter(found_range)) == XSD['int']) & (o.value >= 0):
                        correct_range = True
                else:
                    key = "\n Unrecognised range: "+\
                        ', '.join(map(example_graph.qname, sorted(found_range)))+\
                        ' for '+example_graph.qname(p)+' should be '+\
                        ', '.join(map(example_graph.qname, sorted(owl_ranges[p])))
            else:
                # if example_graph.qname(p)=="nidm:effectDegreesOfFreedom":
                #     print example_name
                key = "\n Missing range: "+' for '+example_graph.qname(p)
                
            if not correct_range:
                # print key
                # print my_range_exception
                if not key in my_range_exception:
                    my_range_exception[key] = set([example_name])
                else:
                    my_range_exception[key].add(example_name)
                # print my_range_exception[key]


    return list((my_exception, my_range_exception))

def merge_exception_dict(excep_dict, other_except_dict):
    merged_dict = dict(excep_dict.items() + other_except_dict.items())
    # When key is in both dictionaries, we need to merge the set manually
    for key in list(set(excep_dict.keys()) & set(other_except_dict.keys())):
        merged_dict[key] = excep_dict[key].union(other_except_dict[key])

    return merged_dict
