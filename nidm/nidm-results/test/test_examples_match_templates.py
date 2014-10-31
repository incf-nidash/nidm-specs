#!/usr/bin/env python
'''Test that NIDM-Results examples were made using the templates defined in 
nidm/nidm-results/terms/templates. 

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''
import os
import unittest
from rdflib import Graph
from rdflib.compare import *

NIDM_RESULTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.join(NIDM_RESULTS_DIR, "scripts")
import sys
sys.path.append(SCRIPT_DIR)
import create_spm_example
import create_spm_example_001
import create_spm_example_002
from TestCommons import *


class TestExamplesMatchTemplates(unittest.TestCase):    
    def _parse_graph(self, ex_file, replace_by=None):
        ex_fid = open(ex_file, "r")
        ex = ex_fid.read()
        ex_fid.close()
        my_graph = Graph()
        
        # Replace before parsing new graph so that if parsing fails the file
        # is in a consistent state
        if replace_by is not None:
            # Write back current version of the example (the purpose of this 
            # function is just testing not updating the example).
            spm_ex_fid = open(ex_file, "w")
            spm_ex_fid.write(replace_by)
            spm_ex_fid.close()

        try:
            my_graph.parse(data=ex, format="turtle")
        except BadSyntax:
            my_graph=None

        return list([my_graph, ex])

    def _compare_graphs(self, graph1, graph2):
        iso1 = to_isomorphic(graph1)
        iso2 = to_isomorphic(graph2)

        found_difference = False
        if iso1 != iso2:
            in_both, in_first, in_second = graph_diff(iso1, iso2)

            # diff_graph = (in_first+in_second)
            found_difference_1 = display_graph(in_first, "\t In first: ")
            found_difference_2 = display_graph(in_second, "\t In second: ")
            found_difference = found_difference_1 or found_difference_2

        return found_difference

    def test_spm_results(self):
        example_file = os.path.join(NIDM_RESULTS_DIR, "spm", "spm_results.ttl")

        current_graph, spm_current = self._parse_graph(example_file)
        create_spm_example.main()
        updated_graph, unused = self._parse_graph(example_file, spm_current)


        found_difference = self._compare_graphs(current_graph, updated_graph)


        if found_difference:
            raise Exception("spm_results.ttl is not up to date with templates. \
                Please use nidm/nidm-results/scripts/create_spm_examples.py.")

    def test_spm_ex001(self):
        example_file = os.path.join(NIDM_RESULTS_DIR, "spm", \
            "example001", 'example001_spm_results.ttl')

        current_graph, spm_current = self._parse_graph(example_file)
        create_spm_example_001.main()
        updated_graph, unused = self._parse_graph(example_file, spm_current)

        found_difference = self._compare_graphs(current_graph, updated_graph)

        if found_difference:
            raise Exception("example001_spm_results.ttl is not up to date  \
                with templates. Please use \
                nidm/nidm-results/scripts/create_spm_example_001.py.")

    def test_spm_ex002(self):
        spm_example_file = os.path.join(NIDM_RESULTS_DIR, "spm", \
            "example002", 'spm_results_2contrasts.ttl')

        current_graph, spm_current = self._parse_graph(spm_example_file)
        create_spm_example_002.main()
        updated_graph, unused = self._parse_graph(spm_example_file, spm_current)

        found_difference = self._compare_graphs(current_graph, updated_graph)

        if found_difference:
            raise Exception("example002/spm_results_2contrasts.ttl is not up \
                to date with templates. Please use \
                nidm/nidm-results/scripts/create_spm_example_002.py.")

if __name__ == '__main__':
    unittest.main()