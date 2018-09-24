import rdflib as rl
import pyld as ld
import json

g = rl.ConjunctiveGraph()
g.parse(('https://raw.githubusercontent.com/incf-nidash/nidm-specs/master/nidm/nidm-results'
        '/spm/example001/example001_spm_results.ttl'), 
        format='turtle')
g2 = g.serialize(format='json-ld')

context = { "@context": "https://raw.githubusercontent.com/satra/nidm-jsonld/master/nidm-results.jsonld" }
foo = ld.jsonld.compact(json.loads(g2), context)
print(json.dumps(foo, indent=2))