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

TERMSPATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'terms')

class UpdateTermsReadme():

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
        # # For each class find out attribute list as defined by domain in attributes
        # # For each ObjectProperty found out corresponding range
        # attributes_ranges = get_attributes_from_owl(self.owl)
        # self.attributes = attributes_ranges[0]
        # self.ranges = attributes_ranges[1]      
        # self.type_restrictions = attributes_ranges[2]     
    # Update Readme
    def write_readme(self, readme_file, readme_txt):
        readme_file_open = open(readme_file, 'w')
        readme_file_open.write(readme_txt)
        readme_file_open.close()

    def update_readme(self, readme_file): 
        terms = dict()
        definitions = dict()
        editors = dict()

        for owl_class in self.owl_classes:
            curation_status = NIDM['Uncurated']
            curation_status = list(self.owl.objects(owl_class, NIDM['curationStatus']))
            if curation_status:
                curation_status = curation_status[0]

            definition = list(self.owl.objects(owl_class, PROV['definition']))
            if definition:
                definition = definition[0]
            else:
                definition = ""

            editor = list(self.owl.objects(owl_class, NIDM['termEditor']))
            if editor:
                editor = " (editor: "+editor[0]+")"
            else:
                editor = ""

            if definition:
                if curation_status:
                    curation_key = str(curation_status)
                    class_key = self.owl.qname(owl_class)
                    if curation_key in terms:
                        terms[curation_key].add(class_key)
                    else:
                        terms[curation_key] = set([class_key])
                    if class_key in definitions:
                        definitions[class_key].add(definition)
                    else:
                        definitions[class_key] = definition
                    if class_key in editors:
                        editors[class_key].add(editor)
                    else:
                        editors[class_key] = editor                    

        table_txt = "<table>\n<tr><th>Curation Status</th><th>Term</th></tr>"

        img_colors = dict()
        img_colors['nidm:PendingFinalVetting'] = "green"
        img_colors['nidm:MetadataIncomplete'] = "orange"
        img_colors['nidm:Uncurated'] = "red"
        order = "nidm:PendingFinalVetting,nidm:MetadataIncomplete,nidm:Uncurated".split(',')
        # Include missing keys
        order+=(list(set(terms.keys()) - set(order+list(['nidm:ReadyForRelease']))))
        terms_sorted = [(key, terms.get(key)) for key in order]

        for tuple_status_term in terms_sorted:
            curation_status = tuple_status_term[0]
            class_names = tuple_status_term[1]

            img_color=""     
            if curation_status in img_colors:
                img_color = '<img src="./doc/content/specs/img/'+img_colors[curation_status]+'.png"/>  ' 

            if class_names:
                for class_name in class_names:
                    table_txt = table_txt+"<tr>"+\
                            "<td>"+img_color+curation_status+editors[class_name]+"</td>"\
                            "<td><b>"+class_name+": </b>"+definitions[class_name]+"</td></tr>"
        table_txt = table_txt+"\n</table>"
        self.write_readme(readme_file, table_txt)

if __name__ == '__main__':
    # Retreive owl file for NIDM-Results
    owl_file = os.path.join(TERMSPATH, 'nidm-results.owl')
    print owl_file
    # check the file exists
    assert os.path.exists(owl_file)

    updateReadme = UpdateTermsReadme(owl_file)

    readme_file = os.path.join(TERMSPATH, 'README.md')
    updateReadme.update_readme(readme_file)
    # print aa.owl


