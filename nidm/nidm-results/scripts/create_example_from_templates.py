"""
Use templates defined in terms/templates to create a new NIDM example.

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os, sys
from string import Template
import logging
import re

NIDM_TERMS_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'terms')
TPL_DIR = os.path.join(NIDM_TERMS_DIR, 'templates')
EX_DIR = os.path.join(NIDM_TERMS_DIR, 'examples')

# Append parent script directory to path
RELPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(RELPATH, os.pardir, os.pardir, os.pardir, "scripts"))
from OwlReader import OwlReader
from Constants import *

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)

class ExampleFromTemplate(object):
    
    def __init__(self, nidm_classes, example_file, one_file_per_class=False, 
        owl_file=None):
        self.nidm_classes = nidm_classes
        self.one_file_per_class = one_file_per_class

        self.owl = None
        if owl_file is None:
            owl_file = os.path.join(NIDM_TERMS_DIR, 'nidm-results.owl')
        self.owl = OwlReader(owl_file)

        if not one_file_per_class:
            self.file = example_file
        else:
            self.dir = example_file

    def create_example(self):
        # To make a complete document, we need to add namespaces at 
        # the beginning
        fid = open(os.path.join(TPL_DIR, "Namespaces.txt"), 'r')
        namespaces = fid.read()
        fid.close()

        example = ""
        for nidm_class, substitutes in sorted(self.nidm_classes.items()):

            templates = str.split(nidm_class, "_")
            if len(templates) > 1:
                base_template_name = templates[0]            
            else:
                base_template_name = None

            if base_template_name and \
                os.path.isfile(os.path.join(TPL_DIR, base_template_name+".txt")):
                fid = open(os.path.join(TPL_DIR, base_template_name+".txt"), 'r')
                nidm_base_tpm = Template(fid.read())
                fid.close()
            else:
                nidm_base_tpm = None
                templates = ["", nidm_class]

            class_example = ""
            if nidm_base_tpm:
                try:
                    class_example = nidm_base_tpm.substitute(**substitutes)
                except KeyError, k:
                    logger.debug(nidm_class)
                    logger.debug(base_template_name)
                    logger.debug(substitutes)
                    raise KeyError(k);

            for template in templates[1:]:
                template_name = str.split(template, "-")[0]
                if nidm_base_tpm is not None:
                    template_name = base_template_name+"_"+template_name
                    if class_example:
                        class_example = class_example[:-1]+";\n"
                logger.debug(" "+template_name)

                fid = open(os.path.join(TPL_DIR, template_name+".txt"), 'r')
                nidm_tpm = Template(fid.read())
                fid.close()                

                try:
                    class_example += nidm_tpm.substitute(**substitutes)
                except KeyError, k:
                    logger.debug(nidm_class)
                    logger.debug(template_name)
                    logger.debug(substitutes)
                    raise KeyError(k);


            if self.one_file_per_class:
                example_file = os.path.join(self.dir, nidm_class+".txt")
                example_fid = open(example_file, 'w')
                if self.owl:     
                    class_example = self.replace_alphanum_id_by_prefixes(class_example)   
                example_fid.write(str(class_example))
                example_fid.close()


            else:
                example += class_example+"\n\n"

        if not self.one_file_per_class:  
                if self.owl:     
                    example = self.replace_alphanum_id_by_prefixes(example)   
                example = namespaces+"\n"+example

                example_fid = open(self.file, 'w')
                example_fid.write(str(example))
                example_fid.close()


    def replace_alphanum_id_by_prefixes(self, example):
        alphanum_ids = re.findall('nidm:NIDM_\d*', example)

        prefix_definitions = ""
        for idt in alphanum_ids:
            term_uri = NIDM[idt.split(":")[1]]
            prefix_name = self.owl.get_label(term_uri).replace(" ", "")\
                            .replace(":", "_").replace("'", "")+":"
            prefix_definition = "@prefix "+prefix_name+" <"+str(term_uri)+"> .\n"
            if not prefix_definition in prefix_definitions:
                prefix_definitions += prefix_definition

            example = example.replace(idt, prefix_name)
        
        if prefix_definitions:
            example = prefix_definitions+"\n\n"+example

        return example