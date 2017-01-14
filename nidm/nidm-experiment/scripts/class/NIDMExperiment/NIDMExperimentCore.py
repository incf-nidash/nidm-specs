import sys
import uuid
from rdflib.namespace import XSD
from types import *
from Constants import *
import rdflib as rdf



class NIDMExperimentCore(object):
    """Base-class for NIDM-Experimenent

    Typically this class is not instantiated directly.  Instantiate one of the child classes such as
    NIDMExperimentInvestigation, NIDMExperimentImaging, NIDMExperimentAssessments, etec.

    @author: David Keator <dbkeator@uci.edu>
    @copyright: University of California, Irvine 2017

    """
    language = 'en'
    def __init__(self):
        """
        Default constructor, loads empty graph and namespaces from NIDM/Scripts/Constants.py
        """
        #make a local copy q_graph with namespaces already bound
        self.graph = q_graph
        #make a local copy of the namespaces
        self.namespaces = namespaces

    #class constructor with user-supplied graph, namespaces from Constants.py
    @classmethod
    def withGraph(self,graph):
        """
        Alternate constructor, loads user-supplied graph and default namespaces from NIDM/Scripts/Constants.py

        Keyword arguments:
            graph -- an rdflib.Graph object
        """
        self.graph = graph
        #bind namespaces to self.graph
        for name, namespace in self.namespaces.items():
            self.graph.bind(name, namespace)

    #class constructor with user-supplied graph and namespaces
    @classmethod
    def withGraphAndNamespaces(self,graph,namespaces):
        """
        Alternate constructor, loads user-supplied graph and binds user-supplied namespaces

        :param graph: an rdflib.Graph object
        :param namespaces: python dictionary {namespace_identifier, URL}
        :return: none
        """


        self.graph = graph
        self.namespaces = namespaces
        #bind namespaces to self.graph
        for name, namespace in self.namespaces.items():
            self.graph.bind(name, namespace)

    def getGraph(self):
        """
        Returns rdflib.Graph object
        """
        return self.graph

    def getNamespace(self):
        """
        Returns namespace dictionary {namespace_id, URL}
        """
        return self.namespaces

    def addNamespace(self, prefix, namespace):
        """
        Adds namespace to self.graph
        :param prefix: namespace identifier
        :param namespace: namespace URL
        :return: none
        """
        self.graph.bind(prefix, namespace)

    def safe_string(self, string):
        return string.strip().replace(" ","_").replace("-", "_").replace(",", "_").replace("(", "_").replace(")","_")\
            .replace("'","_").replace("/", "_")

    def getUUID (self):
        return str(uuid.uuid1())

    def getDataType(self,var):
        if type(var) is IntType:
            return XSD.integer
        elif type(var) is LongType:
            return XSD.long
        elif type(var) is FloatType:
            return XSD.float
        elif (type(var) is StringType) or (type(var) is UnicodeType):
            return XSD.string
        else:
            return None
    def addLiteralAttribute(self, id, pred_namespace, pred_term, object):
        """
        Adds generic literal to subject [id] and inserts into the graph
        :param id: subject identifier/URI
        :param pred_namespace: predicate namespace URL
        :param pred_term: predidate term to associate with tuple
        :param object: literal to add as object of tuple
        :return: none
        """
        #figure out datatype of literal
        datatype = self.getDataType(object)
        #figure out if predicate namespace is defined, if not, return predicate namespace error
        try:
            if (datatype != None):
                self.graph.add((id, self.namespaces[pred_namespace][pred_term], rdf.Literal(object, datatype=datatype)))
            else:
                self.graph.add((id, self.namespaces[pred_namespace][pred_term], rdf.Literal(object)))
        except (KeyError,),e:
            print "\nPredicate namespace identifier \"" + str(e).split("'")[1] + "\" not found!"
            print "Use addNamespace method to add namespace before adding literal attribute"
            print "No attribute has been added \n"
    def addPerson(self):
        """
        Generic add prov:Person, use addLiteralAttribute to add more descriptive attributes
        :return: URI identifier of this subject
        """
        #Get unique ID
        uuid = self.getUUID()
        #add to graph
        self.graph.add((self.namespaces["nidm"][uuid], rdf.RDF.type, self.namespaces["prov"]["Person"]))
        return self.namespaces["nidm"][uuid]
    def wasAssociatedWith(self, subject, object):
        """
        Generic prov:wasAssociatedWith function to associate the subject and objects together in graph
        :param subject: URI of subject (e.g. person)
        :param object: URI of object (e.g. investigation)
        :return: URI identifier of this subject
        """
        self.graph.add((subject, self.namespaces["prov"]["wasAssociatedWith"], object))
    def serializeTurtle(self):
        """
        Serializes graph to Turtle format
        :return: text of serialized graph in Turtle format
        """
        return self.graph.serialize(format='turtle')
    def __str__(self):
        return "NIDM-Experiment Base Class"
