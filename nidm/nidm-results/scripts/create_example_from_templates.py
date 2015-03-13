"""
Use templates defined in terms/templates to create a new NIDM example.

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from string import Template

NIDM_TERMS_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'terms')
TPL_DIR = os.path.join(NIDM_TERMS_DIR, 'templates')
EX_DIR = os.path.join(NIDM_TERMS_DIR, 'examples')

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

            try:
                class_example = nidm_tpm.substitute(**substitutes)
            except KeyError as e:
                print template_name
                print nidm_class
                print substitutes
                raise e

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

