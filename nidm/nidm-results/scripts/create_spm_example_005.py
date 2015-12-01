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
			location="DisplayMask.nii.gz",
			user_defined="true",
			filename="DisplayMask.nii.gz",
			format="image/nifti",
			coordinate_space_id="niiri:coordinate_space_id_1",
			sha="e43b6e01b0463fe7d40782137867a"
			),
		"CoordinateSpace-1": dict(
			coordinate_space_id="niiri:coordinate_space_id_1",
			label="Coordinate space 1",
			voxel_to_world_mapping="[[-3, 0, 0, 78],[0, 3, 0, -112],[0, 0, 3, -70],[0, 0, 0, 1]]",
			voxel_units="[ \\\"mm\\\", \\\"mm\\\", \\\"mm\\\" ]",
			voxel_size="[ 3, 3, 3 ]",
			coord_system="nidm:NIDM_0000051",
			number_of_dim="3",
			dimensions="[ 53, 63, 52 ]"),
		"ActivityUsedEntity": dict(
			activity_id="niiri:display_map_id",
			activity_type="nidm:NIDM_0000049",
			entity_id="niiri:height_threshold_id", 
			)
		}

	NIDM_SPM_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'spm', 'example005')
	ttl_file = os.path.join(NIDM_SPM_DIR, 'nidm.ttl')
	example = ExampleFromTemplate(nidm_classes, ttl_file, False)
	example.create_example()
	
if __name__ == '__main__':
	main()