#!/usr/bin/env python
''' Automatically-generates NIDM-Experiment specification based on 
nidm-experiment.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

import logging
import os
from rdflib.compare import *
import sys
import collections

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDM_EXPE_PATH = os.path.dirname(RELPATH)

# Append test directory to path
sys.path.append(os.path.join(RELPATH, "..", "test"))
from CheckConsistency import *

# Append parent script directory to path
sys.path.append(os.path.join(RELPATH, "..", "..", "..", "scripts"))
from owl_to_webpage import OwlSpecification

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TERMS_FOLDER = os.path.join(NIDM_EXPE_PATH, 'terms')
RELEASED_TERMS_FOLDER = os.path.join(TERMS_FOLDER, "releases")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        nidm_original_version = sys.argv[1]
        nidm_version = nidm_original_version.replace(".", "")
    else:
        nidm_version = 'dev'

    # Retreive owl file for NIDM-Results
    if nidm_version == "dev":
        owl_file = os.path.join(TERMS_FOLDER, 'nidm-results.owl')
    else:
        owl_file = os.path.join(RELEASED_TERMS_FOLDER, \
            'nidm-results_'+nidm_version+'.owl')

    # check the file exists
    assert os.path.exists(owl_file)

    components =  collections.OrderedDict()
    components["Project"] = [NIDM['ProjectObject']]
    components["Study"] = [NIDM['StudyObject']]
    components["Acquisition"] = [NIDM['AcquisitionObject']]
    components["Other entities"] = []

    # Add manually used and wasDerivedFrom because these are not stored in the 
    # owl file (no relations yet!)
    used_by = { 
    }
    generated_by = { 
    }
    derived_from = {       
    }

    owlspec = OwlSpecification(owl_file, "NIDM-Experiment", components, used_by, 
        generated_by, derived_from)

    component_name = "nidm-experiment"
    owlspec._header_footer(component=component_name)
    owlspec.write_specification(component=component_name, version=nidm_version)


