#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom
import urllib2
import prov.model as prov
from uuid import uuid1

dcterms = prov.Namespace("dcterms", "http://purl.org/dc/terms/")
xsd = prov.Namespace("xsd", "http://www.w3.org/2001/XMLSchema#")
cml = prov.Namespace("cml", "http://www.connectomics.org/cff-2/")
nidm = prov.Namespace("nidm", "http://www.incf.org/ns/nidash/fs#")

# uuid method
get_id = lambda: uuid1().hex


def cff2provn(filename):
    """Parse cml xml file and return a prov bundle object"""
    #filename = "/Users/fariba/Desktop/UCI/freesurfer/scripts/meta-MC-SCA-023_tp1.cml"
    tree = xml.dom.minidom.parse(filename)
    collections = tree.documentElement

    g = prov.ProvBundle()
    g.add_namespace(xsd)
    g.add_namespace(dcterms)
    g.add_namespace(cml)

    url_entity = g.entity(cml[get_id()])
    url_entity.add_extra_attributes({prov.PROV['type']: nidm['nidm:ConnectomeFileFormat'],
                                     prov.PROV['location']: prov.Literal(filename, prov.XSD['String'])})

    cml_collection = g.collection(cml[get_id()])
    cml_collection.add_extra_attributes(
        {prov.PROV['type']: cml['connectome'],
         prov.PROV['label']: filename})
    g.wasDerivedFrom(cml_collection, url_entity)

    # get species, subject_name, and subject_timepoint
    species = tree.getElementsByTagName('cml:species')[0].toxml()
    species = species.replace('<cml:species>', '').replace('</cml:species>', '')

    tp = ''
    sub = ''
    tags = collections.getElementsByTagName("cml:tag")
    for t in tags:
        if t.attributes['key'].value == 'subject_name':
            sub = t.toxml()
        if t.attributes['key'].value == 'subject_timepoint':
            tp = t.toxml()
    sub = sub.replace('<cml:tag key="subject_name">', '').replace('</cml:tag>', '')
    tp = tp.replace('<cml:tag key="subject_timepoint">', '').replace('</cml:tag>', '')
    #print species + " " + sub + " " + tp

    cml_meta = g.entity(cml[get_id()])
    cml_meta.add_extra_attributes(
        {prov.PROV['type']: cml['connectome-meta'], cml['species']: species, cml['timepoint']: tp,
         cml['subject_name']: sub})
    g.hadMember(cml_collection, cml_meta)

    volumes = collections.getElementsByTagName("cml:connectome-volume")
    c = 0
    for v in volumes:
        c = c + 1
        #print v.getAttribute("src") + " " + v.getAttribute("dtype") + " " + v.getAttribute("name") + " " + v.getAttribute("fileformat")
        #print v.attributes['fileformat'].value
        dtype = v.getAttribute('dtype')
        src = v.getAttribute('src')
        name = v.getAttribute('name')
        fileformat = v.getAttribute('fileformat')
        cml_volume = g.entity(cml[get_id()])
        cml_volume.add_extra_attributes(
            {prov.PROV['type']: cml['connectome-volume'], cml['dtype']: dtype, cml['src']: src, cml['name']: name,
             cml['fileformat']: fileformat})
        g.hadMember(cml_collection, cml_volume)

    tracks = collections.getElementsByTagName("cml:connectome-track")
    c = 0
    for t in tracks:
        c = c + 1
        #print t.getAttribute("src") + " " + t.getAttribute("dtype") + " " + t.getAttribute("name") + " " + t.getAttribute("fileformat")
        dtype = t.getAttribute('dtype')
        src = t.getAttribute('src')
        name = t.getAttribute('name')
        fileformat = t.getAttribute('fileformat')
        cml_track = g.entity(cml[get_id()])
        cml_track.add_extra_attributes(
            {prov.PROV['type']: cml['connectome-track'], cml['dtype']: dtype, cml['src']: src, cml['name']: name,
             cml['fileformat']: fileformat})
        g.hadMember(cml_collection, cml_track)

    networks = collections.getElementsByTagName("cml:connectome-network")
    c = 0
    for n in networks:
        c = c + 1
        #print n.getAttribute("src") + " " + n.getAttribute("dtype") + " " + n.getAttribute("name") + " " + n.getAttribute("fileformat")
        dtype = n.getAttribute('dtype')
        src = n.getAttribute('src')
        name = n.getAttribute('name')
        fileformat = n.getAttribute('fileformat')
        cml_network = g.entity(cml[get_id()])
        cml_network.add_extra_attributes(
            {prov.PROV['type']: cml['connectome-network'], cml['dtype']: dtype, cml['src']: src, cml['name']: name,
             cml['fileformat']: fileformat})
        g.hadMember(cml_collection, cml_network)

    surfaces = collections.getElementsByTagName("cml:connectome-surface")
    c = 0
    for s in surfaces:
        c = c + 1
        #print s.getAttribute("src") + " " + s.getAttribute("dtype") + " " + s.getAttribute("name") + " " + s.getAttribute("fileformat")
        dtype = s.getAttribute('dtype')
        src = s.getAttribute('src')
        name = s.getAttribute('name')
        fileformat = s.getAttribute('fileformat')
        cml_surface = g.entity(cml[get_id()])
        cml_surface.add_extra_attributes(
            {prov.PROV['type']: cml['connectome-surface'], cml['dtype']: dtype, cml['src']: src, cml['name']: name,
             cml['fileformat']: fileformat})
        g.hadMember(cml_collection, cml_surface)

    data = collections.getElementsByTagName("cml:connectome-data")
    c = 0
    for d in data:
        c = c + 1
        #print d.getAttribute("src") + " " + d.getAttribute("dtype") + " " + d.getAttribute("name") + " " + d.getAttribute("fileformat")
        dtype = d.getAttribute('dtype')
        src = d.getAttribute('src')
        name = d.getAttribute('name')
        cml_data = g.entity(cml[get_id()])
        cml_data.add_extra_attributes(
            {prov.PROV['type']: cml['connectome-data'], cml['dtype']: dtype, cml['src']: src, cml['name']: name,
             cml['fileformat']: fileformat})
        g.hadMember(cml_collection, cml_data)

    return g


def main(args=None):
    import os
    # gather args
    filename = args.meta_file
    project_id = args.project_id
    output_dir = args.output_dir
    outformat = args.format

    # process cff file
    g = cff2provn(filename)

    # print or write file
    if outformat == "provn":
        out = g.get_provn()
        ext = ".provn"
    elif outformat == "turtle":
        out = g.rdf().serialize(format='turtle')
        ext = ".ttl"
    elif outformat == "xml":
        out = g.rdf().serialize(format='xml')
        ext = ".xml"

    if output_dir:
        outfilename = os.path.join(os.path.abspath(output_dir), project_id)
        outfilename_ext = ''.join([outfilename, ext])
        with open(outfilename_ext, 'wt') as fp:
            fp.write(out)
    else:
        print out


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(prog='cff2provn.py', description=__doc__)
    parser.add_argument('-m', '--meta_file', type=str, required=True,
                        help='Path to meta.cml file')
    parser.add_argument('-p', '--project_id', type=str, required=True,
                        help='Project tag to use for the generated prov files')
    parser.add_argument('-o', '--output_dir', type=str,
                        help='Output directory')
    parser.add_argument('-f', '--format', type=str, default="turtle", choices=["provn", "turtle", "xml"],
                        help='Output format')
    args = parser.parse_args()

    sys.exit(main(args=args))