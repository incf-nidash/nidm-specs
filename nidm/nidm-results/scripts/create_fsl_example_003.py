"""
Create minimal FSL example for an analysis thresholded at p<0.05 FWE 
stored in nidm/nidm-results/fsl/example003 by using the class 
templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from create_example_from_templates import ExampleFromTemplate

def main():
	nidm_classes = {
		"HeightThreshold_PUnc": dict(
			height_threshold_id="niiri:height_threshold_id",
			label="Height Threshold: p<0.05 (uncorrected)",
			p_unc="0.050000",
			thresh_type="p-value uncorrected"
			),
		"FSL_ExtentThreshold_NoType": dict(
			extent_threshold_id="niiri:extent_threshold_id",
			label="Extent Threshold: k>=0",
			p_fwe="1.0"
			),
		"InferenceUsedThresh": dict(
			inference_id="niiri:inference_id",
			height_thresh_id="niiri:height_threshold_id", 
			extent_thresh_id="niiri:extent_threshold_id", 
			)
		}

	NIDM_FSL_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'fsl', 'example003')
	ttl_file = os.path.join(NIDM_FSL_DIR, 'fsl_nidm.ttl')
	example = ExampleFromTemplate(nidm_classes, ttl_file, False)
	example.create_example()
	
if __name__ == '__main__':
	main()