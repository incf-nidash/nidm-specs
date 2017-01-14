import rdflib as rdf
import os, sys

from NIDMExperiment import NIDMExperimentCore


class NIDMExperimentInvestigation(NIDMExperimentCore):
    """Class for NIDM-Experimenent Investigation-Level Objects.

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
        return "NIDM-Experiment Investigation Class"

    #adds and investigation entity to graph and stores URI
    def addInvestigation(self, inv_name, inv_id, inv_description):
        """
        Add investigation entity to graph

        :param inv_name: string, name of investigation/project
        :param inv_id: string, identifier of investigation/project
        :param inv_description: string, description of investigation
        :return: URI identifier of this subject

        """
        #create unique ID
        self.uuid = self.getUUID()
        #add to graph
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, self.namespaces["dctypes"]["Dataset"]))
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, self.namespaces["nidm"]["Investigation"]))
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, self.namespaces["prov"]["Entity"]))
        self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces["ncit"]["Identifier"], rdf.Literal(inv_id)))
        self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces["dct"]["title"], rdf.Literal(inv_name, datatype=rdf.XSD.String)))
        self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces["dct"]["description"], rdf.Literal(inv_description, lang=self.language)))
        return self.namespaces["nidm"][self.uuid]

    def addInvestigationPI(self,inv_id,family_name, given_name):
        """
        Add prov:Person with role of PI, use addLiteralAttribute to add more descriptive attributes
        :param inv_id: investigation URI to associate with PI
        :param family_name: string, surname
        :param given_name: sting, first name or personal name
        :return: URI identifier of this subject
        """
        #Get unique ID
        uuid = self.addPerson()
        self.graph.add((uuid, self.namespaces["foaf"]["familyName"], rdf.Literal(family_name, datatype=rdf.XSD.String)))
        self.graph.add((uuid, self.namespaces["foaf"]["givenName"], rdf.Literal(given_name, datatype=rdf.XSD.String)))
        self.graph.add((uuid, self.namespaces["prov"]["hadRole"], self.namespaces["nidm"]["PI"]))
        self.graph.add((uuid, self.namespaces["prov"]["wasAssociatedWith"], inv_id))
        return uuid

