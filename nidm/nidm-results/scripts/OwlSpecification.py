# Automatically-generates section 2 of a specification document given an owl file

import urllib2
import json
import logging
import os
import rdflib
from rdflib.graph import Graph
from rdflib.compare import *
import sys
import codecs
import collections


RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)

# Append test directory to path
sys.path.append(os.path.join(RELPATH, "..", "test"))
from TestCommons import example_filenames
from CheckConsistency import *
from OwlReader import OwlReader

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TERMS_FOLDER = os.path.join(NIDMRESULTSPATH, 'terms')
DOC_FOLDER = os.path.join(os.path.dirname(os.path.dirname(NIDMRESULTSPATH)), 'doc', 'content', 'specs')

class OwlSpecification(object):

    def __init__(self, owl_file, spec_name, components=None):
        self.owl = OwlReader(owl_file)
        self.name = spec_name
        self.section_open = 0

        self.text = ""
        self.create_specification(components)

    def create_specification(self, components):
        self.create_title(self.name+": Types and relations")

        # If no components are defined diplay all classes
        if not components:
            components = dict([(None, self.owl.classes)])

        for component_name, classes in components.items():

            classes_by_types = self.owl.get_class_names_by_prov_type(classes)

            self.create_component_table(classes_by_types, component_name)

            all_classes = sorted(classes_by_types[PROV['Agent']])+\
                          sorted(classes_by_types[PROV['Activity']])+\
                          sorted(classes_by_types[PROV['Entity']])
            for class_name in all_classes:
                self.create_class_section(
                    class_name, 
                    self.owl.get_definition(class_name), 
                    self.owl.attributes.setdefault(class_name, None))

            if component_name:
                self.text += """
            </section>"""

        self.close_sections()

    def create_component_table(self, classes, component_name=None):
        if component_name:
            self.text += """
        <section><h1>"""+component_name+"""</h1>"""
        else:
            component_name = ""

        self.text += """
        <div style="text-align: left;">
            <table class="thinborder" style="margin-left: auto; margin-right: auto;">
                <caption id="overview-types-and-relations"><span>Table 2<sup>\
                <a class="internalDFN" href="#overview-types-and-relations">\
                <span class="diamond"> &#9826;:</span></a></sup> </span>\
                Mapping of """+self.name+""" """+component_name+""" Core Concepts to types and relations \
                and PROV core concepts</caption> \
                <!-- Table 2 -->
                <tbody>
                    <tr>
                        <td><b>NIDM-Results Concepts</b></td>
                        <td><b>Types or Relation (PROV concepts)</b></td>
                        <td><b>Name</b></td>
                    </tr>
        """


        self.text += """
        <!-- HERE ------------- Beginning of PROV Entities ------------- -->
        """

        for prov_class in list([PROV['Agent'], PROV['Activity'], PROV['Entity']]):
            sorted_classes = sorted(classes[prov_class])
            for class_name in sorted_classes:
                class_qname = self.owl.graph.qname(class_name)
                self.text += """
                        <tr>
                            <td><a title="concept-"""+class_qname+"""">"""+class_qname+"""</a>
                            </td>
                    """

                # First iteration
                if class_name is sorted_classes[0]:
                    self.text += """
                                <td rowspan=\""""+str(len(sorted_classes))+"""\" style="text-align: center;">NIDM-Results Types<br/> \
                                (PROV """+self.owl.graph.qname(prov_class).replace('prov:', '')+""")</td>
                        """

                self.text += """
                                <td><a>"""+class_qname+"""</a></td>
                            </tr>
                """

        self.text += """
                </tbody>
                </table>
            </div>"""

    def create_title(self, title):
        self.text += """
        <section>
            <h1>"""+title+"""</h1>
        """
        self.section_open += 1

    def create_class_section(self, class_name, definition, attributes="my attr"):
        class_qname = self.owl.graph.qname(class_name)

        # Lower case first letter of definition
        if definition:
            definition = definition[0].lower() + definition[1:]

        if definition[-1:] is not ".":
            definition += "."

        self.text += """
            <!-- """+class_qname+""" -->
            <section id="section-"""+class_qname+""""> 
                <h1 label=\""""+class_qname+"""\">"""+class_qname+"""</h1>
                <div class="glossary-ref">
                    <dfn title="concept-"""+class_qname+"""">"""+class_qname+"""</dfn>\
                    <sup><a title="concept-"""+class_qname+""""><span class="diamond">&#9826;</span></a></sup> is 
                    """+definition+""" 
                </div>
                <p></p>
                <div class="attributes" id="attributes-"""+class_qname+""""> A nidm:<dfn>"""+class_qname+"""</dfn>\
                <sup><a title=\""""+class_qname+""""><span class="diamond"> &#9826;</span></a></sup><span class="withPn"></span> has attributes:
                <ul>
                    <li><span class="attribute" id=\""""+class_qname+""".label">prov:label</span>: an <em class="rfc2119" title="OPTIONAL">OPTIONAL</em> label describing the """+class_qname+""".</li>
                    
                    
                    """
        if attributes:
            for att in attributes:
                att_name = self.owl.graph.qname(att)
                att_def = self.owl.get_definition(att)
                self.text += """ 
                    <li><span class="attribute" id=\""""+class_qname+"""."""+att_name+"""">"""+att_name+"""\
                    </span>: an <em class="rfc2119" title="OPTIONAL">OPTIONAL</em>"""+att_def+""".</li>
                """

        example = self.owl.get_example(class_name)
        if example:
            self.text += """        
                </ul>
                </div>
                <pre class='example highlight'>"""+self.owl.get_example(class_name)+"""</pre>"""

        self.text += """  
            </section>"""

    def close_sections(self):
        for x in range(0, self.section_open):
            self.text += "\t"*x+"</section>\n"

    # Write out specification
    def write_specification(self, spec_file, prev_file=None, follow_file=None):
        spec_open = codecs.open(spec_file, 'w', "utf-8")
        if prev_file:
            prev_file_open = open(prev_file, 'r')
            self.text = prev_file_open.read().decode('utf-8')+self.text
            prev_file_open.close()
        if follow_file:
            follow_file_open = open(follow_file, 'r')
            self.text = self.text+follow_file_open.read()
            follow_file_open.close()

        spec_open.write(self.text)
        spec_open.close()


if __name__ == '__main__':
    # Retreive owl file for NIDM-Results
    owl_file = os.path.join(TERMS_FOLDER, 'nidm-results.owl')

    # check the file exists
    assert os.path.exists(owl_file)

    components =  collections.OrderedDict()
    components["Model fitting"] = [NIDM['Data'], NIDM['ErrorModel'], NIDM['DesignMatrix'], 
             NIDM['ModelParametersEstimation'], NIDM['ParameterEstimateMap'],
             NIDM['ResidualMeanSquaresMap'], NIDM['MaskMap'], NIDM['ContrastWeights'],
             NIDM['ContrastMap'], NIDM['StatisticMap']]
    components["Inference"] = [NIDM['Inference'], NIDM['HeightThreshold'], NIDM['ExtentThreshold'], 
             NIDM['MaskMap'], NIDM['ExcursionSet'],
             NIDM['SearchSpaceMap'], NIDM['Cluster'], NIDM['Peak'],
             NIDM['Coordinate']]
    components["SPM-specific Concepts"] = [SPM['ReselsPerVoxelMap']]
    components["FSL-specific Concepts"] = [FSL['CenterOfGravity']]

    owlspec = OwlSpecification(owl_file, "NIDM-Results", components)

    INCLUDE_FOLDER = os.path.join(DOC_FOLDER, "include")
    owlspec.write_specification(os.path.join(DOC_FOLDER, "spec.html"),
        os.path.join(INCLUDE_FOLDER, "nidm-results_head.html"),
        os.path.join(INCLUDE_FOLDER, "nidm-results_foot.html"))


