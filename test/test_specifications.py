#!/usr/bin/env python
'''Test that NIDM-Results specification is consistent with nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2015
'''
import unittest
import os
import sys
import difflib
import logging

RELPATH = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(RELPATH)

components = list(["nidm-results", "nidm-experiment"])

script_path = os.path.join(REPO_ROOT, "nidm", "nidm-results", "scripts")
sys.path.append(script_path)
script_path = os.path.join(REPO_ROOT, "nidm", "nidm-experiment", "scripts")
sys.path.append(script_path)

from create_results_specification import main as create_res_spec
from create_expe_specification import main as create_expe_spec

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestSpecifications(unittest.TestCase):

    def setUp(self):
        logger.info("Test: TestSpecifications")

    def test_nidm_results(self):
        component = "nidm-results"
        self._run(component, create_res_spec, "create_results_specification")

    def test_nidm_experiment(self):
        component = "nidm-experiment"
        self._run(component, create_expe_spec, "create_expe_specification")

    def _run(self, component, spec_fun, spec_fun_name):
        original_spec = self._get_spec_txt(component)
        spec_fun()
        updated_spec = self._get_spec_txt(component, original_spec)
        self._compare(component, original_spec, updated_spec, spec_fun_name)

    def _get_spec_txt(self, component, original=None):
        spec_file = os.path.join(REPO_ROOT, "doc", "content", "specs", 
                component+"_dev.html")
        spec_fid = open(spec_file, 'r')
        spec_txt = spec_fid.read()
        spec_fid.close()

        if original is not None:
            # Write back original text found in README           
            spec_fid = open(spec_file, 'w')
            spec_fid.write(original)
            spec_fid.close()

        return spec_txt
            
    def _compare(self, component, original_spec, updated_spec, spec_fun_name):
        if not (updated_spec == original_spec):
            original_spec_lines = original_spec.splitlines()
            updated_spec_lines = updated_spec.splitlines()
            diff = difflib.unified_diff(original_spec_lines, 
                updated_spec_lines)
            logger.debug('\n'.join(diff))

            error_msg = component+" Specification outdated, please update "\
                "using python nidm/"+component+"/scripts/"+spec_fun_name+".py"

            raise Exception(error_msg)

if __name__ == '__main__':
    unittest.main()
