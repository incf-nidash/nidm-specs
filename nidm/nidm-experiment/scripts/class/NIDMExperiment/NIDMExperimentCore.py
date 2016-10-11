import sys
import uuid
from rdflib.namespace import XSD
from types import *
from Constants import *



class NIDMExperimentCore(object):
    """Base-class for NIDM-Experimenent

    Typically this class is not instantiated directly.  Instantiate one of the child classes such as
    NIDMExperimentInvestigation, NIDMExperimentImaging, NIDMExperimentAssessments, etec.

    @author: David Keator <dbkeator@uci.edu>
    @copyright: University of California, Irvine 2016

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

    def __str__(self):
        return "NIDM-Experiment Base Class"
