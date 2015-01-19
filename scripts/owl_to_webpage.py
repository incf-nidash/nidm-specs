
import codecs
from OwlReader import OwlReader
from Constants import *

class OwlSpecification(object):

    def __init__(self, owl_file, spec_name, components=None, used_by=None, 
        generated_by=None, derived_from=None):
        self.owl = OwlReader(owl_file)
        self.name = spec_name
        self.section_open = 0

        self.attributes_done = set()

        self.text = ""
        self.create_specification(components, used_by, generated_by, 
            derived_from)

    def create_specification(self, components, used_by, generated_by,
        derived_from):
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
                    self.owl.attributes.setdefault(class_name, None),
                    used_by, generated_by, derived_from)

            if component_name:
                self.text += """
            </section>"""

        self.close_sections()

    def create_component_table(self, classes, component_name=None):
        if component_name:
            self.text += """
        <section><h1>"""+component_name+"""</h1>"""
            # Check if there is a header file to include here
            fname = os.path.join(INCLUDE_FOLDER, \
                "nidm-results_"+component_name.split(" ")[0].lower()+".html")
            if os.path.isfile(fname):
                fid = open(fname, "r")
                self.text += fid.read()
                fid.close()

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
                            <td><a title=\""""+class_qname+"""\">"""+class_qname+"""</a>
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

    def format_definition(self, definition):
        # Lower case first letter of definition
        if definition:
            definition = definition[0].lower() + definition[1:]

        # Add a dot a the end of the definition
        if definition[-1:] is not ".":
            definition += "."

        return definition

    def create_class_section(self, class_name, definition, attributes, used_by, 
        generated_by, derived_from):
        class_qname = self.owl.graph.qname(class_name)

        definition = self.format_definition(definition)
       
        self.text += """
            <!-- """+class_qname+""" -->
            <section id="section-"""+class_qname+""""> 
                <h1 label=\""""+class_qname+"""\">"""+class_qname+"""</h1>
                <div class="glossary-ref">
                    A <dfn>"""+class_qname+"""</dfn>\
                    <sup><a title=\""""+class_qname+"""\">\
                    <span class="diamond">&#9826;</span></a></sup> is """+definition

        self.text += " <a>"+class_qname+"</a> is a "+\
                    self.owl.graph.qname(self.owl.get_prov_class(class_name))

        found_used_by = False
        if used_by:
            if class_name in used_by:

                if len(used_by[class_name]) >= 2:
                    self.text += \
                        " used by <a>"+"</a>, <a>".join(map(self.owl.graph.qname, \
                        sorted(used_by[class_name])[:-1]))+"</a> and <a>"+\
                        self.owl.graph.qname(sorted(used_by[class_name])[-1])+\
                        "</a>"
                else:
                    self.text += \
                        " used by <a>"+self.owl.graph.qname(used_by[class_name][0])+\
                        "</a>"
                found_used_by = True
            used_entities = list()
            for used_entity, used_activities in used_by.items():
                for used_act in used_activities:
                    if used_act == class_name:
                        used_entities.append(used_entity)
            if used_entities:
                self.text += " that uses <a>"+"</a>, <a>".join(map(self.owl.graph.qname, \
                        sorted(used_entities)[:-1]))+"</a> and <a>"+\
                        self.owl.graph.qname(sorted(used_entities)[-1])+\
                        "</a> entities"
        found_generated_by = False
        if generated_by:
            if class_name in generated_by:
                if found_used_by:
                    self.text += " and "

                self.text += """ generated by <a>"""+\
                        self.owl.graph.qname(generated_by[class_name])+"""</a>"""
                found_generated_by = True

            if class_name in generated_by.values():
                generated_entities = list()
                for generated_entity, generated_act in generated_by.items():
                    if generated_act == class_name:
                        generated_entities.append(generated_entity)

                if generated_entities:
                    self.text += ". This activity generates <a>"+\
                    "</a>, <a>".join(map(self.owl.graph.qname, \
                    sorted(generated_entities)[:-1]))+\
                    "</a> and <a>"+self.owl.graph.qname(sorted(generated_entities)[-1])+\
                            "</a> entities"

        if derived_from:
            if class_name in derived_from:
                if found_used_by or found_generated_by:
                    self.text += " and "

                self.text += """ derived from <a>"""+\
                        self.owl.graph.qname(derived_from[class_name])+"""</a>"""

        self.text +="."

        
        self.text += """ 
                </div>
                <p></p>
                <div class="attributes" id="attributes-"""+class_qname+""""> A """+\
                """<a>"""+class_qname+"""</a> has attributes:
                <ul>
                    <li><span class="attribute" id=\""""+\
                    class_qname+""".label">prov:label</span>: an \
                    <em class="rfc2119" title="OPTIONAL">OPTIONAL</em> human readable description \
                    of the """+class_qname+""".</li>
                    """

        if attributes:
            for att in sorted(attributes):
                att_name = self.owl.graph.qname(att)

                if att not in self.attributes_done:
                    # First definition of this attribute
                    att_tag = "dfn" 
                else:
                    att_tag = "a" 

                if att_name[0:5] == "nidm:":
                    att_def = self.owl.get_definition(att)
                    self.text += """ 
                        <li><span class="attribute" id=\""""+class_qname+"""."""+att_name+"""">
                        <"""+att_tag+""">"""+att_name+"""</"""+att_tag+""">
                        </span>: an <em class="rfc2119" title="OPTIONAL">OPTIONAL</em> """+\
                        self.format_definition(att_def)

                    if att in self.owl.ranges:
                        self.text += " (range "+", ".join(map(self.owl.graph.qname, \
                            sorted(self.owl.ranges[att])))+")"

                    self.text += "</li>"

                self.attributes_done.add(att)

        BASE_REPOSITORY = "https://raw.githubusercontent.com/incf-nidash/nidm/master/"
        examples = self.owl.get_example(class_name, BASE_REPOSITORY)
        for example in sorted(examples):
            self.text += """        
                </ul>
                </div>
                <pre class='example highlight'>"""+example+"""</pre>"""

        self.text += """  
            </section>"""

    def close_sections(self):
        for x in range(0, self.section_open):
            self.text += "\t"*x+"</section>\n"

    # Write out specification
    def write_specification(self, spec_file):
        spec_open = codecs.open(spec_file, 'w', "utf-8")
        spec_open.write(self.text)
        spec_open.close()

    def _header_footer(self, prev_file=None, follow_file=None):
        if prev_file:
                prev_file_open = open(prev_file, 'r')
                self.text = prev_file_open.read().decode('utf-8')+self.text
                prev_file_open.close()
        if follow_file:
            follow_file_open = open(follow_file, 'r')
            self.text = self.text+follow_file_open.read()
            follow_file_open.close()