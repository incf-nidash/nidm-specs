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
        import_files = glob.glob(os.path.join(NIDM_EXPE_PATH, "imports", '*.ttl'))
    else:
        owl_file = os.path.join(RELEASED_TERMS_FOLDER, \
            'nidm-experiment_'+nidm_version+'.owl')
        # For released version of the ontology imports are embedded
        import_files = None

    # check the file exists
    assert os.path.exists(owl_file)

    subcomponents =  collections.OrderedDict()

    subcomponents['Project'] = [
        NIDM['CoInvestigator'], NIDM['Group'], NIDM['ModelDesigner'], NIDM['ModelSpecification'],
        NIDM['PrincipalInvestigator'], NIDM['Project'], NIDM['Protocol'], NIDM['ResearchAssistant'], 
        NIDM['SpecifiedPlan'], NIDM['Subject']
        ]
    subcomponents['Acquisition'] = [
        NIDM['AcquisitionMethod'],NIDM['AcquisitionModality'],
        NIDM['AcquisitionObject'], NIDM['AcquisitionObjectQuality'], NIDM['AssessmentInstrumentAdministrator'],
        NIDM['AuxiliaryFile'], NIDM['AuxiliaryFileCollection'],  
        NIDM['BehavioralDataAcquisition'],NIDM['ClinicalAssessmentAcquisitionObject'], 
        NIDM['AcquisitionDeviceOperator'], NIDM['DemographicsDataAcquisition'],
        NIDM['DemographicsInstrumentAdministrator'], NIDM['ImageContrastType'], NIDM['ImageDataReconstruction'],
        NIDM['ImageUsageType'], NIDM['InformedConsentAcquisition'], NIDM['InformedConsentInstrumentAdministrator'],
        NIDM['PerformedPlan'], NIDM['PresentationSoftware'],  NIDM['PulseSequence'],
        NIDM['RawAcquisitionObject'],NIDM['ReconstructedAcquisitionObject'], NIDM['Session'],
        NIDM['SessionObject']
        ]
    subcomponents['Magnetic Resonance Imaging'] = [
        NIDM['Anatomical'], NIDM['Cartesian'], 
        NIDM['DICOMTagCollection'], NIDM['DiffusionTensor'],NIDM['DiffusionWeighted'], 
        NIDM['DynamicContrastEnhanced'], NIDM['DynamicSusceptibilityContrast'],
        NIDM['EchoPlanar'], NIDM['FlowWeighted'],
        NIDM['Functional'],NIDM['Inside-outSpiral'], NIDM['MagneticResonanceImaging'],
        NIDM['NuclearMagneticResonanceSpectroscopy'], NIDM['Outside-inSpiral'], NIDM['ParallelImaging'], 
        NIDM['ProtonDensityWeighted'],NIDM['Rectilinear'], NIDM['Session'],NIDM['SimultaneousMultisliceMethod'], 
        NIDM['StimulusPresentationFile'], NIDM['StimulusResponseFile'], NIDM['Structural'], 
        NIDM['SusceptibilityWeighted'], NIDM['SusceptibilityWeightedImaging'], NIDM['Task'],
        NIDM['T1Weighted'], NIDM['T2StarWeighted'], NIDM['T2Weighted'],  NIDM['b-ValueFile'],
        NIDM['b-VectorFile'], NIDM['k-spaceTraversalScheme'], NIDM['NIDM_0000152'], NIDM['NIDM_0000153'],
        NIDM['NIDM_0000154'], NIDM['NIDM_0000155']
        ]
    subcomponents['Electrophysiology'] = [
        NIDM['Amperometry'], NIDM['CurrentClamp'], 
        NIDM['Electroencephalography'], NIDM['ExtracellularElectrophysiologyRecording'],  NIDM['Electrocorticography'],
        NIDM['FieldPotential'], NIDM['IntracellularElectrophysiologyRecording'], 
        NIDM['MultiUnitReccording'],  NIDM['SharpElectrode'], NIDM['SingleUnitReccording'], 
        NIDM['PatchClamp'], NIDM['VoltageClamp']
        ]
    subcomponents['Positron Emission Tomography'] = [NIDM['PositronEmissionTomography']]
    subcomponents['X-ray Computed Tomography'] = [NIDM['X-rayComputedTomography']]
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
