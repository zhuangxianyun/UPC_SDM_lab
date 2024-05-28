!pip install rdflib
#ABox
# Importing necessary libraries and modules
import pandas as pd
import random
from rdflib.namespace import RDF, RDFS, FOAF, XSD, URIRef
from rdflib import Graph
import pandas as pd
from rdflib import Namespace

# Importing required files
authorsDF = pd.read_csv('/kaggle/working/authors.csv')
authorsPapersDF = pd.read_csv('/kaggle/working/authorsPapers.csv')
conferencesDF = pd.read_csv('/kaggle/working/conferences.csv')
conferenceProceedingsDF = pd.read_csv('/kaggle/working/conferenceProceedings.csv')
journalsDF = pd.read_csv('/kaggle/working/journals.csv')
journalVolumesDF = pd.read_csv('/kaggle/working/journalVolumes.csv')
papersDF = pd.read_csv('/kaggle/working/papers.csv')
proceedingsDF = pd.read_csv('/kaggle/working/proceedings.csv')
volumesDF = pd.read_csv('/kaggle/working/volumes.csv')
submittedPapersDF = pd.read_csv('/kaggle/working/submittedPapers.csv')
keywordPapersDF = pd.read_csv('/kaggle/working/keywordPapers.csv')

# Creating a graph
g = Graph()
# Create many URIRefs in the same namespace, i.e. URIs with the same prefix
LAB = Namespace("http://SDM_LAB2.org/")
# Bind the lab namespace to a prefix for more readable output
g.bind('lab',LAB)

# Adding author--[writes]--> paper instances to the graph
g.add((LAB.Author, LAB.writes, LAB.Paper))   
for k in range(len(authorsPapersDF['authorId'])):
    g.add((URIRef(LAB+authorsPapersDF['authorId'][k]), LAB.writes, URIRef(LAB+authorsPapersDF['paperId'][k])))
    g.add((URIRef(LAB+authorsPapersDF['authorId'][k]), RDF.type, LAB.Author))
    ptype = authorsPapersDF['paperType'][k]
    if ptype == "Letter":
        g.add((URIRef(LAB+authorsPapersDF['paperId'][k]), RDF.type, LAB.Letter))
    elif ptype == "Article":
        g.add((URIRef(LAB+authorsPapersDF['paperId'][k]), RDF.type, LAB.Article))
    elif ptype == "Conference paper":
        g.add((URIRef(LAB+authorsPapersDF['paperId'][k]), RDF.type, LAB.Conferencepaper))
    elif ptype == "Erratum":
        g.add((URIRef(LAB+authorsPapersDF['paperId'][k]), RDF.type, LAB.Erratum))


# Adding conference--[isPartOf]--> proceedings instances to the graph
g.add((LAB.Conference, LAB.isPartOf, LAB.Proceedings))
for k in range(len(conferenceProceedingsDF['conferenceId'])):
    g.add((URIRef(LAB+conferenceProceedingsDF['conferenceId'][k]), LAB.isPartOf, URIRef(LAB+conferenceProceedingsDF['conferenceProceedingIds'][k])))

# Adding journal--[hasVolume]--> volume instances to the graph
g.add((LAB.Journal, LAB.hasVolume, LAB.Volume))
for k in range(len(journalVolumesDF['journalId'])):
    g.add((URIRef(LAB+journalVolumesDF['journalId'][k]), LAB.hasVolume, URIRef(LAB+journalVolumesDF['journalVolumeIds'][k])))

# Paper -- [paperTitle] --> String 
# Adding Paper -- [paperTitle] --> String instances to the graph
g.add((LAB.Paper, LAB.paperTitle, XSD.string))
for k in range(len(papersDF['paperId'])):
    g.add((URIRef(LAB+papersDF['paperId'][k]), LAB.paperTitle, Literal(papersDF['paperTitle'][k])))

# Paper -- [paperAbstract] --> String
# Adding Paper -- [paperAbstract] --> String instances to the graph
g.add((LAB.Paper, LAB.paperAbstract, XSD.string))
for k in range(len(papersDF['paperId'])):
    g.add((URIRef(LAB+papersDF['paperId'][k]), LAB.paperAbstract, Literal(papersDF['paperAbstract'][k])))

# Author -- [authorName] --> String 
# Adding Paper -- [authorName] --> String instances to the graph
g.add((LAB.Author, LAB.authorName, XSD.string))
for k in range(len(authorsDF['authorId'])):
    g.add((URIRef(LAB+authorsDF['authorId'][k]), LAB.authorName, Literal(authorsDF['authorName'][k])))

# Adding Paper -- [isPublishedin] --> Conference instances to the graph
g.add((LAB.Paper, LAB.isPublishedin, LAB.Conference))   
for k in range(len(submittedPapersDF['paperId'])):
    pbelongto = submittedPapersDF['conferenceJournalId'][k]
    if pbelongto and pbelongto.startswith('con'):
        g.add((URIRef(LAB+submittedPapersDF['paperId'][k]), LAB.isPublishedin, URIRef(LAB+submittedPapersDF['conferenceJournalId'][k])))

  # Paper -- [isIndexedin] --> Journal
# Adding Paper -- [isIndexedin] --> Journal instances to the graph
g.add((LAB.Paper, LAB.isIndexedin, LAB.Journal))   
for k in range(len(submittedPapersDF['paperId'])):
    pbelongto = submittedPapersDF['conferenceJournalId'][k]
    if pbelongto and pbelongto.startswith('jou'):
        g.add((URIRef(LAB+submittedPapersDF['paperId'][k]), LAB.isIndexedin, URIRef(LAB+submittedPapersDF['conferenceJournalId'][k])))

  # paper--[hasKeywords]--> String
# Adding paper--[hasKeywords]--> String instances to the graph
g.add((LAB.Paper, LAB.hasKeywords, XSD.string))
for k in range(len(keywordPapersDF['paperId'])):
    g.add((URIRef(LAB+keywordPapersDF['paperId'][k]), LAB.hasKeywords, Literal(keywordPapersDF['keyword'][k])))	

g.serialize('/kaggle/working/abox2.ttl',format = 'ttl')
