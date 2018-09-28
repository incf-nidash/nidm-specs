"""
Use templates defined in terms/templates to create a new NIDM example.

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os, sys
from string import Template
import logging
import re
import glob
import rdflib as rl
import pyld as ld
import json

NIDM_TERMS_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'terms')
NIDMPATH = os.path.join(NIDM_TERMS_DIR, os.pardir, os.pardir)
TPL_DIR = os.path.join(NIDM_TERMS_DIR, 'templates')
EX_DIR = os.path.join(NIDM_TERMS_DIR, 'examples')

# Append parent script directory to path
RELPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(
    os.path.join(RELPATH, os.pardir, os.pardir, os.pardir, "scripts"))
from nidmresults.owl.owl_reader import OwlReader
from nidmresults.objects.constants_rdflib import *

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)


class ExampleFromTemplate(object):

    def __init__(self, nidm_classes, example_file, one_file_per_class=False,
                 owl_file=None, remove_att=None):
        self.nidm_classes = nidm_classes
        self.one_file_per_class = one_file_per_class
        self.remove_att = remove_att

        self.owl = None
        if owl_file is None:
            import_files = glob.glob(
                os.path.join(NIDMPATH, "imports", '*.ttl'))
            owl_file = os.path.join(NIDM_TERMS_DIR, 'nidm-results.owl')

        self.owl = OwlReader(owl_file, import_files)

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
                os.path.isfile(
                    os.path.join(TPL_DIR, base_template_name+".txt")):
                fid = open(
                    os.path.join(TPL_DIR, base_template_name+".txt"), 'r')
                nidm_base_tpm = Template(fid.read())
                fid.close()
            else:
                nidm_base_tpm = None
                templates = ["", nidm_class]

            class_example = ""

            if nidm_base_tpm:
                try:
                    class_example += nidm_base_tpm.substitute(**substitutes)
                except KeyError, k:
                    logger.debug("--- Key error on ---")
                    logger.debug(self.file)
                    logger.debug(nidm_class)
                    logger.debug(substitutes)
                    raise KeyError(k)

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
                    logger.debug("--- Key error on ---")
                    logger.debug(self.file)
                    logger.debug(nidm_class)
                    logger.debug(substitutes)
                    raise KeyError(k)

            if self.one_file_per_class:
                example_file = os.path.join(self.dir, nidm_class+".txt")
                example_fid = open(example_file, 'w')
                if self.remove_att is not None:
                    class_example = \
                        self.remove_attributes(self.remove_att, class_example)
                if self.owl:
                    class_example = self.replace_alphanum_id_by_prefixes(
                        class_example)
                if "comment" in substitutes.keys():
                    class_example = "#  " + substitutes['comment'] + "\n\n" + \
                                    class_example
                example_fid.write(str(class_example))
                example_fid.close()

            else:
                example += class_example+"\n\n"

        if not self.one_file_per_class:
                if self.remove_att is not None:
                    example = self.remove_attributes(self.remove_att, example)
                if self.owl:
                    example = self.replace_alphanum_id_by_prefixes(example)
                example = namespaces+"\n"+example
                if "comment" in substitutes.keys():
                    class_example = "#  " + substitutes['comment'] + "\n\n" + \
                                    class_example
                if not os.path.isdir(os.path.dirname(self.file)):
                    os.mkdir(os.path.dirname(self.file))
                example_file = self.file
                example_fid = open(example_file, 'w')
                example_fid.write(str(example))
                example_fid.close()

                # Create JSON-LD version
                g = rl.ConjunctiveGraph()
                g.parse(example_file, format='turtle')
                g2 = g.serialize(format='json-ld')

                # Create nice JSON-LD version
                with open(os.path.join(TPL_DIR, "..", "nidmr.json")) as jnidm:
                    context = json.load(jnidm)

                # context = {"@context":
                #            os.path.join(TPL_DIR, "..", "nidmr.json")}
                foo = ld.jsonld.compact(json.loads(g2), context)
                with open(self.file.replace('.ttl', '.json'), "w") as fid:
                    fid.write(json.dumps(foo, indent=2))

    def remove_attributes(self, terms, example):
        for term in terms:
            for att in re.findall(r"\s*"+q_graph.qname(term)+".*", example):
                example = example.replace(att, "")
                # If we removed the final dot then put it back
                if att.rsplit(None, 1)[-1] == ".":
                    example = example[::-1].replace(
                        ";"[::-1], "."[::-1], 1)[::-1]
        return example

    def replace_alphanum_id_by_prefixes(self, example):
        # FIXME: This should be done automatically using prefixes.csv
        alphanum_ids = re.findall('nidm:NIDM_\d*', example) + \
                       re.findall(
                        'http://purl.org/nidash/nidm#NIDM_\d*', example) + \
                       re.findall('obo:STATO_\d*', example) + \
                       re.findall(
                        'http://purl.obolibrary.org/obo/STATO_\d*', example) +\
                       re.findall('obo:OBI_\d*', example) + \
                       re.findall('spm:SPM_\d*', example) + \
                       re.findall(
                        'http://purl.org/nidash/spm#SPM_\d*', example) + \
                       re.findall('fsl:FSL_\d*', example) + \
                       re.findall(
                        'http://purl.org/nidash/fsl#FSL_\d*', example) + \
                       re.findall('nlx:[\w-]*', example) + \
                       re.findall(
                        'http://scicrunch.org/resolver/SCR_\d*', example) + \
                       re.findall('scr:SCR_\w*', example)

        prefix_definitions = ""
        for idt in alphanum_ids:
            if idt.startswith("nidm:"):
                term_uri = NIDM[idt.split(":")[1]]
            elif idt.startswith("http://purl.org/nidash/nidm"):
                term_uri = NIDM[idt.split("#")[1]]
            elif idt.startswith("obo:"):
                term_uri = OBO[idt.split(":")[1]]
            elif idt.startswith("http://purl.obolibrary.org/obo/STATO_"):
                term_uri = OBO[idt.split("/")[-1]]
            elif idt.startswith("spm:"):
                term_uri = SPM[idt.split(":")[1]]
            elif idt.startswith("http://purl.org/nidash/spm"):
                term_uri = SPM[idt.split("#")[1]]
            elif idt.startswith("fsl:"):
                term_uri = FSL[idt.split(":")[1]]
            elif idt.startswith("http://purl.org/nidash/fsl"):
                term_uri = FSL[idt.split("#")[1]]
            elif idt.startswith("nlx:"):
                term_uri = NLX[idt.split(":")[1]]
            elif idt.startswith("scr:"):
                term_uri = SCR[idt.split(":")[1]]
            elif idt.startswith("http://scicrunch.org/resolver/SCR_"):
                term_uri = SCR[idt.split("/")[1]]
            else:
                raise Exception('Unknown alphanumeric id: ' + idt)

            prefix_name = self.owl.get_label(term_uri).replace(" ", "")\
                                                      .replace(":", "_")\
                                                      .replace("'", "")\
                                                      .replace("-", "")+":"
            prefix_definition = "@prefix " + prefix_name + " <" + \
                                str(term_uri)+"> .\n"
            if prefix_definition not in prefix_definitions:
                prefix_definitions += prefix_definition

            example = example.replace(idt, prefix_name)

        if prefix_definitions:
            example = prefix_definitions+"\n\n"+example

        return example