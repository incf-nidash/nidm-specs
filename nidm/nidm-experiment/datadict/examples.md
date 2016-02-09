## Data Dictionary and Element Examples

### NIMH Data Archive

```
<dataStructure>
<shortName>grit01</shortName>
<title>12-Item Grit Scale</title>
<sources>
<source>RDoC</source>
</sources>
<categories>
<category>Questionnaire</category>
</categories>
<dataType>Clinical Assessments</dataType>
<status>Published</status>
</dataStructure>

--

<dataType>Clinical Assessments</dataType>
<status>Published</status>
<dataElements>
<dataElement>
<required>Required</required>
<aliases />
<position>1</position>
<name>subjectkey</name>
<type>GUID, string, etc.</type>
<description>The NDAR Global Unique Identifier (GUID) for research subject</description>
<valueRange>NDAR*, M;F; T, etc.</valueRange>
<size>12</size>
<translations />
<notes>Required field</notes>
<translations />
</dataElement>
```

### REDCap

```
Variable / Field Name
Form Name
Section Header
Field Type
Field Label
"Choices, Calculations, OR Slider Labels"
Field Note
Text Validation Type OR Show Slider Number
Text Validation Min
Text Validation Max
Identifier?
Branching Logic (Show field only if...)
Required Field?
Custom Alignment
Question Number (surveys only)
Matrix Group Name
Matrix Ranking?
```
