"""
Create minimal SPM example for an analysis using an F-test
stored in nidm/nidm-results/spm/example006 by using the class
templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2015
"""
import os
import sys
from create_example_from_templates import ExampleFromTemplate

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from Constants import q_graph, NIDM_CONTRAST_ESTIMATION, \
    NIDM_EVENT_RELATED_DESIGN, NIDM_MODEL_PARAMETERS_ESTIMATION, \
    NIDM_REGRESSOR_NAMES, NIDM_HAS_HRF_BASIS, NIDM_HAS_DRIFT_MODEL, PROV, NFO,\
    CRYPTO, DC, NIDM_IN_COORDINATE_SPACE


def f_test():
    nidm_classes = {
        "ContrastExplainedMeanSquareMap": dict(
            id="niiri:contrast_explained_mean_square_map_id",
            label="Contrast Explained Mean Square Map",
            location="ContrastExplainedMeanSquareMap_F001.nii.gz",
            filename="ContrastExplainedMeanSquareMap_F001.nii.gz",
            format="image/nifti",
            coordinate_space_id="",
            sha="",
            contrast_est_id="niiri:contrast_estimation_id",
            ),
        "EntityWasGeneratedByActivity": dict(
            activity_id="niiri:contrast_estimation_id",
            activity_type=q_graph.qname(NIDM_CONTRAST_ESTIMATION),
            entity_id="niiri:contrast_explained_mean_square_map_id",
            )
        }

    MIN_EX_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'test',
        'minimal_examples', 'f_test')
    ttl_file = os.path.join(MIN_EX_DIR, 'nidm.ttl')
    example = ExampleFromTemplate(nidm_classes, ttl_file, False,
                                  remove_att=[
                                      NIDM_IN_COORDINATE_SPACE,
                                      PROV.atLocation, CRYPTO.sha512])
    example.create_example()


def design_matrix_event_related():
    nidm_classes = {
        "DesignMatrix_1stLevel": dict(
            design_matrix_id='niiri:design_matrix_id',
            label="Design Matrix",
            location="DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id",
            regressors="",
            hrf_basis="",
            drift_model=""),
        "ActivityUsedEntity": dict(
            activity_id="niiri:model_parameter_estimation_id",
            activity_type=q_graph.qname(NIDM_MODEL_PARAMETERS_ESTIMATION),
            entity_id="niiri:design_matrix_id",
            )
        }

    MIN_EX_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'test',
        'minimal_examples', 'event_related_design')
    ttl_file = os.path.join(MIN_EX_DIR, 'nidm.ttl')
    example = ExampleFromTemplate(
        nidm_classes, ttl_file, False,
        remove_att=[NIDM_REGRESSOR_NAMES, NIDM_HAS_HRF_BASIS,
                    NIDM_HAS_DRIFT_MODEL])
    example.create_example()


def explicit_mask():
    nidm_classes = {
        "MaskMap": dict(
            mask_id="niiri:explicit_mask_id",
            label="Mask Map",
            location="",
            filename="",
            user_defined="true",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="",
            used_by_act_id="niiri:model_parameter_estimation_id"
            ),
        "ActivityUsedEntity": dict(
            activity_id="niiri:model_parameter_estimation_id",
            activity_type=q_graph.qname(NIDM_MODEL_PARAMETERS_ESTIMATION),
            entity_id="niiri:explicit_mask_id",
            )
        }

    MIN_EX_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'test',
        'minimal_examples', 'explicit_mask')
    ttl_file = os.path.join(MIN_EX_DIR, 'nidm.ttl')
    example = ExampleFromTemplate(
        nidm_classes, ttl_file, False, remove_att=[
            NIDM_IN_COORDINATE_SPACE,
            PROV.atLocation, NFO.fileName, CRYPTO.sha512, DC.description])
    example.create_example()


def main():
    f_test()
    design_matrix_event_related()
    explicit_mask()

if __name__ == '__main__':
    main()
