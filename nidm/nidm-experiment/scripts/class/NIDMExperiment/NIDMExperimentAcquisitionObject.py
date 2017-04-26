import rdflib as rdf
import os, sys
from Constants import *

from NIDMExperiment import NIDMExperimentCore


class NIDMExperimentAcquisitionObject(NIDMExperimentCore):
    """Class for NIDM-Experimenent AcquisitionObject-Level Objects.

    Default constructor uses empty graph with namespaces added from NIDM/Scripts/Constants.py.
    Additional alternate constructors for user-supplied graphs and default namespaces (i.e. from Constants.py)
    and user-supplied graph and namespaces

    @author: David Keator <dbkeator@uci.edu>
    @copyright: University of California, Irvine 2017

    """
    #constructor
    def __init__(self):
        #execute default parent class constructor
        NIDMExperimentCore.__init__(self)

    #constructor with user-supplied graph, namespaces come from base class import of Constants.py
    #note this sets the graph in the base class
    @classmethod
    def withGraph(self, graph):
        #execute default parent class constructor
        NIDMExperimentCore.withGraph(self, graph)

    #constructor with user-supplied graph and namespaces
    #note this sets the graph in the base class
    @classmethod
    def withGraphAndNamespaces(self, graph, namespaces):
        #sets up empty dictionary to map object URIs to experiment names
        self.inv_object_dict={}
        #execute default parent class constructor
        NIDMExperimentCore.withGraphAndNamespaces(self, graph, namespaces)


    def __str__(self):
        return "NIDM-Experiment AcquisitionObject Class"

     #adds acquisition entity to to graph and stores URI
    def addAcquisitionObject(self, study_id):
        """
        Add acquisition object entity to graph and associates with study_id

        :param study_id: URI of study to associate acquisition objct
        :return: URI identifier of this study

        """
        #create unique ID
        self.uuid = self.getUUID()
        #add to graph
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, NIDM_ACQUISITION_OBJECT))
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, self.namespaces["prov"]["Entity"]))
        self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces["prov"]["wasGeneratedBy"], study_id))
        return self.namespaces["nidm"][self.uuid]

    def addParticipant(self,identifier, acq_obj):
        """
        Add prov:Person with role of Participant, use addLiteralAttribute to add more descriptive attributes
        :param identifier: identifier of participant
        :param acq_obj: URI of acquisition object to associate participant
        :return: URI identifier of this subject
        """
        person = self.addPerson();
        self.addLiteralAttribute(person,"ncit","subjectID", identifier)
        self.addURIRef(person,"prov","hadRole", NIDM_PARTICIPANT)
        return person
    def associateParticipantWithAcquisitionObj(self,acq_obj,participant_obj):
        """
        Add prov:Person with role of Participant, use addLiteralAttribute to add more descriptive attributes
        :param acq_obj: URI of acquisition object
        :param participant_obj: URI of participant object
        """
        self.graph.add((acq_obj, self.namespaces["prov"]["wasAttributedTo"], participant_obj))
