# Minutes from meeting 

## October 14th, 2013: Derived data call

When: 10/14/13, Time: 8-9am PDT, Join the conference call: Google hangout 

### Agenda:
(1) Neuroimaging Terms
(2) Data Modeling
(3) Minutes, wikis, blogs, google docs, google groups, etc.
    (a) ideas for simpler, integrated coordination of our work?

### Attendees:
1. Guillaume Flandin (GF)
2. Satrajit Gosh (SG)
3. David Keator (DK)
4. Camille Maumet (CM)
5. Nolan Nichols (NN)
6. Thomas Nichols (TN)
7. Jessica Turner (JT)
8. Jean-Bapiste Poline (JB)

### Minutes:

#### Neuroimaging Terms & Data Modeling

[Looking at the SPM minimal input/output tab in the Neuroimaging spreadsheet]

TN: The “threshold” term still needs to be sorted. The question when defining those terms is where the structure has to come as the structure impacts the way we define terms.

DK: If in SPM “height threshold” is consistent with a more general definition then we can use the general “threshold” term. This could be done through the use of synonyms (instead of using directly the general term) but this would be more work for the user.

SG: We had a discussion with Nolan about sub-graphs mapping within the model. For now, we should probably concentrate on terms mapping and later on we will think about sub-graph mapping.

DK: Have we covered everything needed by Guillaume? GF: The cluster size in resels is missing.

TN: Let’s add a term for that.

SG: In the output a 3D image is missing.

TN: In the outputs “Maximun intensity projection map”, “Surface with blob overlaid”, “2D plot”, we were unsure how these should be stored.

SG: Storing a 3D image would allow for more interactive visualisation.

TN: In the terms, what would “image” represent: a filepath, a nifty...

SG: The image could be an entity of type nifty file with an attribute location.

DK: All the information, such as the resolution, could then be retrieved from this file. In a first time, we want to focus on representing the meta-data and later on we will be able to think
about a new image format.

SG: Now, we try to build an object model (with link to SPM file) and a list of terms.
￼￼￼￼￼￼￼￼￼￼￼￼￼
DK: I was supposed to update fig. 1 of the SPM object model specification with the things that were on on the last call.

DK: Do you, Guillaume, have enough to start working with?

GF: About the NI-DM terms, do we agree on what they are now?

DK: Do we want to use SPM-specific terms and then defined them as synonyms later or to use directly the generic terms? 

SG: FSL will soon come in.

NN: Start with SPM terms and then general terms.

TN: Should we go ahead using Guillaume’s terms?

SG: Yes, Guillaume can add his terms to the representation and specify the link with the general NI-DM terms. For instance, an “spm peak FWE” is also an “NI-DM FWE”.

DK: What is important is to have a term for each entity. And to do the cross-software mapping we will need the synonyms. Now, we need an agreement on the structure. I will send out
another model and Guillaume can give us a beta version.

TN: To be clear, we need to speak about the graph.

DK: An overview of the model is in fig. 1 of the SPM object model specification.

SG: At the moment, the meta-data is missing.

DK: I will update the model for Wednesday and the corresponding code snippets. When we have that, Guillaume can use it right away.

TN: Does parser exist for this kind of structure?

SG: There are Java and Python bundles for PROV-N.

DK: Between PROV-N, RDF, JSON... we should find one which one is more usable and advise using it.

TN: What about Matlab?

SG: If there is a good JSON parser in Matlab then we should stick with that as JSON is the recommended option for the web.

GF: Initially, we were thinking about PROV-N.

TN: What is easier for you?

GF: From SPM point of view, creating an export function would be equally simple whatever the format we are using.

DK: The reason I do not like PROV-N is that it is not as widespread.

JB: Favouring RDF/JSON makes a lot of sense to facilitate the interaction with SPARQL.

NN: For readability, we could use RDF turtle (PROV-N is difficult to read); for application, one of the JSON implementations.

SG: On the JSON side, let’s use JSON-LD.

NN: For the one who are not familiar with JSON-LD, it is a serialization of RDF that looks like a regular JSON document.

GF: For SPM, JSON-LD is fine.

DK: JSON Pros: Can easily convert to other type of representation, existing parsers.... JSON Cons: Need a format (model). Though we can easily convert across format, we should choose one to avoid having different
file formats out of different software. We should agree on a “transport format”. What is the W3C doing?

SG: The W3C deals a lot with HTML/XML/Java. PROV-N is the most agnostic option but it is also the one with the least libraries available across tools.

JB: Would the next step be to get several of those document on the web (as examples). 

SG: JSON-LD to RDF is a 1 to 1 mapping.

DK: We should also work on the definition of SPM-specific terms. JT: We can reuse the NI-DM definition when appropriate.

DK: Let’s define synonyms instead.
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼
TN: We can reuse the definition in Guillaume’s spreadsheet.

JT: These need to be extended/updated.

TN: We can help Guillaume to do that.

JT: Being as specific as possible about what these terms are is the first step towards explaining what the software is doing to someone else.

SG: This will be useful later for reconciliation.

TN: What is the “Context” column?

JT: There was a time when this was useful (for instance for a “conversion” term that would help understanding which conversion we are talking about). [Decision is taken to delete the column] Minutes, wikis, blogs, Google docs, Google groups, ideas for simpler, integrated coordination of our work?

JB: We would need a higher level document to link to all these documents. A New Google doc? 

JT: I have a Google directory I can share. In fact, not so easy to share as we need everyone’s address (and sometimes there are
several per person).

TN: We would need some wiki page and a list of muntes.

JB: How about the INCF wiki?

DK: We currently have 2 wikis: the BIRN wiki (links to repository, old minutes, old documents sent before but the links are not up-to-date), the INCF wiki.

TN: If there is a lot there on the BIRN wiki we could stay there, on the other hand using the INCF wiki would give the action more credibility.

[DK shows the current BIRN wiki]

SG: We need to check that there will be no data loss if we go for the INCF wiki.

DK: We also need to move what is currently on the BIRN wiki. INCF wiki is probably easier to set the appropriate rights to edit/read the pages. SG: Yes, any INCF member can edit the INCF wiki.

#### Next steps

Terms:
- GF adds his SPM-specific terms in the NI-DM spreadsheet, update the definition, link with the general NI-DM terms (synonyms) with help from TN and CM.

Model:
- DK updates the data model object specification and the code snippets.
- TN lists the minimal inputs/ouputs for FSL. 

Coordination of our work:
- SG checks with INCF, the backup solution for the INCF wiki.

### Previous Minutes

- CM posts the minutes on the INCF wiki when backup is confirmed.
