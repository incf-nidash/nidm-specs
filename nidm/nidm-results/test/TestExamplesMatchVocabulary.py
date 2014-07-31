#!/usr/bin/env python
'''Test that NIDM-Results examples are consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''
import unittest
import os
# from subprocess import call #jb: call not used 
import re
import rdflib

from rdflib.graph import Graph
from TestCommons import *
from CheckConsistency import *

RELPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestExamples(unittest.TestCase):

    def setUp(self):
        # Retreive owl file for NIDM-Results
        owl_file = os.path.join(RELPATH, 'nidm-results.owl')
        # check the file exists
        assert os.path.exists(owl_file)
        # Read owl (turtle) file
        self.owl = Graph()

        # This is a workaround to avoid issue with "#" in base prefix as 
        # described in https://github.com/RDFLib/rdflib/issues/379,
        # When the fix is introduced in rdflib these 2 lines will be replaced by:
        # self.owl.parse(owl_file, format='turtle')
        owl_txt = open(owl_file, 'r').read().replace("http://www.w3.org/2002/07/owl#", 
                        "http://www.w3.org/2002/07/owl")
        self.owl.parse(data=owl_txt, format='turtle')
        
        # Retreive all classes defined in the owl file
        self.sub_types = get_class_names_in_owl(self.owl) #set(); #{'entity': set(), 'activity': set(), 'agent' : set()}
        # For each class find out attribute list as defined by domain in attributes
        # For each ObjectProperty found out corresponding range
        attributes_ranges = get_attributes_from_owl(self.owl)
        self.attributes = attributes_ranges[0]
        self.ranges = attributes_ranges[1]      
        self.type_restrictions = attributes_ranges[2]      

        self.examples = dict()
        for example_file in example_filenames:
            provn_file = os.path.join(os.path.dirname(os.path.dirname(
                                os.path.abspath(__file__))), example_file)
            ttl_file_url = get_turtle(provn_file)

            # Read turtle
            self.examples[example_file] = Graph()
            self.examples[example_file].parse(ttl_file_url, format='turtle')

    def test_check_classes(self):
        my_exception = dict()
        for example_name, example_graph in self.examples.items():
            # Check that all entity, activity, agent are defined in the data model
            exception_msg = check_class_names(example_graph, example_name, class_names=self.sub_types)
            my_exception = merge_exception_dict(my_exception, exception_msg)

        # Aggredate errors over examples for conciseness
        if my_exception:
            error_msg = ""
            for unrecognised_class_name, examples in my_exception.items():
                error_msg += unrecognised_class_name+" (from "+', '.join(examples)+")"
            raise Exception(error_msg)

    def test_check_attributes(self):
        my_exception = dict()
        my_range_exception = dict()
        my_restriction_exception = dict()
        for example_name, example_graph in self.examples.items():
            exception_msg = check_attributes(example_graph, example_name, 
                self.attributes, self.ranges, self.type_restrictions)
            
            my_exception = merge_exception_dict(my_exception, exception_msg[0])
            my_range_exception = merge_exception_dict(my_range_exception, exception_msg[1])
            my_restriction_exception = merge_exception_dict(my_restriction_exception, exception_msg[2])

        # Aggregate errors over examples for conciseness
        error_msg = ""
        for found_exception in list([my_exception, my_range_exception, my_restriction_exception]):
            if found_exception:
                for unrecognised_attribute, example_names in found_exception.items():
                    error_msg += unrecognised_attribute+" (from "+', '.join(example_names)+")"
        # if my_range_exception:
        #     for unrecognised_range, example_names in my_range_exception.items():
        #         error_msg += unrecognised_range+" (from "+', '.join(example_names)+")"
        if error_msg:
            raise Exception(error_msg)

if __name__ == '__main__':
    unittest.main()
