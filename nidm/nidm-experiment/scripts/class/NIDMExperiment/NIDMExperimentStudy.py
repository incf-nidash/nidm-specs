import rdflib as rdf
import os, sys
from Constants import *

from NIDMExperiment import NIDMExperimentCore


class NIDMExperimentStudy(NIDMExperimentCore):
    """Class for NIDM-Experimenent Study-Level Objects.

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
        return "NIDM-Experiment Study Class"

    #adds study activity to to graph and stores URI
    def addStudy(self, proj_id):
        """
        Add study activity to graph and associates with proj_id

        :param proj_id: URI of project to associate study
        :return: URI identifier of this study

        """
        #create unique ID
        self.uuid = self.getUUID()
        #add to graph
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, NIDM_STUDY))
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, self.namespaces["prov"]["Activity"]))
        self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces["dct"]["isPartOf"], proj_id))
        return self.namespaces["nidm"][self.uuid]