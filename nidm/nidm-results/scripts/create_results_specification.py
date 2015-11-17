#!/usr/bin/env python
''' Automatically-generates NIDM-Results specification based on
nidm-results.owl

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
        owl_file = os.path.join(RELEASED_TERMS_FOLDER,
                                'nidm-results_' + nidm_version + '.owl')
        # For released version of the ontology imports are embedded
        import_files = None

    # check the file exists
    assert os.path.exists(owl_file)

    components = collections.OrderedDict()
    components["General"] = [NIDM_RESULTS, NIDM_MAP, NIDM_COORDINATE_SPACE,
                             SPM_SOFTWARE, FSL_SOFTWARE]
    components["Parameters estimation"] = [
        NIDM_MODEL_PARAMETERS_ESTIMATION,
        NIDM_DATA, NIDM_DESIGN_MATRIX, NIDM_ERROR_MODEL,
        NIDM_GRAND_MEAN_MAP, NIDM_MASK_MAP, NIDM_PARAMETER_ESTIMATE_MAP,
        NIDM_RESELS_PER_VOXEL_MAP, NIDM_RESIDUAL_MEAN_SQUARES_MAP]
    components["Contrast estimation"] = [
        NIDM_CONTRAST_ESTIMATION,
        STATO_CONTRAST_WEIGHT_MATRIX, NIDM_CONTRAST_MAP,
        NIDM_CONTRAST_STANDARD_ERROR_MAP,
        NIDM_CONTRAST_EXPLAINED_MEAN_SQUARE_MAP, NIDM_STATISTIC_MAP]
    components["Inference"] = [
        NIDM_INFERENCE,
        NIDM_CLUSTER_DEFINITION_CRITERIA, NIDM_CLUSTER_LABELS_MAP,
        NIDM_COORDINATE, NIDM_DISPLAY_MASK_MAP,
        NIDM_EXCURSION_SET_MAP, NIDM_EXTENT_THRESHOLD,
        NIDM_HEIGHT_THRESHOLD, NIDM_PEAK,
        NIDM_PEAK_DEFINITION_CRITERIA, NIDM_SEARCH_SPACE_MASK_MAP,
        NIDM_SUPRA_THRESHOLD_CLUSTER]

    if nidm_version == 'dev':
        # For the developement version only list all terms that were not
        # referred to in other components
        components["Other"] = []

    # Add manually used and wasDerivedFrom because these are not stored in the
    # owl file
    used_by = {
        NIDM_DATA: [NIDM_MODEL_PARAMETERS_ESTIMATION],
        NIDM_ERROR_MODEL: [NIDM_MODEL_PARAMETERS_ESTIMATION],
        NIDM_DESIGN_MATRIX: [NIDM_MODEL_PARAMETERS_ESTIMATION,
                             NIDM_CONTRAST_ESTIMATION],
        NIDM_PARAMETER_ESTIMATE_MAP: [NIDM_CONTRAST_ESTIMATION],
        NIDM_RESIDUAL_MEAN_SQUARES_MAP: [NIDM_CONTRAST_ESTIMATION],
        NIDM_MASK_MAP: [NIDM_CONTRAST_ESTIMATION,
                        NIDM_MODEL_PARAMETERS_ESTIMATION],
        STATO_CONTRAST_WEIGHT_MATRIX: [NIDM_CONTRAST_ESTIMATION],
        NIDM_CONTRAST_MAP: [NIDM_INFERENCE],
        NIDM_STATISTIC_MAP: [NIDM_INFERENCE],
        NIDM_CLUSTER_DEFINITION_CRITERIA: [NIDM_INFERENCE],
        NIDM_DISPLAY_MASK_MAP: [NIDM_INFERENCE],
        NIDM_PEAK_DEFINITION_CRITERIA: [NIDM_INFERENCE],
        NIDM_RESELS_PER_VOXEL_MAP: [NIDM_INFERENCE]
    }
    generated_by = {
        NIDM_PARAMETER_ESTIMATE_MAP: NIDM_MODEL_PARAMETERS_ESTIMATION,
        NIDM_RESIDUAL_MEAN_SQUARES_MAP: NIDM_MODEL_PARAMETERS_ESTIMATION,
        NIDM_RESELS_PER_VOXEL_MAP: NIDM_MODEL_PARAMETERS_ESTIMATION,
        NIDM_MASK_MAP: NIDM_MODEL_PARAMETERS_ESTIMATION,
        NIDM_CONTRAST_MAP: NIDM_CONTRAST_ESTIMATION,
        NIDM_STATISTIC_MAP: NIDM_CONTRAST_ESTIMATION,
        NIDM_CONTRAST_EXPLAINED_MEAN_SQUARE_MAP: NIDM_CONTRAST_ESTIMATION,
        NIDM_CONTRAST_STANDARD_ERROR_MAP: NIDM_CONTRAST_ESTIMATION,
        NIDM_GRAND_MEAN_MAP: NIDM_MODEL_PARAMETERS_ESTIMATION,
    }

    derived_from = {
        NIDM_SUPRA_THRESHOLD_CLUSTER: NIDM_EXCURSION_SET_MAP,
        NIDM_PEAK: NIDM_SUPRA_THRESHOLD_CLUSTER,
        NIDM_CLUSTER_CENTER_OF_GRAVITY: NIDM_SUPRA_THRESHOLD_CLUSTER
    }

    if nidm_version == "020":
        # nidm namespaces were defined under incf.org (instead of purl)
        NIDM_INCF = Namespace('http://www.incf.org/ns/nidash/nidm#')
        SPM_INCF = Namespace('http://www.incf.org/ns/nidash/spm#')
        FSL_INCF = Namespace('http://www.incf.org/ns/nidash/fsl#')

        # The following classes were named differently in 0.2.0
        renaming = [(NIDM_EXCURSION_SET_MAP, NIDM_INCF['ExcursionSet']),
                    (NIDM_SEARCH_SPACE_MASK_MAP, NIDM_INCF['SearchSpaceMap']),
                    (NIDM_SUPRA_THRESHOLD_CLUSTER, NIDM_INCF['Cluster']),
                    (NIDM_ERROR_MODEL, NIDM_INCF['NoiseModel']),
                    (NIDM_CONTRAST_ESTIMATION,
                     NIDM_INCF['ContrastEstimation']),
                    (NIDM_CONTRAST_MAP, NIDM_INCF['ContrastMap']),
                    (NIDM_MAP, NIDM_INCF['Map']),
                    (NIDM_DATA, NIDM_INCF['Data']),
                    (NIDM_DESIGN_MATRIX, NIDM_INCF['DesignMatrix']),
                    (NIDM_MODEL_PARAMETERS_ESTIMATION,
                     NIDM_INCF['ModelParametersEstimation']),
                    (NIDM_GRAND_MEAN_MAP, NIDM_INCF['GrandMeanMap']),
                    (NIDM_RESIDUAL_MEAN_SQUARES_MAP,
                     NIDM_INCF['ResidualMeanSquaresMap']),
                    (NIDM_MASK_MAP, NIDM_INCF['MaskMap']),
                    (STATO_CONTRAST_WEIGHT_MATRIX,
                     NIDM_INCF['ContrastWeights']),
                    (NIDM_STATISTIC_MAP, NIDM_INCF['StatisticMap']),
                    (NIDM_CONTRAST_STANDARD_ERROR_MAP,
                     NIDM_INCF['ContrastStandardErrorMap']),
                    (NIDM_INFERENCE, NIDM_INCF['Inference']),
                    (NIDM_HEIGHT_THRESHOLD, NIDM_INCF['HeightThreshold']),
                    (NIDM_EXTENT_THRESHOLD, NIDM_INCF['ExtentThreshold']),
                    (NIDM_PEAK, NIDM_INCF['Peak']),
                    (NIDM_CLUSTER_LABELS_MAP, NIDM_INCF['ClusterLabelsMap']),
                    (NIDM_COORDINATE, NIDM_INCF['Coordinate']),
                    (NIDM_PARAMETER_ESTIMATE_MAP,
                     NIDM_INCF['ParameterEstimateMap']),
                    (NIDM_RESELS_PER_VOXEL_MAP,
                     SPM_INCF['ReselsPerVoxelMap']),
                    (NIDM_CLUSTER_CENTER_OF_GRAVITY,
                        FSL_INCF['CenterOfGravity'])]

        # MaskMap was sometimes called CustomMaskMap (when isUserDefined=true)
        components["Parameters estimation"].append(NIDM_INCF['CustomMaskMap'])

        # The following classes were not represented in 0.2.0
        components["Inference"].remove(NIDM_CLUSTER_DEFINITION_CRITERIA)
        components["Inference"].remove(NIDM_PEAK_DEFINITION_CRITERIA)
        components["Inference"].remove(NIDM_DISPLAY_MASK_MAP)
        components["Inference"].remove(NIDM_CONJUNCTION_INFERENCE)

        # The following classes were represented in another component in 0.2.0
        components["Parameters estimation"].remove(NIDM_RESELS_PER_VOXEL_MAP)

        del used_by[NIDM_CLUSTER_DEFINITION_CRITERIA]
        del used_by[NIDM_PEAK_DEFINITION_CRITERIA]
        del used_by[NIDM_DISPLAY_MASK_MAP]

        # SPM and FSL software were described using software-specific terms
        components["SPM-specific Concepts"] = [
            NIDM_INCF['SPM'], SPM_INCF['ReselsPerVoxelMap']]
        components["FSL-specific Concepts"] = [
            NIDM_INCF['FSL'], FSL_INCF['CenterOfGravity']]

        # Add manually used and wasDerivedFrom because these are not stored in
        # the owl file
        used_by[NIDM_INCF['CustomMaskMap']] = [
            NIDM_INCF['ModelParametersEstimation']]
        used_by[NIDM_MASK_MAP] = [NIDM_CONTRAST_ESTIMATION]

        # In version 0.2.0 "ErrorModel" was called "NoiseModel"
        components, used_by, generated_by, derived_from = _replace_term_by(
            renaming, components, used_by, generated_by, derived_from)

    commentable = False
    if nidm_version == "dev":
        commentable = True

    intro = ""
    if nidm_version == "dev":
        intro = """
                <p>This section introduces neuroimaging results concepts with \
definitions and illustrative examples.</p>
            """

    owlspec = OwlSpecification(
        owl_file, import_files, "NIDM-Results",
        components, used_by, generated_by, derived_from, prefix=str(NIDM),
        commentable=commentable, intro=intro)

    owlspec._header_footer(component="nidm-results", version=nidm_version)

    if not nidm_version == "dev":
        if nidm_version == "110":
            # Previous version
            owlspec.text = owlspec.text.replace(
                "nidm-results_020.html", "nidm-results_100.html")
        elif nidm_version == "020":
            # Previous version
            owlspec.text = owlspec.text.replace(
                "nidm-results_020.html", "nidm-results_010.html")
        owlspec.text = dev_to_release(owlspec.text, nidm_original_version)

    owlspec.write_specification(component="nidm-results", version=nidm_version)


def dev_to_release(text, full_version):
    version = full_version.replace(".", "")
    text = text.replace(
        "(under development)", full_version)
    text = text.replace(
        "nidm-results_dev.html",
        "nidm-results_" + version + ".html", 1)
    text = text.replace(
        "img/", "img/nidm-results_" + version + "/")
    return text


def _replace_term_by(renaming, components, used_by, generated_by,
                     derived_from):
    for original_term, renamed_term in renaming:
        generated_by = dict((k if k != original_term else renamed_term,
                             v if v != original_term else renamed_term)
                            for (k, v) in generated_by.items())
        derived_from = dict((k if k != original_term else renamed_term,
                             v if v != original_term else renamed_term)
                            for (k, v) in derived_from.items())

        used_by = dict(
            (k if k != original_term else renamed_term,
             list(el if el != original_term else renamed_term for el in v))
            for (k, v) in used_by.items())

        components = collections.OrderedDict(
            (k if k != original_term else renamed_term,
             list(el if el != original_term else renamed_term for el in v))
            for (k, v) in components.items())

    return list([components, used_by, generated_by, derived_from])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        nidm_version = sys.argv[1]
    else:
        nidm_version = 'dev'

    main(nidm_version)
