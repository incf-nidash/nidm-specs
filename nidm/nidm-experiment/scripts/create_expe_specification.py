#!/usr/bin/env python
''' Automatically-generates NIDM-Experiment specification based on nidm-experiment.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

import logging
import os
from rdflib.compare import *
import sys
import collections
import glob

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDM_EXPE_PATH = os.path.dirname(RELPATH)
NIDMPATH = os.path.join(NIDM_EXPE_PATH, os.pardir)

# Append parent script directory to path
sys.path.append(os.path.join( os.path.dirname(os.path.dirname(\
    os.path.dirname(RELPATH))), "scripts"))
from owl_to_webpage import OwlSpecification
from nidmresults.objects.constants_rdflib import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TERMS_FOLDER = os.path.join(NIDM_EXPE_PATH, 'terms')
RELEASED_TERMS_FOLDER = os.path.join(TERMS_FOLDER, "releases")

def main():
    if len(sys.argv) > 1:
        nidm_original_version = sys.argv[1]
        nidm_version = nidm_original_version.replace(".", "")
    else:
        nidm_original_version = "dev"
        nidm_version = 'dev'

    # Retreive owl file for NIDM-Results
    if nidm_version == "dev":
        owl_file = os.path.join(TERMS_FOLDER, 'nidm-experiment.owl')
        import_files = glob.glob(os.path.join(NIDMPATH, "imports", '*.ttl'))
    else:
        owl_file = os.path.join(RELEASED_TERMS_FOLDER, \
            'nidm-experiment_'+nidm_version+'.owl')
        # For released version of the ontology imports are embedded
        import_files = None

    # check the file exists
    assert os.path.exists(owl_file)

    subcomponents =  collections.OrderedDict()

    subcomponents["Investigation"] = [NIDM['InvestigationCollection'],
        NIDM['InvestigationProcess'],NIDM['Model'],
        NIDM['ModelSpecification'],NIDM['Group'],
        NIDM['Contrast'], NIDM['Task'],NIDM['Condition']]
    subcomponents["Session"] = [NIDM['DataCollection'],NIDM['SessionAcquisition']]
    subcomponents["Serie"] = [NIDM['AnatomyImagingAcquisition'],
        NIDM['TaskBasedImagingAcquisition'], NIDM['AnatomicalScan'],
        NIDM['FunctionalScan'], NIDM['BehaviorAndConditionOnsets'],
        NIDM['MRScanner'], NIDM['PresentationSoftware']]

    subcomponents["Project"] = [NIDM['ProjectObject']]
    subcomponents["Study"] = [NIDM['StudyObject']]
    subcomponents["Acquisition"] = [NIDM['AcquisitionObject']]
    subcomponents["Other"] = []

    # Add manually used and wasDerivedFrom because these are not stored in the
    # owl file (no relations yet!)
    used_by = {
    }
    generated_by = {
    }
    derived_from = {
    }

    owlspec = OwlSpecification(owl_file, import_files, "NIDM-Experiment",
        subcomponents, used_by, generated_by, derived_from,
        prefix=str(NIDM))

    if not nidm_version == "dev":
        owlspec.text = owlspec.text.replace("(under development)", nidm_original_version)
        owlspec.text = owlspec.text.replace("img/", "img/nidm-results_"+nidm_version+"/")

    component_name = "nidm-experiment"
    owlspec._header_footer(component=component_name, version=nidm_version)
    owlspec.write_specification(component=component_name, version=nidm_version)


if __name__ == '__main__':
    main()
