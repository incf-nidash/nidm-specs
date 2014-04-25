from xml.dom.minidom import parse
import xml.dom.minidom
import urllib2
import prov.model as prov
from uuid import uuid1

dcterms = prov.Namespace("dcterms", "http://purl.org/dc/terms/")
xsd = prov.Namespace("xsd","http://www.w3.org/2001/XMLSchema#")
cff = prov.Namespace("cff", "http://www.connectomics.org/cff-2/")

# uuid method
get_id = lambda : uuid1().hex

# parse cff xml file
filename = "meta.cml"
tree = xml.dom.minidom.parse(filename)
collections = tree.documentElement

g = prov.ProvBundle()
g.add_namespace(xsd)
g.add_namespace(dcterms);
g.add_namespace("prov", "http://www.w3.org/ns/prov-o/")
g.add_namespace(cff)


url_entity = g.entity(cff[get_id()])
url_entity.add_extra_attributes({prov.PROV['type']: cff['cff_file'],
  prov.PROV['location']:prov.Literal(filename,prov.XSD['AnyURI'])})

cml_collection = g.collection(cff[get_id()])
cml_collection.add_extra_attributes({prov.PROV['type']: cff['tag_collection'],prov.PROV['label']:filename})
g.wasDerivedFrom(cml_collection,url_entity)

# get species, subject_name, and subject_timepoint
species = tree.getElementsByTagName('cml:species')[0].toxml()
species = species.replace('<cml:species>','').replace('</cml:species>','')

tp = ''
sub = ''
tags = collections.getElementsByTagName("cml:tag")
for t in tags:
  if t.attributes['key'].value == 'subject_name':
    sub = t.toxml()
  if t.attributes['key'].value == 'subject_timepoint':
    tp = t.toxml()
sub = sub.replace('<cml:tag key="subject_name">','').replace('</cml:tag>','')
tp = tp.replace('<cml:tag key="subject_timepoint">','').replace('</cml:tag>','')
print species + " " + sub + " " + tp

cml_meta = g.entity(cff[get_id()]);
cml_meta.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_meta_tag',cff['species']:species,cff['timepoint']:tp,cff['subject_name']:sub})
g.hadMember(cml_collection, cml_meta)

volumes = collections.getElementsByTagName("cml:connectome-volume")
c = 0
for v in volumes:
  c = c + 1
  print v.getAttribute("src") + " " + v.getAttribute("dtype") + " " + v.getAttribute("name") + " " + v.getAttribute("fileformat")
  #print v.attributes['fileformat'].value
  cml_volume = g.entity(cff[get_id()])
  cml_volume.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_volume_tag',cff['dtype']:v.getAttribute("dtype"),cff['src']:v.getAttribute("src"),cff['name']:v.getAttribute("name"),cff['fileformat']:v.getAttribute("fileformat")})
  g.hadMember(cml_collection,cml_volume)

tracks = collections.getElementsByTagName("cml:connectome-track")
c = 0
for t in tracks:
  c = c + 1
  print v.getAttribute("src") + " " + v.getAttribute("dtype") + " " + v.getAttribute("name") + " " + v.getAttribute("fileformat")
  cml_track = g.entity(cff[get_id()])
  cml_track.add_extra_attributes({prov.PROV['type']:'cff:cml_tag',prov.PROV['label']:'cml_track_tag',cff['dtype']:v.getAttribute("dtype"),cff['src']:v.getAttribute("src"),cff['name']:v.getAttribute("name"),cff['fileformat']:v.getAttribute("fileformat")})
  g.hadMember(cml_collection,cml_track)

provn = g.get_provn()
with open('cff-test.provn', 'wt') as fp:
  fp.writelines(provn)

g.rdf().serialize('cff-test.ttl', format='turtle')
g.rdf().serialize('cff-test.xml', format='xml')
exit()
