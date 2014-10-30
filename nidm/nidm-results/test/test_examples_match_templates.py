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
import create_spm_examples
from TestCommons import *


class TestExamplesMatchTemplates(unittest.TestCase):    

    def test_spm_results(self):
        # test_examples_match_templates()
        spm_example_file = os.path.join(NIDM_RESULTS_DIR, "spm", "spm_results.ttl")

        spm_ex_fid = open(spm_example_file, "r")
        spm_current = spm_ex_fid.read()
        spm_ex_fid.close()
        current_graph = Graph()
        current_graph.parse(data=spm_current, format="turtle")

        create_spm_examples.main()
        spm_ex_fid = open(spm_example_file, "r")
        spm_updated = spm_ex_fid.read()
        spm_ex_fid.close()
        updated_graph = Graph()
        updated_graph.parse(data=spm_updated, format="turtle")

        iso1 = to_isomorphic(current_graph)
        iso2 = to_isomorphic(updated_graph)

        found_difference = False
        if iso1 != iso2:
            in_both, in_first, in_second = graph_diff(iso1, iso2)

            # diff_graph = (in_first+in_second)
            found_difference_1 = display_graph(in_first, "\t In first: ")
            found_difference_2 = display_graph(in_second, "\t In second: ")
            found_difference = found_difference_1 or found_difference_2

        # Write back current version of the example (the purpose of this 
        # function is just testing not updating the example).
        spm_ex_fid = open(spm_example_file, "w")
        spm_current = spm_ex_fid.write(spm_current)
        spm_ex_fid.close()

        if found_difference:
            raise Exception("spm_results.ttl is not up to date with templates. \
                Please use nidm/nidm-results/scripts/create_spm_examples.py.")


if __name__ == '__main__':
    unittest.main()