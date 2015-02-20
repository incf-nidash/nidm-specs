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

# Append parent script directory to path
sys.path.append(os.path.join( os.path.dirname(os.path.dirname(\
    os.path.dirname(RELPATH))), "scripts"))
from owl_to_webpage import OwlSpecification
from Constants import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TERMS_FOLDER = os.path.join(NIDM_EXPE_PATH, 'terms')
RELEASED_TERMS_FOLDER = os.path.join(TERMS_FOLDER, "releases")

def main():
    if len(sys.argv) > 1:
        nidm_original_version = sys.argv[1]
        nidm_version = nidm_original_version.replace(".", "")
    else:
        nidm_version = 'dev'

    # Retreive owl file for NIDM-Results
    if nidm_version == "dev":
        owl_file = os.path.join(TERMS_FOLDER, 'nidm-experiment.owl')
    else:
        owl_file = os.path.join(RELEASED_TERMS_FOLDER, \
            'nidm-experiment_'+nidm_version+'.owl')

    # check the file exists
    assert os.path.exists(owl_file)

    subcomponents =  collections.OrderedDict()
    
    subcomponents["Investigation"] = [NIDM_EXPERIMENT['InvestigationCollection'],
        NIDM_EXPERIMENT['InvestigationProcess'],NIDM_EXPERIMENT['Model'], 
        NIDM_EXPERIMENT['ModelSpecification'],NIDM_EXPERIMENT['Group'],
        NIDM_EXPERIMENT['Contrast'], NIDM_EXPERIMENT['Task'],NIDM_EXPERIMENT['Condition']]
    subcomponents["Session"] = [NIDM_EXPERIMENT['DataCollection'],NIDM_EXPERIMENT['SessionAcquisition']]
    subcomponents["Serie"] = [NIDM_EXPERIMENT['AnatomyImagingAcquisition'],
        NIDM_EXPERIMENT['TaskBasedImagingAcquisition'], NIDM_EXPERIMENT['AnatomicalScan'],
        NIDM_EXPERIMENT['FunctionalScan'], NIDM_EXPERIMENT['BehaviorAndConsitionOnsets'],
        NIDM_EXPERIMENT['MRScanner'], NIDM_EXPERIMENT['PresentationSoftware']]

    subcomponents["Project"] = [NIDM_EXPERIMENT['ProjectObject']]
    subcomponents["Study"] = [NIDM_EXPERIMENT['StudyObject']]
    subcomponents["Acquisition"] = [NIDM_EXPERIMENT['AcquisitionObject']]
    subcomponents["Other"] = []

    # Add manually used and wasDerivedFrom because these are not stored in the 
    # owl file (no relations yet!)
    used_by = { 
    }
    generated_by = { 
    }
    derived_from = {       
    }

    owlspec = OwlSpecification(owl_file, "NIDM-Experiment", subcomponents, \
        used_by, generated_by, derived_from, prefix=str(NIDM_EXPERIMENT))

    if not nidm_version == "dev":
        owlspec.text = owlspec.text.replace("(under development)", nidm_original_version)
        owlspec.text = owlspec.text.replace("img/", "img/nidm-results_"+nidm_version+"/")

    component_name = "nidm-experiment"
    owlspec._header_footer(component=component_name)
    owlspec.write_specification(component=component_name, version=nidm_version)


if __name__ == '__main__':
    main()