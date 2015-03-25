#!/usr/bin/env python
'''Test that NIDM-Results examples are consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''
import unittest
import os, sys

from rdflib.graph import Graph
from TestCommons import *
import glob

RELPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NIDMPATH = os.path.dirname(RELPATH)
SCRIPTSPATH = os.path.join(NIDMPATH, os.pardir, "scripts")

# Append parent script directory to path
sys.path.append(SCRIPTSPATH)
from OwlReader import OwlReader

class TestExamples(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestExamples, self).__init__(*args, **kwargs)    
        # Retreive owl file for NIDM-Results
        owl_file = os.path.join(RELPATH, 'terms', 'nidm-results.owl')

        # check the file exists
        assert os.path.exists(owl_file)
        # Read owl (turtle) file
        import_files = glob.glob(os.path.join(os.path.dirname(owl_file), os.pardir, os.pardir, "imports", '*.ttl'))
        # self.owl = get_owl_graph(owl_file, import_files)
        self.owlreader = OwlReader(owl_file, import_files)
        self.owl = self.owlreader.graph

       
        # Retreive all classes defined in the owl file
        self.sub_types = self.owlreader.get_class_names() #set(); #{'entity': set(), 'activity': set(), 'agent' : set()}
        # For each class find out attribute list as defined by domain in attributes
        # For each ObjectProperty found out corresponding range
        # attributes_ranges = get_attributes_from_owl(self.owl)
        self.attributes, self.ranges, self.type_restrictions, self.parent_ranges = self.owlreader.get_attributes()
        # attributes_ranges[0]
        # self.ranges = attributes_ranges[1]      
        # self.type_restrictions = attributes_ranges[2]      

        self.examples = dict()
        for example_file in example_filenames:
            provn_file = os.path.join(os.path.dirname(os.path.dirname(
                                os.path.abspath(__file__))), example_file)
            # ttl_file_url = get_turtle(provn_file)
            ttl_file = provn_file.replace(".provn", ".ttl")

            # Read turtle
            self.examples[example_file] = Graph()
            self.examples[example_file].parse(ttl_file, format='turtle')

    def test_check_classes(self):
        logger.info("TestExamples: test_check_classes")
        my_exception = dict()
        for example_name, example_graph in self.examples.items():
            # Check that all entity, activity, agent are defined in the data model
            exception_msg = self.owlreader.check_class_names(example_graph, example_name)
            my_exception = merge_exception_dict(my_exception, exception_msg)

        # Aggredate errors over examples for conciseness
        if my_exception:
            error_msg = ""
            for unrecognised_class_name, examples in my_exception.items():
                error_msg += unrecognised_class_name+" (from "+', '.join(examples)+")"
            raise Exception(error_msg)

    def test_check_attributes(self):
        logger.info("TestExamples: test_check_attributes")
        my_exception = dict()
        my_range_exception = dict()
        my_restriction_exception = dict()
        for example_name, example_graph in self.examples.items():
            exception_msg = self.owlreader.check_attributes(example_graph, example_name)
            
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
