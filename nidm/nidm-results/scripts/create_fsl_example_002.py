"""
Create minimal FSL example for an analysis thresholded at p<0.05 FWE
stored in nidm/nidm-results/fsl/example002 by using the class
templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
import sys
from create_example_from_templates import ExampleFromTemplate

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from Constants import OBO_P_VALUE_FWER_QNAME, OBO_STATISTIC_QNAME


def main():
    nidm_classes = {
        "HeightThreshold": dict(
            height_threshold_id="niiri:height_threshold_id",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            label="Height Threshold: p<0.05 (FWE)",
            value="0.050000",
            ),
        "ExtentThresholdStat": dict(
            extent_threshold_id="niiri:extent_threshold_id",
            label="Extent Threshold: k>=0",
            thresh_type=OBO_STATISTIC_QNAME,
            cluster_size_vox="0",
            ),
        "InferenceUsedThresh": dict(
            inference_id="niiri:inference_id",
            height_thresh_id="niiri:height_threshold_id",
            extent_thresh_id="niiri:extent_threshold_id",
            )
        }

    NIDM_FSL_DIR = os.path.join(os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))), 'test', 'ground_truth',
        'voxelwise_p050_fwe')
    ttl_file = os.path.join(NIDM_FSL_DIR, 'nidm.ttl')
    example = ExampleFromTemplate(nidm_classes, ttl_file, False)
    example.create_example()

if __name__ == '__main__':
    main()
