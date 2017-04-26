#!/usr/bin/env python

import sys, getopt, os

sys.path.insert(0, os.path.abspath('NIDMExperiment'))
from NIDMExperiment import *
import json
from pprint import pprint
import csv
from argparse import ArgumentParser

def main(argv):
    parser = ArgumentParser()

    parser.add_argument('-d', dest='directory', required=True, help="Path to BIDS dataset directory")
    parser.add_argument('-o', dest='outputfile', default="nidm.ttl", help="NIDM output turtle file")
    args = parser.parse_args()

    directory = args.directory
    outputfile = args.outputfile

    #create empty NIDM-Exp document
    nidm_doc = NIDMExperimentProject()
    #Parse dataset_description.json file in BIDS directory
    with open(directory+'/'+'dataset_description.json') as data_file:
        dataset_data = json.load(data_file)
    #pprint(dataset_data)
    proj = nidm_doc.addProject(dataset_data['Name'],dataset_data['BIDSVersion'],dataset_data['Procedure'])
    nidm_doc.addListAttribute(proj,"dcat","accessURL",dataset_data['ReferencesAndLinks'])
    nidm_doc.addLiteralAttribute(proj,"dcat","license", dataset_data['License'])
    nidm_doc.addListAttribute(proj,"ncit","Author",dataset_data['Authors'])

    #create session object
    study = NIDMExperimentSession()
    study_obj = study.addSession(proj)


    #Parse participants.tsv file in BIDS directory and create study and acquisition objects
    with open(directory+'/'+'participants.tsv') as csvfile:
        participants_data = csv.DictReader(csvfile, delimiter='\t')
        print(participants_data.fieldnames)
        for row in participants_data:
            #for now we're not worrying about all variables in participants.tsv file.  just go with ID, diagnosis, age, and gender
            #add acquisition object
            acq = NIDMExperimentAcquisitionObject()
            acq_obj = acq.addAcquisitionObject(study_obj)
            participant = acq.addParticipant(row['participant_id'], acq_obj)
            acq.associateParticipantWithAcquisitionObj(acq_obj,participant)
            acq.addLiteralAttribute(acq_obj,"ncit","age",int(row['age']))
            acq.addLiteralAttribute(acq_obj,"ncit","gender",row['gender'])
            acq.addLiteralAttribute(acq_obj,"ncit","diagnosis",row['diagnosis'])


            #print(row['participant_id'], row['diagnosis'], row['age'], row['gender'])

    with open(outputfile,'w') as f:
        f.write(nidm_doc.serializeTurtle())
    print(nidm_doc.serializeTurtle())
if __name__ == "__main__":
   main(sys.argv[1:])

