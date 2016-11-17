
import rdflib as rdf
import os, sys

from NIDMExperiment import NIDMExperimentCore


class NIDMExperimentInvestigation(NIDMExperimentCore):
    """Class for NIDM-Experimenent Investigation-Level Objects.

    Default constructor uses empty graph with namespaces added from NIDM/Scripts/Constants.py.
    Additional alternate constructors for user-supplied graphs and default namespaces (i.e. from Constants.py)
    and user-supplied graph and namespaces

    @author: David Keator <dbkeator@uci.edu>
    @copyright: University of California, Irvine 2016

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
        #create unique ID
        self.uuid = self.getUUID()
        #add to graph
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, self.namespaces["dctypes"]["Dataset"]))
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, self.namespaces["nidm"]["Investigation"]))
        self.graph.add((self.namespaces["nidm"][self.uuid], rdf.RDF.type, self.namespaces["prov"]["Entity"]))
        self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces["ncit"]["Identifier"], rdf.Literal(inv_id)))
        self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces["dct"]["title"], rdf.Literal(inv_name, datatype=rdf.XSD.String)))
        self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces["dct"]["description"], rdf.Literal(inv_description, lang=self.language)))

    def addLiteralAttribute(self, pred_namespace, pred_term, object):
        #figure out datatype of literal
        datatype = self.getDataType(object)
        #figure out if predicate namespace is defined, if not, return predicate namespace error
        try:
            if (datatype != None):
                self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces[pred_namespace][pred_term], rdf.Literal(object, datatype=datatype)))
            else:
                self.graph.add((self.namespaces["nidm"][self.uuid], self.namespaces[pred_namespace][pred_term], rdf.Literal(object)))
        except (KeyError,),e:
            print "\nPredicate namespace identifier \"" + str(e).split("'")[1] + "\" not found!"
            print "Use addNamespace method to add namespace before adding literal attribute"
            print "No attribute has been added \n"


    def serializeTurtle(self):
        return self.graph.serialize(format='turtle')