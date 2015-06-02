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

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)
logger.info(' ---------- Debug log ----------')



class TestSpecifications(unittest.TestCase):

    def setUp(self):
        logger.info("Test: TestSpecifications")

    def test_nidm_results(self):
        component = "nidm-results"
        self._run(component, create_res_spec, "create_results_specification",
                  "dev")

    def test_nidm_results_020(self):
        component = "nidm-results"
        self._run(component, create_res_spec, "create_results_specification",
                  "0.2.0")

    def test_nidm_results_100(self):
        component = "nidm-results"
        self._run(component, create_res_spec, "create_results_specification",
                  "1.0.0")

    def test_nidm_results_110(self):
        component = "nidm-results"
        self._run(component, create_res_spec, "create_results_specification",
                  "1.1.0")

    def test_nidm_experiment(self):
        component = "nidm-experiment"
        self._run(component, create_expe_spec, "create_expe_specification")

    def _run(self, component, spec_fun, spec_fun_name, param=None):
        original_spec = self._get_spec_txt(component, None, param)
        if param is not None:
            spec_fun(param)
        else:
            spec_fun()
        updated_spec = self._get_spec_txt(component, original_spec, param)
        self._compare(component, original_spec, updated_spec, spec_fun_name, param)

    def _get_spec_txt(self, component, original=None, version=None):
        if not version:
            version = "dev"
        else:
            version = version.replace(".", "")

        spec_file = os.path.join(REPO_ROOT, "doc", "content", "specs", 
                component+"_"+version+".html")
        print str(spec_file)        

        with open(spec_file, 'r') as f:
            spec_txt = f.read()

        if original is not None:
            # Write back original text found in README         
            with open(spec_file, 'w') as f:
                f.write(original)

        return spec_txt
            
    def _compare(self, component, original_spec, updated_spec, spec_fun_name,\
        param=None):
        if not (updated_spec == original_spec):
            original_spec_lines = original_spec.splitlines()
            updated_spec_lines = updated_spec.splitlines()
            diff = difflib.unified_diff(original_spec_lines, 
                updated_spec_lines)
            logger.debug('\n'.join(diff))

            if param is None:
                version = ""
            else:
                version = param

            error_msg = component+" Specification outdated, please update "\
                "using python nidm/"+component+"/scripts/"+spec_fun_name+".py"\
                +" "+version

            raise Exception(error_msg)

if __name__ == '__main__':
    unittest.main()
