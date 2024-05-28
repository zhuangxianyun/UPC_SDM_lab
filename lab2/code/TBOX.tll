from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDFS, RDF, XSD

# Create a Graph
graph = Graph()

# Create many URIRefs in the same namespace, i.e. URIs with the same prefix
LAB = Namespace("http://SDM_LAB2.org/")

# Bind the lab namespace to a prefix for more readable output
graph.bind('lab',LAB)


# --------------------- 1) Paper Super Class --------------------------- #
graph.add((LAB.Paper, RDF.type, RDFS.Class))
graph.add((LAB.Paper, RDFS.label, Literal("Paper")))

graph.add((LAB.hasKeywords, RDF.type, RDF.Property))
graph.add((LAB.hasKeywords, RDFS.domain, LAB.Paper))
graph.add((LAB.hasKeywords, RDFS.range, XSD.string))
graph.add((LAB.hasKeywords, RDFS.label, Literal("hasKeywords")))


graph.add((LAB.hasReview, RDF.type, RDF.Property))
graph.add((LAB.hasReview, RDFS.domain, LAB.Paper))
graph.add((LAB.hasReview, RDFS.range, LAB.Review))
graph.add((LAB.hasReview, RDFS.label, Literal("hasReview")))


# SubClasses of Paper
# 1.1) Article
graph.add((LAB.Article, RDF.type, RDFS.Class))
graph.add((LAB.Article, RDFS.subClassOf, LAB.Paper))
graph.add((LAB.Article, RDFS.label, Literal("Article")))

# 1.2) Erratum
graph.add((LAB.Erratum, RDF.type, RDFS.Class))
graph.add((LAB.Erratum, RDFS.subClassOf, LAB.Paper))
graph.add((LAB.Erratum, RDFS.label, Literal("Erratum")))

# 1.3) Conferencepaper
graph.add((LAB.Conferencepaper, RDF.type, RDFS.Class))
graph.add((LAB.Conferencepaper, RDFS.subClassOf, LAB.Paper))
graph.add((LAB.Conferencepaper, RDFS.label, Literal("Conferencepaper")))

# 1.4) Letter
graph.add((LAB.Letter, RDF.type, RDFS.Class))
graph.add((LAB.Letter, RDFS.subClassOf, LAB.Paper))
graph.add((LAB.Letter, RDFS.label, Literal("Letter")))


# Adding some additional attributes for Paper Concept
# 1) Title
graph.add((LAB.Title, RDF.type, RDF.Property))
graph.add((LAB.Title, RDFS.domain, LAB.Paper))
graph.add((LAB.Title, RDFS.range, XSD.string))
graph.add((LAB.Title, RDFS.label, Literal("Title")))

# 2) Abstract
graph.add((LAB.Abstract, RDF.type, RDF.Property))
graph.add((LAB.Abstract, RDFS.domain, LAB.Paper))
graph.add((LAB.Abstract, RDFS.range, XSD.string))
graph.add((LAB.Abstract, RDFS.label, Literal("Abstract")))

# 3) isIndexedin
graph.add((LAB.isIndexedin, RDF.type, RDF.Property))
graph.add((LAB.isIndexedin, RDFS.domain, LAB.Paper))
graph.add((LAB.isIndexedin, RDFS.range, LAB.Journal))
graph.add((LAB.isIndexedin, RDFS.label, Literal("isIndexedin")))


# 4) isPublishedin
graph.add((LAB.isPublishedin, RDF.type, RDF.Property))
graph.add((LAB.isPublishedin, RDFS.domain, LAB.Paper))
graph.add((LAB.isPublishedin, RDFS.range, LAB.Conference))
graph.add((LAB.isPublishedin, RDFS.label, Literal("isPublishedin")))


# --------------------- 2) Person Super Class --------------------------- #
graph.add((LAB.Person, RDF.type, RDFS.Class))
graph.add((LAB.Person, RDFS.label, Literal("Person")))

# Subclasses of Person
# 2.1) Author
graph.add((LAB.Author, RDF.type, RDFS.Class))
graph.add((LAB.Author, RDFS.subClassOf, LAB.Person))
graph.add((LAB.Author, RDFS.label, Literal("Author")))

# Adding some extra properties for Author Concept
graph.add((LAB.authorName, RDF.type, RDF.Property))
graph.add((LAB.authorName, RDFS.domain, LAB.Author))
graph.add((LAB.authorName, RDFS.range, XSD.string))
graph.add((LAB.authorName, RDFS.label, Literal("authorName")))

graph.add((LAB.writes, RDF.type, RDF.Property))
graph.add((LAB.writes, RDFS.domain, LAB.Author))
graph.add((LAB.writes, RDFS.range, LAB.Paper))
graph.add((LAB.writes, RDFS.label, Literal("writes")))

# 2.2) Reviewer
graph.add((LAB.Reviewer, RDF.type, RDFS.Class))
graph.add((LAB.Reviewer, RDFS.subClassOf, LAB.Person))
graph.add((LAB.Reviewer, RDFS.label, Literal("Reviewer")))


# --------------------- 3) Venue Super Class --------------------------- #
graph.add((LAB.Venue, RDF.type, RDFS.Class))
graph.add((LAB.Venue, RDFS.label, Literal("Venue")))

# SubClasses of Venue
# 3.1) Journal
graph.add((LAB.Journal, RDF.type, RDFS.Class))
graph.add((LAB.Journal, RDFS.subClassOf, LAB.Venue))
graph.add((LAB.Journal, RDFS.label, Literal("Journal")))

# Adding properties for journal
graph.add((LAB.journalTitle, RDF.type, RDF.Property))
graph.add((LAB.journalTitle, RDFS.domain, LAB.Journal))
graph.add((LAB.journalTitle, RDFS.range, XSD.string))
graph.add((LAB.journalTitle, RDFS.label, Literal("journalTitle")))

graph.add((LAB.hasVolume, RDF.type, RDF.Property))
graph.add((LAB.hasVolume, RDFS.domain, LAB.Journal))
graph.add((LAB.hasVolume, RDFS.range, LAB.Volume))
graph.add((LAB.hasVolume, RDFS.label, Literal("hasVolume")))

# 3.2) Conference
graph.add((LAB.Conference, RDF.type, RDFS.Class))
graph.add((LAB.Conference, RDFS.subClassOf, LAB.Venue))
graph.add((LAB.Conference, RDFS.label, Literal("Conference")))

# Adding properties for conference
graph.add((LAB.conferenceTitle, RDF.type, RDF.Property))
graph.add((LAB.conferenceTitle, RDFS.domain, LAB.Conference))
graph.add((LAB.conferenceTitle, RDFS.range, XSD.string))
graph.add((LAB.conferenceTitle, RDFS.label, Literal("conferenceTitle")))

graph.add((LAB.isPartOf, RDF.type, RDF.Property))
graph.add((LAB.isPartOf, RDFS.domain, LAB.Conference))
graph.add((LAB.isPartOf, RDFS.range, LAB.Proceedings))
graph.add((LAB.isPartOf, RDFS.label, Literal("isPartOf")))

# --------------------- 4) Proceedings Super Class --------------------------- #
graph.add((LAB.Proceedings, RDF.type, RDFS.Class))
graph.add((LAB.Proceedings, RDFS.label, Literal("Proceedings")))

# Adding properties for proceedings
graph.add((LAB.proceedingName, RDF.type, RDF.Property))
graph.add((LAB.proceedingName, RDFS.domain, LAB.Proceedings))
graph.add((LAB.proceedingName, RDFS.range, XSD.string))
graph.add((LAB.proceedingName, RDFS.label, Literal("proceedingName")))

graph.add((LAB.proceedingYear, RDF.type, RDF.Property))
graph.add((LAB.proceedingYear, RDFS.domain, LAB.Proceedings))
graph.add((LAB.proceedingYear, RDFS.range, XSD.int))
graph.add((LAB.proceedingYear, RDFS.label, Literal("proceedingYear")))

# --------------------- 5) Volume Super Class --------------------------- #
graph.add((LAB.Volume, RDF.type, RDFS.Class))
graph.add((LAB.Volume, RDFS.label, Literal("Volume")))

# Adding properties for volume
graph.add((LAB.volumeName, RDF.type, RDF.Property))
graph.add((LAB.volumeName, RDFS.domain, LAB.Volume))
graph.add((LAB.volumeName, RDFS.range, XSD.string))
graph.add((LAB.volumeName, RDFS.label, Literal("volumeName")))

graph.add((LAB.volumeYear, RDF.type, RDF.Property))
graph.add((LAB.volumeYear, RDFS.domain, LAB.Volume))
graph.add((LAB.volumeYear, RDFS.range, XSD.int))
graph.add((LAB.volumeYear, RDFS.label, Literal("volumeYear")))

print(graph.serialize(format="turtle"))
