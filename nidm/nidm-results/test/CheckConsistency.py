#!/usr/bin/env python
'''Check that a given provn file is consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

from rdflib import RDF, term
# from rdflib.graph import Graph
import sys, os

RELPATH = os.path.dirname(os.path.abspath(__file__))

# Append parent script directory to path
sys.path.append(os.path.join(RELPATH, os.pardir, os.pardir, os.pardir, "scripts"))
from Constants import *

# ignored_attributes = set([   
#                         RDFS['label'], 
#                         RDF['type'],
#                         PROV['value'], PROV['atTime'], PROV['used'], PROV['wasAssociatedWith'],
#                         PROV['qualifiedGeneration'], PROV['wasGeneratedBy'], PROV['atLocation'], 
#                         PROV['wasDerivedFrom'], 
#                         CRYPTO['sha512']
#                         ])  

# def get_sub_class_names(my_graph):
#     sub_types = set()

#     prov_types = set([PROV['Entity'], PROV['Activity'], PROV['Agent']])
#     for prov_type in prov_types:
#         for instance_id in my_graph.subjects(RDF.type, prov_type):
#             for class_name in my_graph.objects(instance_id, RDF.type):
#                if not class_name == prov_type:
#                     sub_types.add(class_name)

#     return sub_types

# def get_class_names_in_owl(my_owl_graph):
#     # Add PROV sub-types
#     sub_types = set([PROV['Bundle'], PROV['Location'], PROV['Collection']]);

#     for class_name in my_owl_graph.subjects(RDF['type'], OWL['Class']):
#         sub_types.add(class_name)

#     return sub_types

def get_property_names_in_owl(my_owl_graph):
    properties = set();
    for class_name in my_owl_graph.subjects(RDF['type'], OWL['DatatypeProperty']):
        properties.add(class_name)
    for class_name in my_owl_graph.subjects(RDF['type'], OWL['ObjectProperty']):
        properties.add(class_name)
    return properties

# def get_attributes_from_owl(my_owl_graph):
#     attributes = dict()
#     # For each ObjectProperty found out corresponding range
#     ranges = dict()

#     restrictions = dict()

#     # Check owl restrictions on classes
#     for class_name in my_owl_graph.subjects(RDF['type'], OWL['Class']):
#         for class_restr in my_owl_graph.objects(class_name, RDFS['subClassOf']):
#             if isinstance(class_restr, term.BNode):
#                 for prop in my_owl_graph.objects(class_restr,OWL['onProperty']):
#                     attributes.setdefault(class_name, set([prop])).add(prop)
#                     for child_class in my_owl_graph.subjects(RDFS['subClassOf'], class_name): 
#                         attributes.setdefault(child_class, set([prop])).add(prop)

#     # Attributes that can be found in all classes
#     for prop,p,o in my_owl_graph.triples((None, RDF['type'], None)):
#         if o == OWL['DatatypeProperty'] or o == OWL['ObjectProperty']:

#             # Check property domain
#             for class_name in my_owl_graph.objects(prop, RDFS['domain']):
#                 # Add attribute to current class
#                 if class_name in attributes:
#                     attributes[class_name].add(prop)
#                 else:
#                     attributes[class_name] = set([prop])
                
#                 # Add attribute to children of current class
#                 for child_class in my_owl_graph.subjects(RDFS['subClassOf'], class_name):
#                     # Add attribute to current class
#                     if child_class in attributes:
#                         attributes[child_class].add(prop)
#                     else:
#                         attributes[child_class] = set([prop])
#                     class_name = child_class

#             for range_name in my_owl_graph.objects(prop, RDFS['range']):
#                 # More complex type including restrictions
#                 if isinstance(range_name, term.BNode):
#                     for restriction_node in my_owl_graph.objects(range_name, OWL['withRestrictions']):
#                         for first_restriction in my_owl_graph.objects(restriction_node, RDF['first']):
#                             xsd_restrictions = set(['minInclusive', 'minExclusive', 'maxInclusive', 'maxExclusive'])
#                             for xsd_restriction in xsd_restrictions:
#                                 for min_incl in my_owl_graph.objects(first_restriction, XSD[xsd_restriction]):
#                                     if (prop in restrictions):
#                                         if (xsd_restriction in restrictions[prop]):
#                                             restrictions[prop] = max(restrictions[prop][xsd_restriction], min_incl)
#                                         else:
#                                             restrictions[prop] = { xsd_restriction: min_incl}
#                                     else:
#                                         restrictions[prop] = { xsd_restriction: min_incl}

#                     for sub_range_name in my_owl_graph.objects(range_name, OWL['onDatatype']):
#                         range_name = sub_range_name

#                 if prop in ranges:
#                     ranges[prop].add(range_name)
#                 else:
#                     ranges[prop] = set([range_name])
#                 # FIXME: more elegant?
#                 # Add child_class to range (for ObjectProperty)
#                 for child_class in my_owl_graph.subjects(RDFS['subClassOf'], range_name):
#                     # Add range to current class
#                     if prop in ranges:
#                         ranges[prop].add(child_class)
#                     else:
#                         ranges[prop] = set([child_class])
#                     range_name = child_class
#                     for child_class in my_owl_graph.subjects(RDFS['subClassOf'], range_name):
#                         # Add attribute to current class
#                         if prop in ranges:
#                             ranges[prop].add(child_class)
#                         else:
#                             ranges[prop] = set([child_class])
#                         range_name = child_class
#                         for child_class in my_owl_graph.subjects(RDFS['subClassOf'], range_name):
#                             # Add attribute to current class
#                             if prop in ranges:
#                                 ranges[prop].add(child_class)
#                             else:
#                                 ranges[prop] = set([child_class])
#                             range_name = child_class
#                             for child_class in my_owl_graph.subjects(RDFS['subClassOf'], range_name):
#                                 # Add attribute to current class
#                                 if prop in ranges:
#                                     ranges[prop].add(child_class)
#                                 else:
#                                     ranges[prop] = set([child_class])
#                                 range_name = child_class
            
#     return list((attributes, ranges, restrictions))

# def get_owl_graph(owl_file, import_files=None):
#     # Read owl (turtle) file
#     owl_graph = Graph()
#     # This is a workaround to avoid issue with "#" in base prefix as 
#     # described in https://github.com/RDFLib/rdflib/issues/379,
#     # When the fix is introduced in rdflib these 2 lines will be replaced by:
#     # self.owl.parse(owl_file, format='turtle')
#     owl_txt = open(owl_file, 'r').read().replace("http://www.w3.org/2002/07/owl#", 
#                     "http://www.w3.org/2002/07/owl")
#     owl_graph.parse(data=owl_txt, format='turtle')

#     if import_files is not None:
#         for import_file in import_files:
#             # Read owl (turtle) file
#             import_graph = Graph()
#             import_txt = open(import_file, 'r').read()

#             # This is a workaround to avoid issue with "#" in base prefix as 
#             # described in https://github.com/RDFLib/rdflib/issues/379,
#             # When the fix is introduced in rdflib these 2 lines will be replaced by:
#             # self.owl.parse(owl_file, format='turtle')
#             import_txt = import_txt.replace("http://www.w3.org/2002/07/owl#", 
#                             "http://www.w3.org/2002/07/owl")
#             import_graph.parse(data=import_txt, format='turtle')

#             owl_graph = owl_graph + import_graph

#     return owl_graph


# def check_class_names(example_graph, example_name, class_names=None, 
#     owl_file=None, owl_imports=None):
#     my_exception = dict()
#     if not class_names:
#         if owl_file is None:
#             raise Exception("One of class_names or owl_file must be not None.")
#         else:
#             owl_graph = get_owl_graph(owl_file)
#             class_names = get_class_names_in_owl(owl_graph)

#     sub_types = get_sub_class_names(example_graph)

#     for not_recognised_sub_type in (sub_types - class_names):

#         if not not_recognised_sub_type.startswith(str(PROV)):
#             # key = example_graph.qname(not_recognised_sub_type)
#             key = "\n Unrecognised sub-type: "+example_graph.qname(not_recognised_sub_type)
#             if key in my_exception:
#                 my_exception[key].add(example_name)
#             else:
#                 my_exception[key] = set([example_name])

#     return my_exception

# def check_attributes(example_graph, example_name, owl_attributes=None, owl_ranges=None, 
#     owl_restrictions=None, owl_graph=None, owl_file=None, owl_imports=None):
#     my_exception = dict()
#     my_range_exception = dict()
#     my_restriction_exception = dict()

#     if not owl_attributes or not owl_ranges:
#         if owl_file is None:
#             raise Exception("One of class_names or owl_file must be not None.")
#         else:
#             owl_graph = get_owl_graph(owl_file, owl_imports)

#             attributes_ranges = get_attributes_from_owl(owl_graph)
#             owl_attributes = attributes_ranges[0]
#             owl_ranges = attributes_ranges[1]   
#             owl_restrictions = attributes_ranges[2]

#     # Find all attributes
#     for s,p,o in example_graph.triples((None, None, None)):
#         # To be a DataTypeProperty then o must be a literal
#         # if isinstance(o, rdflib.term.Literal):
#         if p not in ignored_attributes:
#             # *** Check domain
#             # Get all defined types of current object
#             found_attributes = False
#             class_names = ""
#             for class_name in sorted(example_graph.objects(s, RDF['type'])):
#                 attributes = owl_attributes.get(class_name)

#                 # If the current class was defined in the owl file check if current
#                 # attribute was also defined.
#                 if attributes:
#                     if p in attributes:
#                         found_attributes = True

#                 class_names += ", "+example_graph.qname(class_name)

#             # if not found_attributes:
#                 # if attributes:
#                     # if not (p in attributes):
#             if not found_attributes:
#                 key = "\n Unrecognised attribute: "+example_graph.qname(p)+\
#                             " in "+class_names[2:]
#                 if not key in my_exception:
#                     my_exception[key] = set([example_name])
#                 else:
#                     my_exception[key].add(example_name)


#             # *** Check range for ObjectProperties and DataProperties
#             if isinstance(o, term.URIRef):
#                 # An ObjectProperty can point to an instance, then we look for its type:
#                 found_range = set(example_graph.objects(o, RDF['type']))

#                 # An ObjectProperty can point to a term
#                 if not found_range:
#                     found_range = set([o])

#                     # If the term is an individual, look for its type
#                     if OWL['NamedIndividual'] in \
#                         set(owl_graph.objects(o, RDF['type'])):
#                         found_range = set(owl_graph.objects(o, RDF['type']))

#             elif isinstance(o, term.Literal):
#                 found_range = set([o.datatype])

#             correct_range = False
#             if p in owl_ranges:
#                 # If none of the class found for current ObjectProperty value is part of the range
#                 # throw an error

#                 # If the type of current value is within the authorised ranges
#                 if found_range.intersection(owl_ranges[p]):
#                     correct_range = True
#                 else:
#                     if p in owl_ranges:
#                         # A bit more complicated to deal with "positiveInteger"
#                         for owl_range in owl_ranges[p]:
#                             # FIXME: we should be able to do better than that to check that XSD['positiveInteger'] is 
#                             # in owl_ranges[p]
#                             if (XSD['positiveInteger'] == owl_range) and\
#                                  (next(iter(found_range)) == XSD['int']) and\
#                                   (o.value >= 0):
#                                     correct_range = True
#                 if not correct_range:
#                     found_range_line = ""
#                     # FIXME: This should be better handled to be able to do "if found_range"
#                     if not None in found_range:
#                         found_range_line = ', '.join(map(example_graph.qname, sorted(found_range)))
#                     owl_range_line = ""
#                     if p in owl_ranges:
#                         owl_range_line = ', '.join(map(example_graph.qname, sorted(owl_ranges[p])))

#                     key = "\n Unrecognised range: "+\
#                         found_range_line+\
#                         ' for '+example_graph.qname(p)+' should be '+\
#                         owl_range_line
#             else:
#                 # No range found for current attribute
#                 correct_range = False
#                 key = "\n No range defined for: "+\
#                         example_graph.qname(p)

#             if not correct_range:
#                 if not key in my_range_exception:
#                     my_range_exception[key] = set([example_name])
#                 else:
#                     my_range_exception[key].add(example_name)

#             if p in owl_restrictions:
#                 restrictions_ok = True
#                 if 'minInclusive' in owl_restrictions[p]:
#                     if o.value < owl_restrictions[p]['minInclusive'].value:
#                         restrictions_ok = False
#                 if 'minExclusive' in owl_restrictions[p]:
#                     if o.value <= owl_restrictions[p]['minExclusive'].value:
#                         restrictions_ok = False
#                 if 'maxInclusive' in owl_restrictions[p]:
#                     if o.value > owl_restrictions[p]['maxInclusive'].value:
#                         restrictions_ok = False
#                 if 'maxExclusive' in owl_restrictions[p]:
#                     if o.value >= owl_restrictions[p]['maxExclusive'].value:
#                         restrictions_ok = False
#                 if not restrictions_ok:
#                     key = "\n Contraints: value "+str(o.value)+\
#                         ' for '+example_graph.qname(p)+' does not observe contraints '+\
#                         ', '.join(sorted(owl_restrictions[p]))
#                     if not key in my_restriction_exception:
#                         my_restriction_exception[key] = set([example_name])
#                     else:
#                         my_restriction_exception[key].add(example_name)

#     return list((my_exception, my_range_exception, my_restriction_exception))
