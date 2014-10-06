# For each document in the NIDM repository, this script checks if there is a public document with the same content (from title)
# in the Prov Store (https://provenance.ecs.soton.ac.uk/store). If there is none, the document is uploaded and its README file is updated
# to link to the json, turtle, svg, PDF and png serialisations. 

# To use this script you need to have an account on the Prov Store (cf. https://provenance.ecs.soton.ac.uk/store/account/signup/) and to
# create a file named store_login_key.txt in the same directory including the following text: "mylogin:mykey" where mylogin 
# must be replaced by your Prov Store login and mykey by your ApiKey (cf. https://provenance.ecs.soton.ac.uk/store/account/developer/)

import urllib2
import json
import logging
import os
import rdflib
from rdflib.graph import Graph
from rdflib.compare import *
import sys

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)

# Append test directory to path
sys.path.append(os.path.join(RELPATH, "..", "test"))
from TestCommons import example_filenames
from CheckConsistency import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class_termsPATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'terms')

NIDM_PENDING_FINAL = 'nidm:PendingFinalVetting'
NIDM_METADATA_INCOMPLETE = 'nidm:MetadataIncomplete'
NIDM_REQUIRES_DISCUSSION = 'nidm:RequiresDiscussion'
NIDM_UNCURATED = 'nidm:Uncurated'
NIDM_TO_BE_REPLACED = 'nidm:ToBeReplacedByExternalOntologyTerm'
NIDM_READY = 'nidm:ReadyForRelease'

CURATION_COLORS = dict()
CURATION_COLORS[NIDM_PENDING_FINAL] = "green"
CURATION_COLORS[NIDM_METADATA_INCOMPLETE] = "orange"
CURATION_COLORS[NIDM_REQUIRES_DISCUSSION] = "orange"
CURATION_COLORS[NIDM_UNCURATED] = "red"
CURATION_COLORS[NIDM_TO_BE_REPLACED] = "yellow"

CURATION_ORDER = list([NIDM_PENDING_FINAL, NIDM_METADATA_INCOMPLETE, NIDM_REQUIRES_DISCUSSION, NIDM_UNCURATED, NIDM_TO_BE_REPLACED])

class UpdateTermReadme():

    def __init__(self, owl_file):
        self.data = []
        
        # Read owl (turtle) file
        self.owl = Graph()

        # This is a workaround to avoid issue with "#" in base prefix as 
        # described in https://github.com/RDFLib/rdflib/issues/379,
        # When the fix is introduced in rdflib these 2 lines will be replaced by:
        # self.owl.parse(owl_file, format='turtle')
        owl_txt = open(owl_file, 'r').read().replace("http://www.w3.org/2002/07/owl#", 
                        "http://www.w3.org/2002/07/owl")
        self.owl.parse(data=owl_txt, format='turtle')
        
        # Retreive all classes defined in the owl file
        self.owl_classes = get_class_names_in_owl(self.owl) #set(); #{'entity': set(), 'activity': set(), 'agent' : set()}
        self.owl_properties = get_property_names_in_owl(self.owl)
        # # For each class find out attribute list as defined by domain in attributes
        # attributes_ranges = get_attributes_from_owl(self.owl)
        # self.attributes = attributes_ranges[0]
        # self.ranges = attributes_ranges[1]      
        # self.type_restrictions = attributes_ranges[2]     

    # Write out Readme
    def write_readme(self, readme_file, readme_txt):
        readme_file_open = open(readme_file, 'w')
        readme_file_open.write(readme_txt)
        readme_file_open.close()

    def get_definition(self, owl_term):
        definition = list(self.owl.objects(owl_term, PROV['definition']))
        if definition:
            definition = str(definition[0])
        else:
            definition = ""
        return definition

    def get_range(self, owl_term):
        ranges = list(self.owl.objects(owl_term, RDFS['range']))

        range_display = ""
        for range_value in ranges:
            if isinstance(range_value, rdflib.term.URIRef):
                range_display += str(self.owl.qname(range_value))+" "
            else:
                range_display += str(range_value)
        return range_display

    def get_domain(self, owl_term):
        domains = list(self.owl.objects(owl_term, RDFS['domain']))

        domain_display = ""
        for domain_value in sorted(domains):
            if isinstance(domain_value, rdflib.term.URIRef):
                domain_display += str(self.owl.qname(domain_value))+" "
            else:
                domain_display += str(domain_value)
        return domain_display

    def get_curation_status(self, owl_term):
        curation_status = NIDM['Uncurated']
        curation_status = list(self.owl.objects(owl_term, NIDM['curationStatus']))
        if curation_status:
            curation_status = curation_status[0]
        return curation_status

    def get_editor(self, owl_term):
        editor = list(self.owl.objects(owl_term, NIDM['termEditor']))
        if editor:
            editor = " (editor: "+editor[0]+")"
        else:
            editor = ""
        return editor

    def create_term_row(self, term_name, definition, editor, color, range_value=None, domain=None):
        img_color = ""        
        if color:
            img_color = '<img src="../../../doc/content/specs/img/'+color+'.png?raw=true"/>  ' 

        range_domain = ""
        if range_value is not None:
            range_domain = """
    <td>"""+domain+"""</td>
    <td>"""+range_value+"""</td>"""

        term_row = """
<tr>
    <td>"""+img_color+"""</td>
    <td><b>"""+term_name+""": </b>"""+definition+editor+"""</td>"""+range_domain+"""
</tr>"""
        return term_row

    def create_curation_legend(self, order):
        curation_legend = "<b>Curation status</b>: "
        curation_colors_sorted = [(key, CURATION_COLORS.get(key)) for key in order]
        for curation_color in curation_colors_sorted:
            curation_status =  curation_color[0]
            color =  curation_color[1]
            if color:
                curation_legend = curation_legend+'<img src="../../../doc/content/specs/img/'+color+'.png?raw=true"/>&nbsp;'+\
                    curation_status.replace("nidm:", "")+";\n"
        return curation_legend

    # Get README text according to owl file information
    def update_readme(self, readme_file): 
        class_terms = dict()
        prpty_terms = dict()
        attribute_terms = dict()
        definitions = dict()
        editors = dict()
        ranges = dict()
        domains = dict()

        for owl_term in self.owl_classes.union(self.owl_properties):
            curation_status = self.get_curation_status(owl_term)
            definition = self.get_definition(owl_term)
            editor = self.get_editor(owl_term)
            range_value = self.get_range(owl_term)
            domain = self.get_domain(owl_term)
            
            if definition:
                if curation_status:
                    curation_key = str(curation_status)
                    term_key = self.owl.qname(owl_term)
                    if owl_term in self.owl_classes:
                        class_terms.setdefault(curation_key, list()).append(term_key)
                    else:
                        if owl_term in self.owl_properties:
                            prpty_terms.setdefault(curation_key, list()).append(term_key)
                    definitions[term_key] = definition
                    editors[term_key] = editor
                    ranges[term_key] = range_value
                    domains[term_key] = domain

        # Include missing keys and do not display ready for release terms
        order=CURATION_ORDER+(list(set(class_terms.keys()).union(set(prpty_terms.keys())) - set(CURATION_ORDER+list([NIDM_READY]))))
        class_terms_sorted = [(key, class_terms.get(key)) for key in order]
        prpty_terms_sorted = [(key, prpty_terms.get(key)) for key in order]

        class_table_txt = "<h2>Classes</h2>\n<table>\n<tr><th>Curation Status</th><th>Term</th></tr>"
        for tuple_status_term in class_terms_sorted:
            curation_status = tuple_status_term[0]
            class_names = tuple_status_term[1]

            if class_names:
                for class_name in sorted(class_names):
                    class_table_txt += self.create_term_row(class_name, \
                        definitions[class_name], \
                        editors[class_name], \
                        CURATION_COLORS.setdefault(curation_status, ""))
        class_table_txt = class_table_txt+"\n</table>"

        prpty_table_txt = "<h2>Properties</h2>\n<table>\n<tr><th>Curation Status</th><th>Term</th><th>Domain</th><th>Range</th></tr>"
        for tuple_status_term in prpty_terms_sorted:
            curation_status = tuple_status_term[0]
            term_names = tuple_status_term[1]

            if term_names:
                for term_name in sorted(term_names):
                    prpty_table_txt += self.create_term_row(term_name, \
                        definitions[term_name], \
                        editors[term_name], \
                        CURATION_COLORS.setdefault(curation_status, ""), \
                        ranges[term_name], \
                        domains[term_name])
        prpty_table_txt = prpty_table_txt+"\n</table>"

        curation_legend = self.create_curation_legend(order)
        title = "<h1>NIDM-Results Terms curation status</h1>"
        self.write_readme(readme_file, title+curation_legend+class_table_txt+prpty_table_txt)

if __name__ == '__main__':
    # Retreive owl file for NIDM-Results
    owl_file = os.path.join(class_termsPATH, 'nidm-results.owl')

    # check the file exists
    assert os.path.exists(owl_file)

    updateReadme = UpdateTermReadme(owl_file)

    readme_file = os.path.join(class_termsPATH, 'README.md')
    updateReadme.update_readme(readme_file)


