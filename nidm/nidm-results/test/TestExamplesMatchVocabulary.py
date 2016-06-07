#!/usr/bin/env python
'''Test that NIDM-Results examples are consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''
import unittest
import os, sys

from rdflib.graph import Graph
from nidmresults.test.test_commons import *
import glob

RELPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NIDMPATH = os.path.dirname(RELPATH)
SCRIPTSPATH = os.path.join(NIDMPATH, os.pardir, "scripts")

# Append parent script directory to path
sys.path.append(SCRIPTSPATH)
from nidmresults.owl.owl_reader import OwlReader

class TestExamples(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestExamples, self).__init__(*args, **kwargs)    

        namespaces_def = os.path.join(RELPATH, "terms", "templates", 'Namespaces.txt')
        fid = open(namespaces_def, "r")
        namespaces = fid.read()
        fid.close()

        self.term_examples = glob.glob(os.path.join(RELPATH, "terms", "examples", '*.txt'))
        self.example_files = example_filenames.union(self.term_examples)

        self.examples = dict()
        self.owl_files = dict()

        for example_file in self.example_files:
            ttl_file = os.path.join(os.path.dirname(os.path.dirname(
                                os.path.abspath(__file__))), example_file)
            # ttl_file_url = get_turtle(provn_file)
            # ttl_file = provn_file.replace(".provn", ".ttl")

            # Read turtle
            self.examples[example_file] = Graph()
            if example_file in self.term_examples:
                fid = open(ttl_file, "r")
                ttl_txt = fid.read()
                fid.close()

                self.examples[example_file].parse(data=namespaces+ttl_txt, format='turtle')
            else:
                self.examples[example_file].parse(ttl_file, format='turtle')

            term_dir = os.path.join(os.path.dirname(ttl_file), os.pardir, 'terms')
            if not os.path.isdir(term_dir):
                term_dir = os.path.join(os.path.dirname(ttl_file), os.pardir, os.pardir, 'terms')

            # Retreive owl file for minimal examples
            if not os.path.isdir(term_dir):
                term_dir = os.path.join(
                    os.path.dirname(ttl_file), os.pardir, os.pardir,
                    os.pardir, 'terms')
            owl_files = glob.glob(os.path.join(term_dir, '*.owl'))
            self.owl_files[example_file] = owl_files[0]
            self.owl_readers = dict()

    def _load_owl(self, owl_file):
        if owl_file in self.owl_readers:
            self.owl = self.owl_readers[owl_file]
        else:
            # Retreive owl file for NIDM-Results
            # owl_file = os.path.join(RELPATH, 'terms', 'nidm-results.owl')

            # check the file exists
            assert os.path.exists(owl_file)
            # Read owl (turtle) file

            owl_path = os.path.dirname(owl_file)

            if not "extension" in os.path.dirname(owl_file):
                import_files = glob.glob(os.path.join(owl_path, \
                    os.pardir, os.pardir, "imports", '*.ttl'))
            else:
                import_files = glob.glob(os.path.join(owl_path, \
                    os.pardir, os.pardir, os.pardir, os.pardir, "imports", '*.ttl'))
                # Main ontology file
                import_files += glob.glob(os.path.join(owl_path, \
                    os.pardir, os.pardir, os.pardir, "terms", '*.owl'))

            self.owl = OwlReader(owl_file, import_files)
            self.owl_readers[owl_file] = self.owl

    def test_check_classes(self):
        logger.info("TestExamples: test_check_classes")
        my_exception = dict()
        for example_file in self.example_files:

            example_name = example_file
            example_graph = self.examples[example_file]
            owl = self.owl_files[example_file]

            self._load_owl(owl)

            # Check that all entity, activity, agent are defined in the data model
            exception_msg = self.owl.check_class_names(example_graph, example_name)
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
        for example_file in self.example_files:
            example_name = example_file
            example_graph = self.examples[example_file]
            owl = self.owl_files[example_file]

            self._load_owl(owl)

            exception_msg = self.owl.check_attributes(example_graph, example_name)
            
            my_exception = merge_exception_dict(my_exception, exception_msg[0])
            if not example_file in self.term_examples:
                my_range_exception = merge_exception_dict(my_range_exception, exception_msg[1])
            else:
                # Ignore range exceptions for test examples (as for object 
                # properties the linked object will be missing)
                my_range_exception = dict()
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
