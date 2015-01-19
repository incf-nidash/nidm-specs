#!/usr/bin/env python
''' Automatically-generates NIDM-Results specification based on nidm-results.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

import logging
import os
from rdflib.compare import *
import sys
import collections


RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)

# Append test directory to path
sys.path.append(os.path.join(RELPATH, "..", "test"))
from CheckConsistency import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TERMS_FOLDER = os.path.join(NIDMRESULTSPATH, 'terms')
DOC_FOLDER = os.path.join(os.path.dirname(os.path.dirname(NIDMRESULTSPATH)), \
    'doc', 'content', 'specs')
INCLUDE_FOLDER = os.path.join(DOC_FOLDER, "include")

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
        owl_file = os.path.join(INCLUDE_FOLDER, 'nidm-results_'+nidm_version+'.owl')

    # check the file exists
    assert os.path.exists(owl_file)


    components =  collections.OrderedDict()
    components["Model fitting"] = [NIDM['Data'], NIDM['ErrorModel'], NIDM['DesignMatrix'], 
             NIDM['ModelParametersEstimation'], NIDM['ParameterEstimateMap'],
             NIDM['GrandMeanMap'],
             NIDM['ContrastEstimation'], NIDM['ResidualMeanSquaresMap'], NIDM['MaskMap'], NIDM['ContrastWeights'],
             NIDM['ContrastMap'], NIDM['StatisticMap']]
    components["Inference"] = [NIDM['Inference'], NIDM['HeightThreshold'], NIDM['ExtentThreshold'], 
             NIDM['InferenceMaskMap'], NIDM['ExcursionSet'], NIDM['ClusterLabelsMap'], NIDM['SearchSpaceMap'], 
             NIDM['Cluster'], NIDM['Peak'],
             NIDM['Coordinate']]
    components["SPM-specific Concepts"] = [SPM['ReselsPerVoxelMap'], NIDM['SPM']]
    components["FSL-specific Concepts"] = [FSL['CenterOfGravity'], NIDM['FSL']]

    # Add manually used and wasDerivedFrom because these are not stored in the owl file
    used_by = { 
                NIDM['Data']: [NIDM['ModelParametersEstimation']],
                NIDM['ErrorModel']: [NIDM['ModelParametersEstimation']],
                NIDM['DesignMatrix']: [NIDM['ModelParametersEstimation'],
                                       NIDM['ContrastEstimation']],
                NIDM['ParameterEstimateMap']: [NIDM['ContrastEstimation']],
                NIDM['ResidualMeanSquaresMap']: [NIDM['ContrastEstimation']],
                NIDM['MaskMap']: [NIDM['ContrastEstimation']],
                NIDM['ContrastWeights']: [NIDM['ContrastEstimation']],
                NIDM['ContrastMap']: [NIDM['Inference']], 
                NIDM['StatisticMap']: [NIDM['Inference']], 
    }
    generated_by = { 
                NIDM['ParameterEstimateMap']: NIDM['ModelParametersEstimation'],
                NIDM['ResidualMeanSquaresMap']: NIDM['ModelParametersEstimation'],
                NIDM['MaskMap']: NIDM['ModelParametersEstimation'],
                NIDM['ContrastMap']: NIDM['ContrastEstimation'], 
                NIDM['StatisticMap']: NIDM['ContrastEstimation'], 
    }
    derived_from = {
                NIDM['Cluster']: NIDM['ExcursionSet'],
                NIDM['Peak']: NIDM['Cluster'],                
    }

    if nidm_version == "020":
        # In version 0.2.0 "ErrorModel" was called "NoiseModel"
        components["Model fitting"][1] = NIDM['NoiseModel']
        used_by.pop(NIDM['ErrorModel'], None)
        used_by[NIDM['NoiseModel']] = [NIDM['ModelParametersEstimation']]
        # No "InferenceMaskMap"
        components["Inference"] = [NIDM['Inference'], NIDM['HeightThreshold'], NIDM['ExtentThreshold'], 
             NIDM['ExcursionSet'], NIDM['ClusterLabelsMap'], NIDM['SearchSpaceMap'], 
             NIDM['Cluster'], NIDM['Peak'],
             NIDM['Coordinate']]

    owlspec = OwlSpecification(owl_file, "NIDM-Results", components, used_by, 
        generated_by, derived_from)

    owlspec._header_footer(os.path.join(INCLUDE_FOLDER, "nidm-results_head.html"),
         os.path.join(INCLUDE_FOLDER, "nidm-results_foot.html"))

    if not nidm_version == "dev":
        if nidm_version == "020":
            # Previous version
            owlspec.text = owlspec.text.replace("nidm-results_020.html", "nidm-results_010.html")
        owlspec.text = owlspec.text.replace("(version under development)", nidm_original_version)
        owlspec.text = owlspec.text.replace("nidm-results_dev.html", "nidm-results_"+nidm_version+".html")
        owlspec.text = owlspec.text.replace("img/", "img/nidm-results_"+nidm_version+"/")

    owlspec.write_specification(os.path.join(DOC_FOLDER, "nidm-results_"+nidm_version+".html"))


