"""
Use templates defined in terms/templates to create a new NIDM example.

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from string import Template
import logging

NIDM_TERMS_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'terms')
TPL_DIR = os.path.join(NIDM_TERMS_DIR, 'templates')
EX_DIR = os.path.join(NIDM_TERMS_DIR, 'examples')

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)

class ExampleFromTemplate(object):
    
    def __init__(self, nidm_classes, example_file, one_file_per_class=False):
        self.nidm_classes = nidm_classes
        self.one_file_per_class = one_file_per_class
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

            template_name = str.split(nidm_class, "-")[0]
            fid = open(os.path.join(TPL_DIR, template_name+".txt"), 'r')
            nidm_tpm = Template(fid.read())
            fid.close()

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

            class_example = ""
            if nidm_base_tpm:
                try:
                    class_example = nidm_base_tpm.substitute(**substitutes)
                except KeyError, k:
                    logger.debug(nidm_class)
                    logger.debug(base_template_name)
                    logger.debug(substitutes)
                    raise KeyError(k);
                class_example = class_example[:-1]+" ;\n"

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
                example_fid.write(str(class_example))
                example_fid.close()
            else:
                example += class_example+"\n\n"

        if not self.one_file_per_class:              
                example = namespaces+"\n\n"+example

                example_fid = open(self.file, 'w')
                example_fid.write(str(example))
                example_fid.close()

