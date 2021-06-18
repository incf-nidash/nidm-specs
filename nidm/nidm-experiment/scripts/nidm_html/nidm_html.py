import os
import codecs
import collections
import sys
import glob
from nidm_owl_reader import OwlReader
from nidm_constants import *
from rdflib import RDF
import markdown2
import cgi
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w')
logger = logging.getLogger(__name__)

RELPATH = os.path.dirname(os.path.abspath(__file__))

#NIDM_ROOT = os.path.dirname(RELPATH)
NIDM_ROOT = os.path.abspath(os.path.join(RELPATH ,'..', '..', '..', '..'))
DOC_FOLDER = os.path.join(NIDM_ROOT, 'doc', 'content', 'specs', 'nidm_html')
INCLUDE_FOLDER = os.path.join(DOC_FOLDER, 'include')

#NIDM_EXPE_PATH = os.path.dirname(RELPATH)
NIDM_EXPE_PATH = os.path.abspath(os.path.join(RELPATH ,'..', '..'))
IMPORTS_FOLDER = os.path.abspath(os.path.join(NIDM_EXPE_PATH ,'imports'))
TERMS_FOLDER = os.path.join(NIDM_EXPE_PATH, 'terms')

RELEASED_TERMS_FOLDER = os.path.join(TERMS_FOLDER, 'releases')

class OwlNidmHtml:
    def __init__(self, owl_file, import_files, spec_name, subcomponents=None,
                 used_by=None, generated_by=None, derived_from=None,
                 attributed_to=None, prefix=None, commentable=False,
                 intro=None, term_prefix=None):
        self.owl = OwlReader(owl_file, import_files)
        self.owl.graph.bind('owl', 'http://www.w3.org/2002/07/owl#')
        self.owl.graph.bind('dct', 'http://purl.org/dc/terms/')
        self.owl.graph.bind('dicom', 'http://purl.org/nidash/dicom#')
        self.owl.graph.bind('nidm', 'http://purl.org/nidash/nidm#')
        self.owl.graph.bind('bids', 'http://purl.org/nidash/bids#')
        self.owl.graph.bind('onli', 'http://neurolog.unice.fr/ontoneurolog/v3.0/instrument.owl#')
        self.owl.graph.bind('pato', 'http://purl.obolibrary.org/obo/pato#')
        self.owl.graph.bind('prov', 'http://www.w3.org/ns/prov')
        self.owl.graph.bind('qibo', 'http://www.owl-ontologies.com/Ontology1298855822.owl')
        self.owl.graph.bind('sio', 'http://semanticscience.org/resource/')
        self.name = spec_name
        self.component = self.name.lower().replace("-", "_")
        self.section_open = 0
        self.already_defined_classes = list()
        self.commentable = commentable
        self.term_prefix = term_prefix
        #self.classes = self.split_process(owl_file)
        self.prefix = prefix

        self.attributes_done = set()
        self.text = ""
        self.create_specification(subcomponents, used_by, generated_by,
                                  derived_from, attributed_to, prefix, intro)
    
    def create_specification(self, subcomponents, used_by, generated_by,
                             derived_from, attributed_to, prefix, intro=None):
        self.create_title(self.name+": Types and relations", "definitions")

        self.text += "<a href='#classes'>Classes</a>"
        if self.has_type_entries(OWL['DatatypeProperty']):
            self.text += " | <a href='#datatypeproperties'>Datatype Properties</a>"
        if self.has_type_entries(OWL['AnnotationProperty']):
            self.text += " | <a href='#annotationproperties'>Annotation Properties</a>"
        if self.has_type_entries(OWL['ObjectProperty']):
            self.text += " | <a href='#objectproperties'>Object Properties</a>"
        if self.has_type_entries(OWL['NamedIndividual']):
            self.text += " | <a href='#namedindividuals'>Named Individuals</a>"

        if intro is not None:
            self.text += intro
        
        #table_num = 3
        #if self.term_prefix == "nidm":
        classes = self.owl.get_classes(prefix=prefix, but=self.already_defined_classes)
        #for classes in self.classes:
        #print("CLASS: "+classes)
        classes_by_types = self.owl.get_class_names_by_prov_type(
            classes, prefix=prefix, but=self.already_defined_classes)
        # for x in classes:
        #     print(x)
        self.already_defined_classes += classes

        #self.create_subcomponent_table(classes_by_types, table_num,
        #                               subcomponent_name)
        #table_num = table_num + 1
        all_classes = \
            classes_by_types[PROV['Activity']] + \
            classes_by_types[PROV['Entity']] + \
            classes_by_types[PROV['Agent']] + \
            classes_by_types[None]

        self.text += "<h1 id='classes'>Classes</h1>"

        for class_uri in all_classes:
            # uncomment this to see uri before processing
            # print(class_uri)
            self.create_class_section(
                class_uri,
                self.owl.get_definition(class_uri),
                self.owl.attributes.setdefault(class_uri, None),
                used_by, generated_by, derived_from, attributed_to,
                children=not (
                    self.owl.get_prov_class(class_uri) == PROV['Entity']))
        
        self.add_type_section(OWL['DatatypeProperty'], used_by, generated_by, derived_from, attributed_to)
        self.add_type_section(OWL['AnnotationProperty'], used_by, generated_by, derived_from, attributed_to)
        self.add_type_section(OWL['ObjectProperty'], used_by, generated_by, derived_from, attributed_to)
        self.add_type_section(OWL['NamedIndividual'], used_by, generated_by, derived_from, attributed_to)

        #if subcomponent_name:
        #    self.text += """
        #</section>"""

        self.close_sections()

    def add_type_section(self, rdf_type, used_by, generated_by, derived_from, attributed_to):
        entries = self.get_type_entries(rdf_type)
        
        if entries:
            if rdf_type == OWL['DatatypeProperty']:
                self.text += "<h1 id='datatypeproperties'>Datatype Properties</h1>"
            elif rdf_type == OWL['AnnotationProperty']:
                self.text += "<h1 id='annotationproperties'>Annotation Properties</h1>"
            elif rdf_type == OWL['ObjectProperty']:
                self.text += "<h1 id='objectproperties'>Object Properties</h1>"
            elif rdf_type == OWL['NamedIndividual']:
                self.text += "<h1 id='namedindividuals'>Named Individuals</h1>"

            for entry in entries:
                # print(entry)
                self.create_class_section(
                    entry,
                    self.owl.get_definition(entry),
                    self.owl.attributes.setdefault(entry, None),
                    used_by, generated_by, derived_from, attributed_to,
                    children=not (
                        self.owl.get_prov_class(entry) == PROV['Entity']))
    
    def get_type_entries(self, rdf_type):
        entries = self.owl.all_of_rdf_type(rdf_type, but_type=OWL['Class'])
        if entries:
            filtered = list()
            for entry in entries:
                pre = self.owl.get_label(entry).split(":")[0]
                if pre.lower() == self.term_prefix:
                    filtered.append(entry)
            if filtered:
                return filtered
        return False
    
    def has_type_entries(self, rdf_type):
        entries = self.owl.all_of_rdf_type(rdf_type, but_type=OWL['Class'])
        if entries:
            for entry in entries:
                pre = self.owl.get_label(entry).split(":")[0]
                if pre.lower() == self.term_prefix:
                    return True
        return False

    def create_subcomponent_table(self, classes, table_num,
                                  subcomponent_name=None):
        if subcomponent_name:
            self.text += """
        <section><h1>"""+subcomponent_name+"""</h1>"""
            # Check if there is a header file to include here
            fname = os.path.join(
                INCLUDE_FOLDER,
                self.component+"_" +
                subcomponent_name.split(" ")[0].lower()+".html")
            if os.path.isfile(fname):
                fid = open(fname, "r")
                self.text += fid.read()
                fid.close()

        else:
            subcomponent_name = ""

        # Did not find how to handle table numbering and ids with Respec as we
        # did for figures?
        table_id = "prov-mapping-"""+subcomponent_name.lower()
        self.text += """
        <div style="text-align: left;">
            <table class="thinborder">
                <caption id=\""""+table_id+"""\">
                    <a class="internalDFN" href=\"#"""+table_id+"""\">Table """+str(table_num)+"""</a>:"""+self.name+subcomponent_name + """ Concepts
                </caption>
                <tbody>
                    <tr>
                        <th align="center"><b>"""+self.name+""" Concept</b></th>
                        <th align="center"><b>PROV type</b></th>
                        <th align="center"><b>Identifier</b></th>
                    </tr>
        """

        self.text += """
        <!-- HERE ------------- Beginning of PROV Entities ------------- -->
        """

        for prov_class in list([
                PROV['Activity'],
                PROV['Entity'],
                PROV['Agent']]):
            sorted_classes = classes[prov_class]
            for class_uri in sorted_classes:
                self.text += """
                        <tr>
                            <td>"""+self.term_link(class_uri)+"""
                            </td>
                    """

                # First iteration
                if class_uri is sorted_classes[0]:
                    self.text += """
                                <td rowspan=\""""+str(len(sorted_classes)) + \
                        """\" style="text-align: center;"> """ + \
                        self.owl.get_label(prov_class) + \
                        """</td>
                        """

                self.text += """
                                <td>"""+self.owl.graph.qname(class_uri) + \
                             """</td>
                            </tr>
                """

        self.text += """
                </tbody>
                </table>
            </div>"""
    
    def create_title(self, title, id=None):

        #print "into create_title"

        if id is None:
            self.text += """
        <section>
        """
        else:
            self.text += """
        <section id=\""""+id+"""\">
        """
        self.text += """
            <h1>"""+title+"""</h1>
        """
        self.section_open += 1
    
    def _format_markdown(self, text):

        #print "into _format_markdown"

        # Replace links specified in markdown by html
        text = markdown2.markdown(text).replace("<p>", "").replace("</p>", "")
        # Remove trailing new line
        text = text[0:-1]
        return text

    def format_definition(self, definition):

        #print "into format_definition"

        # Capitalize first letter, format markdown and end with dot
        if definition:
            definition = definition[0].upper() + definition[1:]
            definition = self._format_markdown(definition)
            definition += "."

        return definition

    def linked_listing(self, uri_list, prefix="", suffix="", sort=True):

        #print "into linked_listing"

        linked_listing = prefix

        if sort:
            uri_list = self.owl.sorted_by_labels(uri_list)

        for i, uri in enumerate(uri_list):
            if i == 0:
                sep = ""
            elif i == len(uri_list):
                sep = " and "
            else:
                sep = ", "
            linked_listing += sep+self.term_link(uri)

        return linked_listing+suffix

    def term_link(self, term_uri, tag="a", text=None):
        href = ""
        if self.owl.is_external_namespace(term_uri):
            href = " href =\""+str(term_uri)+"\""
        else: #target link fix
            term_uri_prefix = self.owl.get_label(term_uri).split(":")[0]
            if term_uri.startswith(self.prefix):
                href = " href =\"#"+self.owl.get_name(term_uri).lower()+"\""
            else:
                html_file = term_uri_prefix+".html"
                if term_uri_prefix == "nidm":
                    html_file = "index.html"
                href = " href =\"./"+html_file+"#"+self.owl.get_name(term_uri).lower()+"\""
        
        if text is None:
            text = self.owl.get_label(term_uri)

        term_link = "<" + tag + " title=\"" + self.owl.get_name(term_uri) + \
                    "\"" + href + ">" + text+"</"+tag+">"

        if tag is "dfn":
            issue_url = "https://github.com/incf-nidash/nidm/issues"

            # Add link to current definition
            term_link = self.term_link(term_uri, text=term_link)

            if self.commentable:
                term_link = term_link + \
                    " <a href=\""+issue_url+"?&q=is%3Aopen+'" + text + \
                    "'\"\"><sup>&#9734;</sup></a>" + \
                    "<a href=\""+issue_url+"/new\";\"><sup>+</sup></a>"

        return term_link

    def create_class_section(self, class_uri, definition, attributes,
                             used_by=None, generated_by=None,
                             derived_from=None, attributed_to=None,
                             children=False,
                             is_range=False):
        class_label = self.owl.get_label(class_uri)
        class_name = self.owl.get_name(class_uri)
        definition = self.format_definition(definition)
        
        if (not self.owl.get_label(class_uri).startswith(self.term_prefix.lower()+':')):
            return
            
        self.text += """
            <!-- """+class_label+""" ("""+class_name+""")"""+""" -->
            <section id=\""""+class_name.lower()+"""\">
                <h2 label=\""""+class_name+"""\">"""+class_label+"""</h2>
                <div class="glossary-ref">
                    """+self.term_link(class_uri, "dfn") + ": " + definition

        self.text += "<p>"+self.term_link(class_uri)+" is"

        nidm_class = self.owl.get_nidm_parent(class_uri)
        if nidm_class:
            #print(self.term_prefix+"-n: "+nidm_class)
            self.text += " a "+self.term_link(nidm_class)
        else:
            prov_class = self.owl.get_prov_class(class_uri)
            if prov_class:
                #print(self.term_prefix+": "+prov_class)
                self.text += " a "+self.term_link(prov_class)
            else:
                #look in NIDM file
                nidm_file = os.path.join(TERMS_FOLDER, 'nidm-experiment.owl')
                nidm_owl = OwlReader(nidm_file)
                nidm_subclass = self.get_nidm_subclass(class_uri, nidm_owl)
                if nidm_subclass:
                    self.text += " a "+self.term_link(nidm_subclass)
                else:
                    subprop = self.get_subprop(class_uri)
                    if subprop:
                        self.text += " a "+self.term_link(subprop)
                    else:
                        nidm_subprop = self.get_nidm_subprop(class_uri, nidm_owl)
                        if nidm_subprop:
                            self.text += " a "+self.term_link(nidm_subprop)
                        else:
                            types = list(self.owl.graph.objects(class_uri, RDF['type']))
                            if len(types) > 1 and OWL['NamedIndividual'] in types:
                                types.remove(OWL['NamedIndividual'])
                            if types:
                                self.text += " a "+self.term_link(types[0])
                                if len(types) > 1:
                                    for itype in types[1:]:
                                        self.text += ", "+self.term_link(itype)

        found_used_by = False
        if used_by:
            if class_uri in used_by:
                self.text += self.linked_listing(used_by[class_uri],
                                                 " used by ")
                found_used_by = True
            used_entities = list()

            for used_entity, used_activities in used_by.items():
                for used_act in used_activities:
                    if used_act == class_uri:
                        used_entities.append(used_entity)
            if used_entities:
                self.text += self.linked_listing(used_entities,
                                                 " that uses ",
                                                 " entities")

        found_attr_to = False
        if attributed_to:
            if class_uri in attributed_to:
                if found_used_by:
                    self.text += " and "
                self.text += self.linked_listing(attributed_to[class_uri],
                                                 " attributed to ")
                found_attr_to = True

        found_generated_by = False
        if generated_by:
            if class_uri in generated_by:
                if found_used_by or found_generated_by:
                    self.text += " and "

                self.text += self.linked_listing(
                    list([generated_by[class_uri]]), " generated by ")

                found_generated_by = True

            if class_uri in generated_by.values():
                generated_entities = list()
                for generated_entity, generated_act in generated_by.items():
                    if generated_act == class_uri:
                        generated_entities.append(generated_entity)

                if generated_entities:
                    self.text += self.linked_listing(
                        generated_entities,
                        ". This activity generates ", " entities")

        if derived_from:
            if class_uri in derived_from:
                if found_used_by or found_generated_by or found_attr_to:
                    self.text += " and "

                self.text += self.linked_listing(
                    list([derived_from[class_uri]]), " derived from ")

        class_children = self.owl.get_direct_children(class_uri)
        if class_children:
            if found_used_by or found_generated_by or found_attr_to:
                self.text += ". It "
            else:
                self.text += " and "
            self.text += " has the following child"
            if len(class_children) > 1:
                self.text += "ren"
            self.text += ": " + \
                         self.linked_listing(class_children)

        self.text += "."
        self.text += "</p>"

        curation = self.owl.get_curation_status(class_uri)
        note = self.owl.get_editor_note(class_uri)
        range_value = self.owl.get_range(class_uri)
        domain = self.owl.get_domain(class_uri)
        same = self.owl.get_same_as(class_uri)
        indiv_types = list(self.owl.graph.objects(class_uri, RDF['type']))

        editor = list(self.owl.graph.objects(class_uri, OBO_TERM_EDITOR))
        if editor:
            if len(editor) > 1:
                logger.warning('Multiple editors for '
                              + self.owl.get_label(class_uri) + ': '
                              + ",".join(editor))
            editor = editor[0]
        else:
            editor = ""

        if indiv_types:
            try:
                self.text += "<p>Type: "
                if self.owl.is_named_individual(class_uri):
                    self.text += self.term_link(OWL['NamedIndividual'])
                else:
                    self.text += self.term_link(indiv_types[0])
                    if len(indiv_types) > 1:
                        for itype in indiv_types[1:]:
                            self.text += ", "+self.term_link(itype)
                self.text+"</p>"
            except:
                logger.warning("URI invalid for: "+class_uri)
        if range_value:
            self.text += "<p>Range: "+range_value+"</p>"
        if domain:
            self.text += "<p>Domain: "+domain+"</p>"
        if same:
            self.text += "<p>Same as: "+self.term_link(same)+"</p>"
        if curation:
            self.text += "<p>Curation Status: "+self.term_link(curation)+"</p>"
        if editor:
            try:
                self.text += "<p>Editor: "+self.term_link(editor)+"</p>"
            except:
                logger.warning("URI invalid for: "+editor)
                self.text += "<p>Editor: "+editor
        if note:
            self.text += "<p>Editor Note: "+note+"</p>"
        

        range_classes = list()

        self.text += """
                </div>"""

        if attributes and (attributes != set([CRYPTO['sha512']])):
            self.text += """
                <p></p>
                <div class="attributes" id="attributes-"""+class_label + \
                """"> A """ + \
                self.term_link(class_uri)+""" has attributes:
                <ul>
                    <li><span class="attribute" id=\"""" + \
                class_label+""".label">rdfs:label</span>: \
                    (<em class="rfc2119" title="OPTIONAL">OPTIONAL</em>) """\
            """Human readable description of the """ + \
                self.term_link(class_uri)+""".</li>"""

            for att in sorted(attributes):

                # Do not display prov relations as attributes
                # (except prov:atLocation...)
                if not self.owl.is_prov(att) or (att == PROV['atLocation']):
                    if att not in self.attributes_done:
                        # First definition of this attribute
                        att_tag = "dfn"
                    else:
                        att_tag = "a"

                    self.attributes_done.add(att)
                    # if att_label.startswith("nidm:"):
                    att_def = self.owl.get_definition(att)
                    self.text += """
                        <li>"""+self.term_link(att, att_tag) + \
                        '</span>: (<em class="rfc2119" title="OPTIONAL">' + \
                        'OPTIONAL</em>) ' + self.format_definition(att_def)

                    if att in self.owl.parent_ranges:
                        child_ranges = list()
                        for parent_range in self.owl.parent_ranges[att]:
                            child_ranges += self.owl.get_direct_children(
                                parent_range)
                            if self.owl.get_label(parent_range).\
                                    startswith('nidm'):
                                range_classes.append(parent_range)
                        child_ranges = sorted(child_ranges)

                        # if nidm_namespace:
                        child_range_txt = ""
                        if child_ranges:
                            # Get all child ranges
                            child_range_txt = self.linked_listing(
                                child_ranges, " such as ")

                        self.text += self.linked_listing(
                            self.owl.parent_ranges[att],
                            " (range ", child_range_txt+")")
                        self.text += "."

                        self.text += "</li>"

            self.text += """
                </ul>
                </div>"""

        BASE_REPOSITORY = "https://raw.githubusercontent.com/" + \
            "incf-nidash/nidm/master/"
        for title, example in self.owl.get_example(class_uri, BASE_REPOSITORY):
            self.text += """
                </ul>
                </div>
                <pre class='example highlight' title=\""""+title+"""\">""" + \
                cgi.escape(example) + """</pre>"""

        # For object property list also children (in sub-sections)
        if children:
            direct_children = self.owl.sorted_by_labels(
                self.owl.get_direct_children(class_uri))
            for child in direct_children:
                if not child in self.already_defined_classes:
                    self.create_class_section(
                        child,
                        self.owl.get_definition(child),
                        self.owl.attributes.setdefault(child, None),
                        children=True)
                    self.already_defined_classes.append(child)

        # Display individuals
        individuals = self.owl.sorted_by_labels(
            self.owl.get_individuals(class_uri))
        if individuals:
            self.text += \
                " Examples of "+self.term_link(class_uri)+" includes " + \
                "<ul>"

            for indiv in individuals:
                self.text += "<li>" + self.term_link(indiv, "dfn") + ": " + \
                             self.format_definition(
                                 self.owl.get_definition(indiv)) + \
                             "</li>"

            self.text += "</ul>"

        if is_range:
            self.text += """
                </section>"""

        for range_name in self.owl.sorted_by_labels(range_classes):
            if not range_name in self.already_defined_classes:
                self.already_defined_classes.append(range_name)
                self.create_class_section(
                    range_name,
                    self.owl.get_definition(range_name),
                    self.owl.attributes.setdefault(range_name, None),
                    children=True, is_range=True)

        if not is_range:
            self.text += """
            </section>"""

    def close_sections(self):

        #print "into close_sections"
        tabs = ""
        for x in range(0, self.section_open):
            tabs += "\t"

        for x in range(0, self.section_open):
            self.text += "\n"+tabs+"</section>\n"

    def get_nidm_subclass(self, class_uri, nidm_owl):
        nidm_subclasses = nidm_owl.get_direct_parents(class_uri)
        for nidm_subclass in nidm_subclasses:
            return nidm_subclass
        return False
    
    def get_subprop(self, prop_uri):
        for parent in self.owl.graph.objects(prop_uri, RDFS['subPropertyOf']):
            return parent
        return False

    def get_nidm_subprop(self, prop_uri, nidm_owl):
        for parent in nidm_owl.graph.objects(prop_uri, RDFS['subPropertyOf']):
            return parent
        return False

    # Write out specification
    def write_specification(self, spec_file="index.html", component=None,
                            version=None):
        if spec_file == "index.html":
            spec_file = os.path.join(DOC_FOLDER, "index.html")
        spec_open = codecs.open(spec_file, 'w', "utf-8")
        spec_open.write(self.text)
        spec_open.close()

    def _header_footer(self, prev_file=None, intro_file=None, follow_file=None, component=None,
                       version=None, term=None):

        #print "into _header_footer"

        release_notes = None
        
        if component:
            prev_file1 = os.path.join(INCLUDE_FOLDER, "head1.html")
            if not os.path.isfile(prev_file1):
                prev_file1 = os.path.join(INCLUDE_FOLDER, "head1.html")
            prev_file2 = os.path.join(INCLUDE_FOLDER, "head2.html")
            if not os.path.isfile(prev_file2):
                prev_file2 = os.path.join(INCLUDE_FOLDER, "head2.html")
            prev_file3 = os.path.join(INCLUDE_FOLDER, "head3.html")
            if not os.path.isfile(prev_file3):
                prev_file3 = os.path.join(INCLUDE_FOLDER, "head3.html")

            if term == "nidm":
                intro_file = os.path.join(INCLUDE_FOLDER, "intro.html")
                if not os.path.isfile(intro_file):
                    intro_file = os.path.join(INCLUDE_FOLDER, "intro.html")

            follow_file = os.path.join(INCLUDE_FOLDER, "foot.html")
            if not os.path.isfile(follow_file):
                follow_file = os.path.join(INCLUDE_FOLDER, "foot.html")

            if version:
                release_notes = os.path.join(os.path.dirname(self.owl.file), "notes.html")
                if not os.path.isfile(release_notes):
                    release_notes = None

        
        start_text = ""
        if prev_file1 is not None:
            prev_file_open1 = open(prev_file1, 'r')
            start_text = start_text+prev_file_open1.read().decode('utf-8')
            prev_file_open1.close()
        title = term.upper()
        if title == "NIDM":
            title = "NIDM-Experiment"
        start_text = start_text+"<title>"+title+"</title>\n"
        if prev_file2 is not None:
            prev_file_open2 = open(prev_file2, 'r')
            start_text = start_text+prev_file_open2.read().decode('utf-8')
            prev_file_open2.close()
        
        project_name = "<h1 class=\"project-name\">"+title+"</h1>\n"
        start_text = start_text+project_name
        if prev_file3 is not None:
            prev_file_open3 = open(prev_file3, 'r')
            start_text = start_text+prev_file_open3.read().decode('utf-8')
            prev_file_open3.close()

        if intro_file is not None:
            intro_file_open = open(intro_file, 'r')
            start_text = start_text+intro_file_open.read().decode('utf-8')
            intro_file_open.close()
        
        self.text = start_text+self.text

        if release_notes is not None:
            release_note_open = open(release_notes, 'r')
            self.text = self.text+release_note_open.read()
            release_note_open.close()

        if follow_file is not None:
            if term is "nidm":
                self.text = self.text+"</section>"
            follow_file_open = open(follow_file, 'r')
            self.text = self.text+follow_file_open.read()
            follow_file_open.close()

    # def split_process(self, owl_file):
    #     f = open(owl_file, "r")
    #     lines = f.readlines()
    #     f.close()
        
    #     classes = []
    #     for x in lines:
    #         x = x.strip()
    #         if x != "" and x[0] != "#" and x[0] != "@" and x[0] != "[":
    #             if "owl:Class" not in x:
    #                 continue
    #             #print(x)
    #             x = shlex.split(x)
    #             subject = x[0]
    #             if subject not in classes:
    #                 classes.append(subject)

    #     return classes

def owl_process(file, imports, spec_name, prefix, term_prefix):
    spec_file = None
    if term_prefix == "nidm":
        spec_file = os.path.join(DOC_FOLDER, "index.html")
    else:
        spec_file = os.path.join(DOC_FOLDER, term_prefix+".html")

    nidm_original_version = "dev"
    nidm_version = 'dev'

    used_by = {}
    generated_by = {}
    derived_from = {}
    subcomponents = {}
    owlspec = OwlNidmHtml(file, imports, spec_name, prefix=prefix, term_prefix=term_prefix)
    
    if not nidm_version == "dev":
        owlspec.text = owlspec.text.replace("(under development)", nidm_original_version)
        owlspec.text = owlspec.text.replace("img/", "img/nidm-results_"+nidm_version+"/") #where versions are included
    
    component_name = spec_name.lower()
    #if term_prefix == "nidm":
    owlspec._header_footer(component=component_name, version=nidm_version, term=term_prefix)
    owlspec.write_specification(spec_file=spec_file, component=component_name, version=nidm_version)


def main():
    if len(sys.argv) > 1:
        nidm_original_version = sys.argv[1]
        nidm_version = nidm_original_version.replace(".", "")
    else:
        nidm_original_version = "dev"
        nidm_version = 'dev'

    # Retrieve owl file for NIDM-Results
    if nidm_version == "dev":
        owl_file = os.path.join(TERMS_FOLDER, 'nidm-experiment.owl')
        import_files = glob.glob(os.path.join(TERMS_FOLDER, "imports", '*.ttl'))
    else:
        owl_file = os.path.join(RELEASED_TERMS_FOLDER, \
            'nidm-experiment_'+nidm_version+'.owl')
        # For released version of the ontology imports are embedded
        import_files = None

    # check the file exists
    assert os.path.exists(owl_file)

    # Add manually used and wasDerivedFrom because these are not stored in the
    # owl file (no relations yet!)
    subcomponents = {}
    used_by = {}
    generated_by = {}
    derived_from = {}

    owlspec = OwlNidmHtml(owl_file, import_files, "NIDM-Experiment", subcomponents, used_by, generated_by, derived_from, prefix=str(NIDM), term_prefix="nidm")
    
    if not nidm_version == "dev":
        owlspec.text = owlspec.text.replace("(under development)", nidm_original_version)
        owlspec.text = owlspec.text.replace("img/", "img/nidm-results_"+nidm_version+"/") #where versions are included

    component_name = "nidm-experiment"
    owlspec._header_footer(component=component_name, version=nidm_version, term="nidm")
    owlspec.write_specification(component=component_name, version=nidm_version)

    
    owl_file = os.path.join(IMPORTS_FOLDER, 'bids_import.ttl')
    owl_process(owl_file, None, "BIDS", prefix=str(BIDS), term_prefix="bids")
    
    owl_file = os.path.join(IMPORTS_FOLDER, 'dicom_import.ttl')
    owl_process(owl_file, None, "DICOM", prefix=str(DICOM), term_prefix="dicom")

    owl_file = os.path.join(IMPORTS_FOLDER, 'sio_import.ttl')
    owl_process(owl_file, None, "SIO", prefix=str(SIO), term_prefix="sio")
    
    owl_file = os.path.join(IMPORTS_FOLDER, 'obo_import.ttl')
    owl_process(owl_file, None, "OBO", prefix=str(OBO), term_prefix="obo")

    owl_file = os.path.join(IMPORTS_FOLDER, 'ontoneurolog_instruments_import.ttl')
    owl_process(owl_file, None, "ONLI", prefix=str(ONLI), term_prefix="onli")

if __name__ == "__main__":
    main()
