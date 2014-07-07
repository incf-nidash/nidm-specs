import requests
from bs4 import BeautifulSoup
import prov.model as prov

r = requests.get('https://raw.githubusercontent.com/joejimbo/HCLSDatasetDescriptions/master/Overview.html')
soup = BeautifulSoup(r.text)
table = soup.find('table')
codes = table.findChildren('code')
code_block = [codes[pos:pos + 2] for pos in xrange(0, len(codes), 2)]
ns_map = {code[0].text[:-1]: code[1].text for code in code_block}


# Access namespace objects as attributes
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self 

# create a prov bundle to store the graph
bundle = prov.ProvBundle()

# add namespaces to the bundle
for k, v in ns_map.iteritems():
    ns = prov.Namespace(k, v)
    bundle.add_namespace(ns)

ns = AttrDict(bundle._namespaces)

# Core Metadata
# property: [summary, version, distribution]
core_metadata = {ns.rdf['type']: ["MUST", "MUST", "MUST"],
                 ns.dct['title']: ["MUST", "MUST", "MUST"],
                 ns.dct['alternative']: ["MAY", "MAY", "MAY"],
                 ns.dct['description']: ["MUST", "MUST", "MUST"],
                 ns.dct['created']: ["NEVER", "SHOULD", "SHOULD"],
                 ns.pav['createdOn']: ["NEVER", "MAY", "MAY"],
                 ns.pav['authoredOn']: ["NEVER", "MAY", "MAY"],
                 ns.pav['curatedOn']: ["NEVER", "MAY", "MAY"],
                 ns.dct['creator']: ["NEVER", "MUST", "MUST"],
                 ns.dct['contributor']: ["NEVER", "MAY", "MAY"],
                 ns.pav['createdBy']: ["NEVER", "MAY", "MAY"],
                 ns.pav['authoredBy']: ["NEVER", "MAY", "MAY"],
                 ns.pav['curatedBy']: ["NEVER", "MAY", "MAY"],
                 ns.dct['issued']: ["NEVER", "SHOULD", "SHOULD"],
                 ns.dct['publisher']: ["MUST", "MUST", "MUST"],
                 ns.foaf['page']: ["SHOULD", "SHOULD", "SHOULD"],
                 ns.schemaorg['logo']: ["SHOULD", "SHOULD", "SHOULD"],
                 ns.dct['license']: ["MUST", "MUST", "MUST"],
                 ns.dct['rights']: ["MAY", "MAY", "MAY"],
                 ns.dct['language']: ["NEVER", "SHOULD", "SHOULD"],
                 ns.dcat['theme']: ["MAY", "MAY", "MAY"],
                 ns.dcat['keyword']: ["MAY", "MAY", "MAY"],
                 ns.void['vocabulary']: ["NEVER", "NEVER", "SHOULD"],
                 ns.dct['conformsTo']: ["NEVER", "MAY", "SHOULD"],
                 ns.cito['citesAsAuthority']: ["MAY", "MAY", "MAY"],
                 ns.dct['hasPart']: ["MAY", "MAY", "NEVER"],
                 ns.void['subset']: ["NEVER", "NEVER", "MAY"]}

core_summary = {k: v[0] for k, v in core_metadata.iteritems() if v[0] != "NEVER"}
core_version = {k: v[1] for k, v in core_metadata.iteritems() if v[1] != "NEVER"}
core_distribution = {k: v[2] for k, v in core_metadata.iteritems() if v[2] != "NEVER"}

identifiers = {ns.idot['preferredPrefix']: ["MAY", "MAY", "MAY"],
               ns.idot['alternatePrefix']: ["MAY", "MAY", "MAY"],
               ns.idot['identifierPattern']: ["NEVER", "NEVER", "MAY"],
               ns.void['uriRegexPattern']: ["NEVER", "NEVER", "MAY"],
               ns.idot['accessPattern']: ["MAY", "MAY", "MAY"],
               ns.idot['exampleIdentifier']: ["NEVER", "NEVER", "SHOULD"],
               ns.void['exampleResource']: ["NEVER", "NEVER", "SHOULD"]}

id_summary = {k: v[0] for k, v in identifiers.iteritems() if v[0] != "NEVER"}
id_version = {k: v[1] for k, v in identifiers.iteritems() if v[1] != "NEVER"}
id_distribution = {k: v[2] for k, v in identifiers.iteritems() if v[2] != "NEVER"}

provenance = {ns.void['inDataset']: ["NEVER", "NEVER", "SHOULD"],
              ns.pav['version']: ["NEVER", "MUST", "SHOULD"],
              ns.dct['isVersionOf']: ["NEVER", "MUST", "NEVER"],
              ns.pav['previousVersion']: ["NEVER", "SHOULD", "SHOULD"],
              ns.pav['hasCurrentVersion']: ["MAY", "NEVER", "NEVER"],
              ns.dct['source']: ["NEVER", "NEVER", "SHOULD"],
              ns.pav['retrievedFrom']: ["NEVER", "SHOULD", "SHOULD"],
              ns.prov['wasDerivedFrom']: ["NEVER", "SHOULD", "SHOULD"],
              ns.pav['createdWith']: ["NEVER", "NEVER", "MAY"],
              ns.dct['accrualPeriodicity']: ["SHOULD", "NEVER", "NEVER"]}

prov_summary = {k: v[0] for k, v in provenance.iteritems() if v[0] != "NEVER"}
prov_version = {k: v[1] for k, v in provenance.iteritems() if v[1] != "NEVER"}
prov_distribution = {k: v[2] for k, v in provenance.iteritems() if v[2] != "NEVER"}

availability = {ns.dct['format']: ["NEVER", "NEVER", "MUST"],
                ns.dcat['distribution']: ["NEVER", "SHOULD", "NEVER"],
                ns.dcat['accessURL']: ["MAY", "MAY", "MAY"],
                ns.dcat['downloadURL']: ["NEVER", "NEVER", "SHOULD"],
                ns.void['dataDump']: ["NEVER", "NEVER", "SHOULD"],
                ns.dcat['landingPage']: ["NEVER", "MAY", "MAY"]}

avail_summary = {k: v[0] for k, v in availability.iteritems() if v[0] != "NEVER"}
avail_version = {k: v[1] for k, v in availability.iteritems() if v[1] != "NEVER"}
avail_distribution = {k: v[2] for k, v in availability.iteritems() if v[2] != "NEVER"}

statistics = {ns.void['triples']: ["NEVER", "NEVER", "SHOULD"],
              ns.void['entities']: ["NEVER", "NEVER", "SHOULD"],
              ns.void['distinctSubjects']: ["NEVER", "NEVER", "SHOULD"],
              ns.void['properties']: ["NEVER", "NEVER", "SHOULD"],
              ns.void['distinctObjects']: ["NEVER", "NEVER", "SHOULD"],
              ns.sd['namedGraph']: ["NEVER", "NEVER", "SHOULD"],
              ns.void['propertyPartition']: ["NEVER", "NEVER", "MAY"],
              ns.void['classPartition']: ["NEVER", "NEVER", "MAY"],
              ns.void['subset']: ["NEVER", "NEVER", "MAY"]}

stats_summary = {k: v[0] for k, v in statistics.iteritems() if v[0] != "NEVER"}
stats_version = {k: v[1] for k, v in statistics.iteritems() if v[1] != "NEVER"}
stats_distribution = {k: v[2] for k, v in statistics.iteritems() if v[2] != "NEVER"}

all_properties = dict(core_metadata.items() + identifiers.items() + provenance.items() + availability.items() + statistics.items())

stats_summary = {k: v[0] for k, v in statistics.iteritems() if ["MUST", "SHOULD"] in v}

summary = [k.get_uri() for k, v in all_properties.iteritems() if "MUST" in v[0]]
version = [k.get_uri() for k, v in all_properties.iteritems() if "MUST" in v[1]]
distribution = [k.get_uri() for k, v in all_properties.iteritems() if "MUST" in v[2]]
