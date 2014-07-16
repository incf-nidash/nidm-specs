#!/usr/bin/env python
'''Test that NIDM-Results examples are consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''
import unittest
import os
from subprocess import call
import re
import rdflib
from rdflib import Namespace, RDF
from rdflib.graph import Graph
import urllib2, urllib
import logging
logging.basicConfig()

PROV = Namespace('http://www.w3.org/ns/prov#')
NIDM = Namespace('http://www.incf.org/ns/nidash/nidm#')
SPM = Namespace('http://www.incf.org/ns/nidash/spm#')
FSL = Namespace('http://www.incf.org/ns/nidash/fsl#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
CRYPTO = Namespace('http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')

def get_sub_class_names(my_graph):
    sub_types = set()

    prov_types = set([PROV['Entity'], PROV['Activity'], PROV['Agent']])
    for prov_type in prov_types:
        for instance_id in my_graph.subjects(RDF.type, prov_type):
            for class_name in my_graph.objects(instance_id, RDF.type):
               if not class_name == prov_type:
                    sub_types.add(class_name)

    return sub_types


class TestExamples(unittest.TestCase):

    def setUp(self):
        # Retreive owl file for NIDM-Results
        owl_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
            'nidm-results.owl')

        # Read owl (turtle) file
        self.owl = Graph()
        # This is a workaround to avoid issue with "#" in base prefix as 
        # described in https://github.com/RDFLib/rdflib/issues/379,
        # When the fix is introduced in rdflib these 3 lines will be replaced by:
        # self.owl.parse(owl_file, format='turtle')
        owl_txt = open(owl_file, 'r').read().replace("http://www.w3.org/2002/07/owl#", 
                        "http://www.w3.org/2002/07/owl")
        self.owl.parse(data=owl_txt, format='turtle')
        OWL = Namespace('http://www.w3.org/2002/07/owl')

        # Retreive all entity/activity/agent sub-classes
        self.sub_types = set(); #{'entity': set(), 'activity': set(), 'agent' : set()}
        # For each class find out attribute list as defined by domain in attributes
        self.attributes = dict()

        # prov_types = set([PROV['Entity'], PROV['Activity'], PROV['Agent']])
        # for prov_type in prov_types:
        for class_name in self.owl.subjects(RDF['type'], OWL['Class']):
            self.sub_types.add(class_name)
                # self.attributes[class_name] = common_attributes

        # Add PROV sub-types
        self.sub_types.add(PROV['Bundle'])
        self.sub_types.add(PROV['Location'])
        self.sub_types.add(PROV['Collection'])      

        # Attributes that can be found in all classes
        self.common_attributes = set([   
                                    RDFS['label'], 
                                    RDF['type'],
                                    PROV['value'], PROV['atTime'], PROV['used'], PROV['wasAssociatedWith'],
                                    PROV['qualifiedGeneration'], PROV['wasGeneratedBy'], PROV['atLocation'], 
                                    PROV['wasDerivedFrom'], 
                                    CRYPTO['sha512']])  

        for data_property,p,o in self.owl.triples((None, RDF['type'], None)):
            if o == OWL['DatatypeProperty'] or o == OWL['ObjectProperty']:
                for class_name in self.owl.objects(data_property, RDFS['domain']):
                    # Add attribute to current class
                    if class_name in self.attributes:
                        self.attributes[class_name].add(data_property)
                    else:
                        self.attributes[class_name] = set([data_property])
                    # Add attribute to children of current class
                    for child_class in self.owl.subjects(RDFS['subClassOf'], class_name):
                        # Add attribute to current class
                        if child_class in self.attributes:
                            self.attributes[child_class].add(data_property)
                        else:
                            self.attributes[child_class] = set([data_property])

        example_filenames = set([   os.path.join('spm', 'spm_results.provn') , 
                                        os.path.join('spm', 'example001', 'example001_spm_results.provn'),
                                        os.path.join('spm', 'example002', 'spm_results_2contrasts.provn'),
                                        os.path.join('spm', 'example003', 'spm_inference_activities.provn'),
                                        os.path.join('spm', 'example003', 'spm_results_conjunction.provn'),
                                        os.path.join('fsl', 'fsl_results.provn'),
                                        os.path.join('fsl', 'example001', 'fsl_nidm.provn')])

        self.examples = dict()
        for example_file in example_filenames:

            # If True turtle file will be downloaded from the prov store using the address specified in the README. 
            # If False the turtle version will be retreived on the fly using the prov translator. By default set to True
            # to check as README should be up to date but setting to False can be useful for local testing.
            ttl_from_readme = True

            if ttl_from_readme:
                # Get URL of turtle from README file
                readme_file = os.path.join(os.path.dirname(os.path.dirname(
                                os.path.abspath(__file__))), os.path.dirname(example_file), 'README')
                readme_file = open(readme_file, 'r')
                readme_txt = readme_file.read()
                turtle_search = re.compile(r'.*turtle: (?P<ttl_file>.*\.ttl).*')
                extracted_data = turtle_search.search(readme_txt) 
                ttl_file_url = extracted_data.group('ttl_file');
            else:
                # Find corresponding provn file
                provn_file = os.path.join(os.path.dirname(os.path.dirname(
                                os.path.abspath(__file__))), example_file)
                provn_file = open(provn_file, 'r')
                ex_provn = provn_file.read()


                url = "https://provenance.ecs.soton.ac.uk/validator/provapi/documents/"
                headers = { 'Content-type' : "text/provenance-notation",
                            'Accept' : "text/turtle" }
                # print urllib.urlencode(data)
                req = urllib2.Request(url, ex_provn, headers)
                response = urllib2.urlopen(req)
                ttl_file_url = response.geturl()

            # Read turtle
            self.examples[example_file] = Graph()
            self.examples[example_file].parse(ttl_file_url, format='turtle')

    def test_check_classes(self):
        my_exception = dict()
        for example_name, example_graph in self.examples.items():
            # Check that all entity, activity, agent are defined in the data model
            sub_types = get_sub_class_names(example_graph)
            for not_recognised_sub_type in (sub_types - self.sub_types):
                key = example_graph.qname(not_recognised_sub_type)
                if key in my_exception:
                    my_exception[key].add(example_name)
                else:
                    my_exception[key] = set([example_name])

        if my_exception:
            error_msg = ""
            for class_name, examples in my_exception.items():
                error_msg += "\n Unrecognised sub-type: "+str(class_name)+\
                                " (from "+', '.join(examples)+")"
            raise Exception(error_msg)

    def test_check_attributes(self):
        my_exception = dict()
        for example_name, example_graph in self.examples.items():
            # Find all attributes
            for s,p,o in example_graph.triples((None, None, None)):
                # To be a DataTypeProperty then o must be a literal
                # if isinstance(o, rdflib.term.Literal):
                if p not in self.common_attributes:
                    # Get all defined types of current object
                    found_attributes = False
                    class_names = ""
                    for class_name in example_graph.objects(s, RDF['type']):

                        attributes = self.attributes.get(class_name)

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
                        key = example_graph.qname(p)+" in "+class_names[2:]
                        if not key in my_exception:
                            my_exception[key] = set([example_name])
                        else:
                            my_exception[key].add(example_name)


        if my_exception:
            error_msg = ""
            for att_name, example_names in my_exception.items():
                error_msg += "\n Unrecognised attribute: "+str(att_name)+\
                                " (from "+', '.join(example_names)+")"
            raise Exception(error_msg)


if __name__ == '__main__':
    unittest.main()