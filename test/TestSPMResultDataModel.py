#!/usr/bin/env python
'''Test of NI-DM SPM export 

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''
import unittest
import os
from subprocess import call
import re
import rdflib
from rdflib.graph import Graph

import logging

logger = logging.getLogger(__name__)

# FIXME: Extend tests to more than one dataset (group analysis, ...)
'''Tests based on the analysis of single-subject auditory data based on test01_spm_batch.m using SPM12b r5918.

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>, Satrajit Ghosh
@copyright: University of Warwick 2014
'''
class TestSPMResultsDataModel(unittest.TestCase):

    '''Print the results query 'res' to the console'''
    def print_results(self, res):
        for idx, row in enumerate(res.bindings):
            rowfmt = []
            print "Item %d" % idx
            for key, val in sorted(row.items()):
                rowfmt.append('%s-->%s' % (key, val.decode()))
            print '\n'.join(rowfmt)

    '''Check if the results query 'res' contains a value for each field'''
    def successful_retreive(self, res, info_str=""):
        if not res.bindings:
            self.my_execption = info_str+""": Empty query results"""
            return False
        for idx, row in enumerate(res.bindings):
            rowfmt = []
            for key, val in sorted(row.items()):
                logging.debug('%s-->%s' % (key, val.decode()))
                if not val.decode():
                    self.my_execption += "\nMissing: \t %s" % (key)
                    return False
        return True

    def setUp(self):
        self.my_execption = ""

        # Display log messages in console
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        # FIXME: This is not the right thing to do to get the test directory...
        self.test_dir = os.path.dirname(os.path.realpath('TestSPMResultsDataModel.py'))

        #  Turtle file obtained with SPM NI-DM export tool
        spm_export_ttl = os.path.join(self.test_dir, 'spm', 'SPMexport', 'test01', 'spm_nidm.ttl');
        
        # RDF obtained by the SPM export 
        self.spmexport = Graph()
        self.spm_export_ttl = os.path.join(self.test_dir, 'spm', 'SPMexport', 'test01', 'spm_nidm.ttl');
        self.spmexport.parse(spm_export_ttl, format='turtle')

    ''' Compare gt_graph and other_graph '''
    def compare_full_graphs(self, gt_graph, other_graph):
        # Check for predicates which are not in common to both graphs (XOR)
        diff_graph = gt_graph ^ other_graph

        # FIXME: There is probably something better than using os.path.basename to remove namespaces
        exlude_s = list()
        missing_s = list()

        exc_wrong = ""
        exc_added = ""
        exc_missing = ""

        for s,p,o in diff_graph.triples( (None,  None, None) ):
            # If triple is found in other_graph
            if (s,  p, o) in other_graph:
                # If subject and predicate found in gt_graph
                if (s,  p, None) in gt_graph:
                    gt_graph_possible_value = ""
                    for (s_gt_graph,  p_gt_graph, o_gt_graph) in gt_graph.triples((s,  p, None)):
                        gt_graph_possible_value += "; "+os.path.basename(o_gt_graph)
                    exc_wrong += "\nWrong:   '%s' \ton '%s' \tis '%s' (instead of '%s')"%(os.path.basename(p),other_graph.label(s),os.path.basename(o),gt_graph_possible_value[2:])
                # If subject found in gt_graph
                elif (s,  None, None) in gt_graph:
                    gt_graph_possible_value = ""
                    for (s_gt_graph,  p_gt_graph, o_gt_graph) in gt_graph.triples((s,  p, None)):
                        gt_graph_possible_value += "; "+os.path.basename(p_gt_graph)
                    exc_added += "\nAdded:   '%s' \ton '%s' (instead of '%s')"%(os.path.basename(p),other_graph.label(s),gt_graph_possible_value[2:])
                # If subject is *not* found in gt_graph
                else:
                    if not s in exlude_s:
                        exc_added += "\nAdded:   '%s'"%(s)
                        exlude_s.append(s)
            # If subject and predicate are found in gt_graph 
            elif (s,  p, o) in gt_graph:
                # If subject and predicate found in other_graph
                if (s,  p, None) in other_graph:
                    # Do nothing as already taken into account before
                    a = 1
                # If subject found in other_graph
                elif (s,  None, None) in other_graph:
                    other_graph_possible_value = ""
                    for (s_export,  p_export, o_export) in other_graph.triples((s,  p, None)):
                        other_graph_possible_value += "; "+os.path.basename(p_export)
                    exc_missing += "\nMissing:   '%s' \ton '%s' (instead of '%s')"%(os.path.basename(p),gt_graph.label(s),other_graph_possible_value[2:])
                # If subject is *not* found in other_graph
                else:
                    if not s in missing_s:
                        exc_missing += "\nMissing:   '%s' "%(s)
                        missing_s.append(s)

        self.my_execption += exc_wrong+exc_added+exc_missing


    '''Test01: Comparing that the ttl file generated by SPM and the expected ttl file (generated manually) are identical'''
    def test01_ex1_auditory_singlesub_full_graph(self):
        #  Turtle file of ground truth (manually computed) RDF
        ground_truth_ttl = os.path.join(self.test_dir, 'spm', 'GroundTruth', 'test01', 'test01_spm_results.ttl');

        # RDF obtained by the ground truth export
        gt = Graph()
        gt.parse(ground_truth_ttl, format='turtle')

        self.compare_full_graphs(gt, self.spmexport)

        if self.my_execption:
            raise Exception(self.my_execption)

    '''Test02: Test availability of attributes needed to perform a meta-analysis as specified in use-case *1* at: http://wiki.incf.org/mediawiki/index.php/Queries'''
    def test02_metaanalysis_usecase1(self):
        prefixInfo = """
        prefix prov: <http://www.w3.org/ns/prov#>
        prefix spm: <http://www.fil.ion.ucl.ac.uk/spm/ns/#>
        prefix nidm: <http://nidm.nidash.org/>

        """
        # Look for:
        # - "location" of "Contrast map",
        # - "location" of "Contrast variance map",
        # - "prov:type" in "nidm" namespace of the analysis software.
        query = prefixInfo+"""
        SELECT ?cfile ?efile ?stype WHERE {
         ?aid a spm:contrast ;
              prov:wasAssociatedWith ?sid.
         ?sid a prov:Agent;
              a prov:SoftwareAgent;
              a ?stype . 
         FILTER regex(str(?stype), "nidm") 
         ?cid a nidm:contrastMap ;
              prov:wasGeneratedBy ?aid ;
              prov:atLocation ?cfile .
         ?eid a nidm:contrastStandardErrorMap ;
              prov:wasGeneratedBy ?aid ;
              prov:atLocation ?efile .
        }
        """

        if not self.successful_retreive(self.spmexport.query(query), 'ContrastMap and ContrastStandardErrorMap'):
            raise Exception(self.my_execption)

    '''Test03: Test availability of attributes needed to perform a meta-analysis as specified in use-case *2* at: http://wiki.incf.org/mediawiki/index.php/Queries'''
    def test03_metaanalysis_usecase2(self):
        prefixInfo = """
        prefix prov: <http://www.w3.org/ns/prov#>
        prefix spm: <http://www.fil.ion.ucl.ac.uk/spm/ns/#>
        prefix nidm: <http://nidm.nidash.org/>

        """

        # Look for:
        # - "location" of "Contrast map",
        # - "prov:type" in "nidm" namespace of the analysis software.
        query = prefixInfo+"""
        SELECT ?cfile ?efile ?stype WHERE {
         ?aid a spm:contrast ;
              prov:wasAssociatedWith ?sid.
         ?sid a prov:Agent;
              a prov:SoftwareAgent;
              a ?stype . 
         FILTER regex(str(?stype), "nidm") 
         ?cid a nidm:contrastMap ;
              prov:wasGeneratedBy ?aid ;
              prov:atLocation ?cfile .
        }
        """

        if not self.successful_retreive(self.spmexport.query(query), 'ContrastMap and ContrastStandardErrorMap'):
            raise Exception(self.my_execption)

    '''Test04: Test availability of attributes needed to perform a meta-analysis as specified in use-case *3* at: http://wiki.incf.org/mediawiki/index.php/Queries'''
    def test04_metaanalysis_usecase3(self):
        prefixInfo = """
        prefix prov: <http://www.w3.org/ns/prov#>
        prefix spm: <http://www.fil.ion.ucl.ac.uk/spm/ns/#>
        prefix nidm: <http://nidm.nidash.org/>

        """

        # Look for:
        # - "location" of "Statistical map",
        # - "nidm:errorDegreesOfFreedom" in "Statistical map".
        query = prefixInfo+"""
        SELECT ?sfile ?dof WHERE {
         ?sid a nidm:statisticalMap ;
              prov:atLocation ?sfile ;
              nidm:errorDegreesOfFreedom ?dof .
        }
        """

        if not self.successful_retreive(self.spmexport.query(query), 'ContrastMap and ContrastStandardErrorMap'):
            raise Exception(self.my_execption)

    '''Test05: Test availability of attributes needed to perform a meta-analysis as specified in use-case *4* at: http://wiki.incf.org/mediawiki/index.php/Queries'''
    def test05_metaanalysis_usecase4(self):
        prefixInfo = """
        prefix prov: <http://www.w3.org/ns/prov#>
        prefix spm: <http://www.fil.ion.ucl.ac.uk/spm/ns/#>
        prefix nidm: <http://nidm.nidash.org/>

        """

        # Look for:
        # - For each "Peak" "equivZStat" and"coordinate1" (and optionally "coordinate2" and "coordinate3"),
        # - "clusterSizeInVoxels" of "height threshold"
        # - "value" of "extent threshold"
        query = prefixInfo+"""
        SELECT ?equivz ?coord1 ?coord2 ?coord3 ?ethresh ?hthresh WHERE {
         ?pid a spm:PeakStatistic ;
            prov:atLocation ?cid ;
            nidm:equivalentZStatistic ?equivz ;
            prov:wasDerivedFrom ?clid .
         ?cid a nidm:coordinate;
            nidm:coordinate1 ?coord1 .
            OPTIONAL { ?cid nidm:coordinate2 ?coord2 }
            OPTIONAL { ?cid nidm:coordinate3 ?coord3 }
         ?iid a nidm:inference .
         ?esid a nidm:ExcursionSetMap;
            prov:wasGeneratedBy ?iid .
         ?setid a spm:SetStatistic;
            prov:wasDerivedFrom ?esid .
         ?clid a spm:ClusterStatistic;
            prov:wasDerivedFrom ?setid .
         ?tid a nidm:extentThreshold ;
            nidm:clusterSizeInVoxels ?ethresh .
         ?htid a nidm:heightThreshold ;
            prov:value ?hthresh .
        }
        """

        if not self.successful_retreive(self.spmexport.query(query), 'ContrastMap and ContrastStandardErrorMap'):
            raise Exception(self.my_execption)


if __name__ == '__main__':
    unittest.main()
