#!/usr/bin/env python
''' Automatically-generates NIDM-Experiment specification based on nidm-experiment.owl

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014

@author: Karl G. Helmer <helmer@nmr.mgh.harvard.edu>
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

    subcomponents["Project"] = [NIDM['CoInvestigator'],
        NIDM['Group'],NIDM['Model'], NIDM['ModelDesigner'],
        NIDM['ModelSpecification'],NIDM['OrganismType'],
        NIDM['PrincipalInvestigator'], NIDM['Project'],
        NIDM['Protocol'], NIDM['ResearchAssistant'], 
        NIDM['SpecifiedPlan'], NIDM['Subject']]
    subcomponents["Acquisition"] = [NIDM['AcquisitionMethod'],NIDM['AcquisitionModality'],
        NIDM['AcquisitionObject'], NIDM['AcquisitionObjectQuality'], NIDM['AssessmentInstrumentAdministrator'],
        NIDM['AuxiliaryFile'], NIDM['AuxiliaryFileCollection'],  
        NIDM['BehavioralDataAcquisition'],NIDM['ClinicalAssessmentAcquisitionObject'], NIDM['Computer'],
        NIDM['DICOMTagCollection'],NIDM['DataAcquisitionDeviceOperator'], NIDM['DemographicsDataAcquisition'],
        NIDM['DemographicsInstrumentAdministrator'], NIDM['ImageContrastType'], NIDM['ImageDataReconstruction'],
        NIDM['ImageUsageType'], NIDM['InformedConsentAcquisition'], NIDM['InformedConsentAdministrator'],
        NIDM['PerformedPlan'], NIDM['PresentationSoftware'],  NIDM['PulseSequence'],
        NIDM['RawAcquisitionObject'],NIDM['ReconstructedAcquisitionObject'], NIDM['Session'],
        NIDM['SessionObject'] ]
    subcomponents["Modality"] = [NIDM['Amperometry'], NIDM['Anatomical'],
        NIDM['Cartesian'],NIDM['ComputedTomography'], NIDM['CurrentClamp'],
        NIDM['DiffusionTensor'],NIDM['DiffusionWeighted'],
        NIDM['DynamicContrastEnhancement'], NIDM['DynamicSusceptibilityContrast'],
        NIDM['EchoPlanar'], NIDM['Electrocorticography'], NIDM['Electroencephalography'],
        NIDM['ExtracellularElectrophysiologyRecording'], 
        NIDM['FieldPotential'],NIDM['FingerTappingTest'], NIDM['FlowWeighted'],
        NIDM['Functional'],NIDM['Inside-outSpiral'], NIDM['IntracellularElectrophysiologyRecording'],
        NIDM['MagneticResonanceImaging'], NIDM['MultiUnitReccording'],
        NIDM['NuclearMagneticResonanceSpectroscopy'], NIDM['Outside-inSpiral'],
        NIDM['ParallelImagingMethod'], NIDM['PatchClamp'],  NIDM['PositronEmissionTomography'],
        NIDM['ProtonDensityWeighted'],NIDM['Rectilinear'], NIDM['Session'],
        NIDM['SharpElectrode'],NIDM['SimultaneousMultisliceMethod'], NIDM['SingleUnitReccording'],
        NIDM['StimulusPresentationFile'], NIDM['StimulusResponseFile'], NIDM['Structural'], 
        NIDM['SusceptibilityWeighted'], NIDM['SusceptibilityWeightedImaging'], NIDM['Task'],
        NIDM['T1Weighted'], NIDM['T2StarWeighted'],  
        NIDM['T2Weighted'],NIDM['VoltageClamp'], NIDM['bValueFile'],
        NIDM['bVectorFile'],NIDM['k-spaceTraversalScheme'] ]
    subcomponents["Assessments"] = [NIDM['BarnesScale'], NIDM['CalgaryDepressionScale'],
        NIDM['CategoryFluencyTest'],NIDM['ClinicalGlobalImpression'], NIDM['CombinedAssessment'],
        NIDM['ContinuousPerformanceTest'],NIDM['DelayedSemanticVerbalLearningTest'],
        NIDM['DelayedVisualFiguralLearningTest'], NIDM['EdinburghHandnessTest'],
        NIDM['FacialEmotionDiscriminationTest'], NIDM['FagerstromSmokingTest'], NIDM['LetterFluencyTest'],
        NIDM['LetterNumberSpanTest'], NIDM['MazeSolvingTest'], NIDM['NorthAmericanAdultReadingTest'], 
        NIDM['PositiveAndNegativeSyndromeScale'],NIDM['PremorbidAdjustment'], NIDM['SemanticVerbalLearningTest'],
        NIDM['SimpsonAngusRatingScale'],NIDM['SocioeconomicScale'], NIDM['SpatialMemorySpan'], 
        NIDM['StroopTest'], NIDM['SymbolDigitAssociationTest'], NIDM['TrailsA'], NIDM['TrailsB'], 
        NIDM['VisualFiguralLearningTest'], NIDM['WisconsinCardSortingTest'] ]
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
