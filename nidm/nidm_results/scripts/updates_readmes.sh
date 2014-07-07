#!/bin/sh
# For each document in the NIDM repository, this script checks if there is a public document with the same content (and title)
# in the Prov Store (https://provenance.ecs.soton.ac.uk/store). If there is none, the document is uploaded and its README file is updated
# to link to the json, turtle and svg serialisations. 

# To use this script you need to have an account on the Prov Store (cf. https://provenance.ecs.soton.ac.uk/store/account/signup/)

# Create a file named store_login_key.txt in the same directory including the following text: "mylogin:mykey" where mylogin 
# must be replaced by your Prov Store login and mykey by your ApiKey (cf. https://provenance.ecs.soton.ac.uk/store/account/developer/)
login_apikey=`cat store_login_key.txt`

update_readme () {
	cwd=$PWD

	cd $1 
	docname=$2 

	# Convert provn to json (Prov store API does not seem to accept provn?)
	jsondoc=`curl -s -L --data-binary @$docname.provn -H "Content-type: text/provenance-notation" \
		-H "Accept: application/json" https://provenance.ecs.soton.ac.uk/validator/provapi/documents/`

	doctitle="NIDM-Results: "$3

	# Get document(s) on prov store with same title
	samedocs=`curl -s -i "https://provenance.ecs.soton.ac.uk/store/api/v0/documents/?document_name__startswith=${doctitle}&document_name__endswith=${doctitle}&format=json"`
	samedocobjects=`echo $samedocs | sed -e 's/^.*"objects": \([^"]*\).*}$/\1/'`

	if [ "$samedocobjects" == "[]" ]; then
		echo "No document with same title in the Prov Store"
		samedoccontent=""
	else
		# Get uri and id of first doc with same title
		samedocuri=`echo $samedocs | sed -e 's/^.*"resource_uri": "\([^"]*\)",.*$/\1/'`
		samedocid=`echo $samedocs | sed -e 's/^.*"id": \([^"]*\),.*$/\1/'`
		
		# Get content of document with same title to check if identical with current doc
		samedoccontent=`curl -s https://provenance.ecs.soton.ac.uk/${samedocuri%?}.json \
				-H 'Content-Type: application/json'\
				-H 'Accept: application/json'`
	fi

	# Upload document to provstore
	output=`curl -s -i -X POST https://provenance.ecs.soton.ac.uk/store/api/v0/documents/ \
		-H 'Content-Type: application/json' -H "Authorization: ApiKey ${login_apikey}" \
		-d "{\"content\":${jsondoc},\"public\":true,\"rec_id\":\"${doctitle}\"}"`

	# Retreive document id
	docid=`echo $output | sed -e 's/^.*"id": \([^"]*\),.*$/\1/'`
	docuri=`echo $output | sed -e 's/^.*"resource_uri": "\([^"]*\)",.*$/\1/'`

	echo "docid: "$docid
	echo "samedocid: "$samedocid

	# Check if uploaded document is identical to previous version. If identical delete the just created document.
	# This cannot be done before the upload as we do not have access to the original file through the APIs.
	
	# Get content of the current document after upload to the prov store
	thisdoccontent=`curl -s https://provenance.ecs.soton.ac.uk/${docuri%?}.json \
			-H 'Content-Type: application/json'\
			-H 'Accept: application/json'`

	# FIXME: This is not functional as order does not seem to be preserved when uploading to prov store.
	# We will need to compare the graphs using rdflib (for example)
	if [ "$thisdoccontent" == "$samedoccontent" ]; then
	  	echo "Same as previous: delete just created document ({$docid}}"
	  	output=`curl -s -i -X DELETE https://provenance.ecs.soton.ac.uk/store/api/v0/documents/{$docid}/ \
			-H 'Content-Type: application/json' -H "Authorization: ApiKey ${login_apikey}"`
		docid=${samedocid}

	fi
	
	echo ${doctitle}": "${docid}

	# Update README
	readme=`cat ./README`
	echo "Alternative serialisations available at: https://provenance.ecs.soton.ac.uk/store/documents/${docid}/ \n \
	\n \
	json: https://provenance.ecs.soton.ac.uk/store/documents/${docid}.json \n \
	turtle: https://provenance.ecs.soton.ac.uk/store/documents/${docid}.ttl \n \
	svg graph: https://provenance.ecs.soton.ac.uk/store/documents/${docid}.svg" > README

	cd $cwd

   return 10
}


# Declare all documents that we want to upload
declare -a docnames=("spm_results" "example001_spm_results" "spm_results_2contrasts" "spm_results_conjunction" "spm_inference_activities" "fsl_results" "fsl_nidm") #
declare -a doctitles=("SPM" "SPM example 001" "SPM example 002" "SPM Conjunctions" "SPM Inference" "FSL" "FSL example 001") #
declare -a dirnames=("../spm" "../spm/example001" "../spm/example002" "../spm/example003" "../spm/example004" "../fsl" "../fsl/example001") #

# Upload each document and update README if needed
max=${#docnames[@]}
for i in `seq 1 $max`
do
    update_readme "${dirnames[$i-1]}" "${docnames[$i-1]}" "${doctitles[$i-1]}" 
done



