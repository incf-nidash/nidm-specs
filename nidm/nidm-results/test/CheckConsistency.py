#!/usr/bin/env python
'''Check that a given provn file is consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

from rdflib import Namespace, RDF

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
            if o == OWL['ObjectProperty']:
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
