"""
Create SPM example 004 stored in nidm/nidm-results/spm/example004 by using the 
class templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from create_example_from_templates import ExampleFromTemplate

def main():
	nidm_classes = {
		"Inference": dict(
			inference_id="niiri:inference_id_1",
			label="Inference",
			alternative_hyp="nidm:OneTailedTest",
			stat_map_id="niiri:statistic_map_id", 
			height_thresh_id="niiri:height_threshold_id", 
			extent_thresh_id="niiri:extent_threshold_id", 
			display_mask_id="niiri:display_map_id", 
			peak_def_id="niiri:peak_definition_criteria_id", 
			cluster_def_id="niiri:cluster_definition_criteria_id",
			mask_id="niiri:mask_id_1",
			software_id="niiri:software_id"
			),
		"ConjunctionInference": dict(
			conj_inference_id="niiri:conjunction_id_1",
			label="Conjunction Inference",
			alternative_hyp="nidm:OneTailedTest",
			stat_map_id_1="niiri:statistic_map_id_1", 
			stat_map_id_2="niiri:statistic_map_id_2", 
			height_thresh_id="niiri:height_threshold_id", 
			extent_thresh_id="niiri:extent_threshold_id", 
			display_mask_id="niiri:display_map_id", 
			peak_def_id="niiri:peak_definition_criteria_id", 
			cluster_def_id="niiri:cluster_definition_criteria_id",
			mask_id="niiri:mask_id_1",
			software_id="niiri:software_id"
			),
		"SPM_KConjunctionInference": dict(
			conj_inference_id="niiri:conjunction_id_2",
			label="k-Conjunction Inference",
			alternative_hyp="nidm:OneTailedTest",
			stat_map_id_1="niiri:statistic_map_id_1", 
			stat_map_id_2="niiri:statistic_map_id_2", 
			global_null_degree="1",
			height_thresh_id="niiri:height_threshold_id", 
			extent_thresh_id="niiri:extent_threshold_id", 
			display_mask_id="niiri:display_map_id", 
			peak_def_id="niiri:peak_definition_criteria_id", 
			cluster_def_id="niiri:cluster_definition_criteria_id",
			mask_id="niiri:mask_id_1",
			software_id="niiri:software_id"
			),
		}

	NIDM_SPM_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'spm', "example004")
	ttl_file = os.path.join(NIDM_SPM_DIR, 'spm_inference_activities.ttl')
	example = ExampleFromTemplate(nidm_classes, ttl_file, False)
	example.create_example()
