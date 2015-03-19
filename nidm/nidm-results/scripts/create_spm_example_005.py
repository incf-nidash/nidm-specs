"""
Create minimal SPM example for an analysis using "contrast masking"
stored in nidm/nidm-results/spm/example005 by using the class 
templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2015
"""
import os
from create_example_from_templates import ExampleFromTemplate

def main():
	nidm_classes = {
		"DisplayMaskMap": dict(
			display_map_id="niiri:display_map_id",
			label="Display Mask Map",
			location="file://./DisplayMask.nii.gz",
			filename="DisplayMask.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a..."
			),
		"Inference_Used_DisplayMask": dict(
			inference_id="niiri:display_map_id",
			display_mask_id="niiri:height_threshold_id", 
			)
		}

	NIDM_SPM_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'spm', 'example005')
	ttl_file = os.path.join(NIDM_SPM_DIR, 'nidm.ttl')
	example = ExampleFromTemplate(nidm_classes, ttl_file, False)
	example.create_example()
	
if __name__ == '__main__':
	main()