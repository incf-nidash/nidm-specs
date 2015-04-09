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
import glob

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
NIDMPATH = os.path.join(NIDMRESULTSPATH, os.pardir)

# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from owl_to_webpage import OwlSpecification
from Constants import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TERMS_FOLDER = os.path.join(NIDMRESULTSPATH, 'terms')
RELEASED_TERMS_FOLDER = os.path.join(TERMS_FOLDER, "releases")

def main(nidm_original_version):
    nidm_version = nidm_original_version.replace(".", "")

    # Retreive owl file for NIDM-Results
    if nidm_version == "dev":
        owl_file = os.path.join(TERMS_FOLDER, 'nidm-results.owl')
        import_files = glob.glob(os.path.join(NIDMPATH, "imports", '*.ttl'))

    else:
        owl_file = os.path.join(RELEASED_TERMS_FOLDER, \
            'nidm-results_'+nidm_version+'.owl')
        # For released version of the ontology imports are embedded
        import_files = None

    # check the file exists
    assert os.path.exists(owl_file)

    components =  collections.OrderedDict()
    components["General"] = [NIDM['Map']]
    components["Parameters estimation"] = [NIDM['Data'], NIDM['ErrorModel'], NIDM['DesignMatrix'], 
             NIDM['ModelParametersEstimation'],  
             NIDM['ParameterEstimateMap'],
             NIDM['GrandMeanMap'], NIDM['ResidualMeanSquaresMap'], 
             NIDM['MaskMap']]    
    components["Contrast estimation"] = [NIDM_CONTRAST_ESTIMATION, 
             NIDM['ContrastWeights'], NIDM['ContrastMap'], NIDM['StatisticMap'], 
             NIDM['ContrastStandardErrorMap']]
    components["Inference"] = [NIDM['Inference'], NIDM['HeightThreshold'], NIDM['ExtentThreshold'], 
             NIDM['ExcursionSetMap'], NIDM['ClusterLabelsMap'], NIDM['SearchSpaceMaskMap'], 
             NIDM['SignificantCluster'], NIDM['Peak'], NIDM['Coordinate'], 
             NIDM['ConjunctionInference'], NIDM['ClusterDefinitionCriteria'],
             NIDM['DisplayMaskMap'], NIDM['PeakDefinitionCriteria']]
    components["SPM-specific Concepts"] = [SPM['ReselsPerVoxelMap']]
    components["FSL-specific Concepts"] = [FSL['ClusterCenterOfGravity']]

    if nidm_version == 'dev':
        # For the developement version only list all terms that were not 
        # referred to in other components
        components["Other"] = []

    # Add manually used and wasDerivedFrom because these are not stored in the owl file
    used_by = { 
                NIDM['Data']: [NIDM['ModelParametersEstimation']],
                NIDM['ErrorModel']: [NIDM['ModelParametersEstimation']],
                NIDM['DesignMatrix']: [NIDM['ModelParametersEstimation'],
                                       NIDM_CONTRAST_ESTIMATION],
                NIDM['ParameterEstimateMap']: [NIDM_CONTRAST_ESTIMATION],
                NIDM['ResidualMeanSquaresMap']: [NIDM_CONTRAST_ESTIMATION],
                NIDM['MaskMap']: [NIDM_CONTRAST_ESTIMATION],
                NIDM['ContrastWeights']: [NIDM_CONTRAST_ESTIMATION],
                NIDM['ContrastMap']: [NIDM['Inference']], 
                NIDM['StatisticMap']: [NIDM['Inference']],
                NIDM['MaskMap']: [NIDM['ModelParametersEstimation']],
                NIDM['ClusterDefinitionCriteria']: [NIDM['Inference']], 
                NIDM['DisplayMaskMap']: [NIDM['Inference']], 
                NIDM['PeakDefinitionCriteria']: [NIDM['Inference']], 
    }
    generated_by = { 
                NIDM['ParameterEstimateMap']: NIDM['ModelParametersEstimation'],
                NIDM['ResidualMeanSquaresMap']: NIDM['ModelParametersEstimation'],
                NIDM['MaskMap']: NIDM['ModelParametersEstimation'],
                NIDM['ContrastMap']: NIDM_CONTRAST_ESTIMATION, 
                NIDM['StatisticMap']: NIDM_CONTRAST_ESTIMATION, 
                NIDM['ContrastStandardErrorMap']: NIDM_CONTRAST_ESTIMATION, 
    }

    derived_from = {
                NIDM['SignificantCluster']: NIDM['ExcursionSetMap'],
                NIDM['Peak']: NIDM['SignificantCluster'],                
    }

    if nidm_version == "020":
        # nidm namespaces were defined under incf.org (instead of purl)
        NIDM_INCF = Namespace('http://www.incf.org/ns/nidash/nidm#')
        SPM_INCF = Namespace('http://www.incf.org/ns/nidash/spm#')
        FSL_INCF = Namespace('http://www.incf.org/ns/nidash/fsl#')

        # The following classes were named differently in 0.2.0
        renaming =  [(NIDM['ExcursionSetMap'],NIDM_INCF['ExcursionSet']),
                     (NIDM['SearchSpaceMaskMap'],NIDM_INCF['SearchSpaceMap']),
                     (NIDM['SignificantCluster'],NIDM_INCF['Cluster']),
                     (NIDM['ErrorModel'],NIDM_INCF['NoiseModel']),
                     (NIDM_CONTRAST_ESTIMATION,NIDM_INCF['ContrastEstimation']),
                     (NIDM['ContrastMap'],NIDM_INCF['ContrastMap']),
                     (NIDM['Map'], NIDM_INCF['Map']),
                     (NIDM['Data'], NIDM_INCF['Data']),
                     (NIDM['DesignMatrix'], NIDM_INCF['DesignMatrix']),
                     (NIDM['ModelParametersEstimation'], NIDM_INCF['ModelParametersEstimation']),
                     (NIDM['GrandMeanMap'], NIDM_INCF['GrandMeanMap']),
                     (NIDM['ResidualMeanSquaresMap'], NIDM_INCF['ResidualMeanSquaresMap']),
                     (NIDM['MaskMap'], NIDM_INCF['MaskMap']),
                     (NIDM['ContrastWeights'], NIDM_INCF['ContrastWeights']),
                     (NIDM['StatisticMap'], NIDM_INCF['StatisticMap']),
                     (NIDM['ContrastStandardErrorMap'], NIDM_INCF['ContrastStandardErrorMap']),
                     (NIDM['Inference'], NIDM_INCF['Inference']),
                     (NIDM['HeightThreshold'], NIDM_INCF['HeightThreshold']),
                     (NIDM['ExtentThreshold'], NIDM_INCF['ExtentThreshold']),
                     (NIDM['Peak'], NIDM_INCF['Peak']),
                     (NIDM['ClusterLabelsMap'], NIDM_INCF['ClusterLabelsMap']),
                     (NIDM['Coordinate'], NIDM_INCF['Coordinate']),
                     (NIDM['ParameterEstimateMap'], NIDM_INCF['ParameterEstimateMap']),
                     (SPM['ReselsPerVoxelMap'], SPM_INCF['ReselsPerVoxelMap']),
                     (FSL['CenterOfGravity'], FSL_INCF['CenterOfGravity'])]

        # MaskMap was sometimes called CustomMaskMap (when isUserDefined=true)
        components["Parameters estimation"].append(NIDM_INCF['CustomMaskMap'])
        
        # The following classes were not represented in 0.2.0
        components["Inference"].remove(NIDM['ClusterDefinitionCriteria'])
        components["Inference"].remove(NIDM['PeakDefinitionCriteria'])
        components["Inference"].remove(NIDM['DisplayMaskMap'])
        components["Inference"].remove(NIDM['ConjunctionInference'])

        # SPM and FSL software were described using software-specific terms
        components["SPM-specific Concepts"].append(NIDM_INCF['SPM'])
        components["FSL-specific Concepts"].append(NIDM_INCF['FSL'])


        # Add manually used and wasDerivedFrom because these are not stored in the owl file
        used_by[NIDM_INCF['MaskMap']] = [NIDM_INCF['ContrastEstimation']]
        used_by[NIDM_INCF['CustomMaskMap']] = [NIDM_INCF['ModelParametersEstimation']]
    

        # In version 0.2.0 "ErrorModel" was called "NoiseModel"
        components, used_by, generated_by, derived_from = _replace_term_by(\
            renaming, components, used_by, generated_by, derived_from)

    owlspec = OwlSpecification(owl_file, import_files, "NIDM-Results", 
        components, used_by, generated_by, derived_from, prefix=str(NIDM))

    

    owlspec._header_footer(component="nidm-results")

    if not nidm_version == "dev":
        if nidm_version == "020":
            # Previous version
            owlspec.text = owlspec.text.replace("nidm-results_020.html", "nidm-results_010.html")
        owlspec.text = owlspec.text.replace("(under development)", nidm_original_version)
        owlspec.text = owlspec.text.replace("nidm-results_dev.html", "nidm-results_"+nidm_version+".html", 1)
        owlspec.text = owlspec.text.replace("img/", "img/nidm-results_"+nidm_version+"/")

    owlspec.write_specification(component="nidm-results", version=nidm_version)

def _replace_term_by(renaming, components, used_by, generated_by, derived_from):
    for original_term, renamed_term in renaming:
        generated_by = dict((k if k != original_term else renamed_term, \
                             v if v != original_term else renamed_term) \
                                for (k, v) in generated_by.items())
        derived_from = dict((k if k != original_term else renamed_term, \
                             v if v != original_term else renamed_term) \
                                for (k, v) in derived_from.items())

        used_by = dict((k if k != original_term else renamed_term, \
                        list(el if el != original_term else renamed_term for el in v)) \
                            for (k, v) in used_by.items())

        components = collections.OrderedDict((k if k != original_term else renamed_term, \
                        list(el if el != original_term else renamed_term for el in v)) \
                            for (k, v) in components.items())

    return list([components, used_by, generated_by, derived_from])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        nidm_version = sys.argv[1]
    else:
        nidm_version = 'dev'

    main(nidm_version)

