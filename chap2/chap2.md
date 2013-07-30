Chapter 2
---

__Corpa__ = large amounts of text / linguistic data

NLTK contains many corpa

- __Project Gutenberg__

```
import nltk
nltk.corpus.gutenberg.fileids()
emma = nltk.Text(nltk.corpus.gutenberg.wrds('austin-emma.txt'))
emma.concordance("suprise")
```

To extract part of the documents:

*Raw text*, including everything (space, punctuation, etc.): `raw()`, as in `gutenberg.raw(fileid)`     
*All words*, space delimited: `words()`, as in `gutenberg.words(fileid)`       
*All sentences*: `sents()`, as in `gutenberg.sents(fileid)`


- __Web text__

```
from nltk.corpus import webtext
```


- __Chatroom conversations__ 

```
from nltk.corpus import nps_chat
```


- __Brown corpus__ -- first million-word electronic corpus in English    
-- Categorized by genre (news, editorial, etc.)      
-- Resource for studying systematic differences between genres -- a kind of linguistics called __stylistics__    
-- e.g. Compare genre's use of modal verbs

```
from ntk.corpus import brown
cfd = nltk.ConditionalFreqDist(
	(genre, word) 
	for genre in brown.catagories()
	for word in brown.words(catagories=genre))
genre = ['news', 'religion', 'hobbies']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples= modals)
```

-- The most frequent modal in news is "will" and the most frequent modal in romance is "could".   

- __Reuter's corpus__ -- 11,000 news documents. Classified in 90 topics. Groups into two sets: "training" and "test" (used to auto detect the topic of a document)
- __Inaugural address corpus__
- __Corpuses in different languages__

```
from nltk.cprpus inport udhr
langauges = ['German_Deutsch']
```

- __Loading your own corpus__

```
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
```

- __Basic Corpus Functionality Summary__ (more documentation available at `help(nltk.corpus.reader)`)  

<table>
	<tr>
		<td>Example</td>
		<td>Description</td>
	</tr>

	<tr>
		<td><pre>fileids()</pre></td>
		<td>the files of the corpus</td>
	</tr>

	<tr>
		<td><pre>fileids([categories])</pre></td>
		<td>the files of the corpus corresponding to these categories</td>
	</tr>

	<tr>
		<td><pre>categories()</pre></td>
		<td>the categories of the corpus</td>
	</tr>

	<tr>
		<td><pre>categories([fileids])</pre></td>
		<td>the categories of the corpus corresponding to these files</td>
	</tr>

	<tr>
		<td><pre>raw()</pre></td>
		<td>the raw content of the corpus</td>
	</tr>

	<tr>
		<td><pre>raw(fileids=[f1,f2,f3])</pre></td>
		<td>the raw content of the specified files</td>
	</tr>

	<tr>
		<td><pre>raw(categories=[c1,c2])</pre></td>
		<td>the raw content of the specified categories</td>
	</tr>
		
	<tr>
		<td><pre>words()</pre></td>
		<td>the words of the whole corpus</td>
	</tr>
	
	<tr>
		<td><pre>words(fileids=[f1,f2,f3])</pre></td>
		<td>the words of the specified fileids</td>
	</tr>
	
	<tr>
		<td><pre>fwords(categories=[c1,c2])</pre></td>
		<td>the words of the specified categories</td>
	</tr>

	<tr>
		<td><pre>sents()</pre></td>
		<td>the sentences of the whole corpus</td>
	</tr>

	<tr>
		<td><pre>sents(fileids=[f1,f2,f3])</pre></td>
		<td>the sentences of the specified fileids</td>
	</tr>

	<tr>
		<td><pre>sents(categories=[c1,c2])</pre></td>
		<td>the sentences of the specified categories</td>
	</tr>

	<tr>
		<td><pre>abspath(fileid)</pre></td>
		<td>the location of the given file on disk</td>
	</tr>

	<tr>
		<td><pre>encoding(fileid)</pre></td>
		<td>the encoding of the file (if known)</td>
	</tr>

	<tr>
		<td><pre>open(fileid)</pre></td>
		<td>open a stream for reading the given corpus file</td>
	</tr>

	<tr>
		<td><pre>root()</pre></td>
		<td>the path to the root of locally installed corpus</td>
	</tr>

	<tr>
		<td><pre>readme()</pre></td>
		<td>the contents of the README file of the corpus</td>
	</tr>
</table>


__Conditional frequency distributions__ = collection of frequency distributions, each for a different condition (e.g. a category)

Generating random text with bigrams:

```
def generate_model(cfdist, word, num=15):
	for i in range(num):
		print word, 
		word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
print cdf['living']
generate-model(cfd, 'living')
```   

- __Functions defined for conditional frequency distributions__:

<table>
	<tr>
		<td>Example</td>
		<td>Description</td>
	</tr>

	<tr>
		<td><pre>cfdist = ConditionalFreqDist(pairs)</pre></td>
		<td>create a conditional frequency distribution from a list of pairs</td>
	</tr>

	<tr>
		<td><pre>cfdist.conditions()</pre></td>
		<td>alphabetically sorted list of conditions</td>
	</tr>

	<tr>
		<td><pre>cfdist[condition]</pre></td>
		<td>the frequency distribution for this condition</td>
	</tr>

	<tr>
		<td><pre>cfdist[condition][sample]</pre></td>
		<td>frequency for the given sample for this condition</td>
	</tr>

	<tr>
		<td><pre>cfdist.tabulate()</pre></td>
		<td>tabulate the conditional frequency distribution</td>
	</tr>

	<tr>
		<td><pre>cfdist.tabulate(samples, conditions)</pre></td>
		<td>tabulation limited to the specified samples and conditions</td>
	</tr>

	<tr>
		<td><pre>cfdist.plot()</pre></td>
		<td>graphical plot of the conditional frequency distribution</td>
	</tr>
		
	<tr>
		<td><pre>cfdist.plot(samples, conditions)</pre></td>
		<td>graphical plot limited to the specified samples and conditions</td>
	</tr>

	<tr>
		<td><pre>cfdist1 &lt; cfdist2</pre></td>
		<td>test if samples in cfdist1 occur less frequently than in cfdist2</td>
	</tr>
</table>


Lexical Resources

__Lexicon__ = a collection of words and/or phrases along with associated info, such as part-of-speech and sense definitions

__Lexical entry__ = consists of a __headword__ (aka a __lemma__) and additional info such as (part of speech and sense).

__Homonyms__ = two distinct words having the same spelling

__stopwords__ = high-frequency, English plumbing words (the, is, to)s
```
from nltk.corpus import stopwords
stopwords.words('english')
```
English names:
```
names = nltk.corpus.names
female_names = names.words('female.txt')
```
Pronouncian dictionary
```
entries = nltk.corpus.cmudict.entries()
syllable = ['N', 'IHO', 'K', 'S']
[word for word, pron in entries if pron[-4:] == syllable]
```

__WordNet__ = semantically oriented English dictionary (righer than a regular thesaurus)
```
from nltk.corpus import wordnet as wn
wn.synsets('motorcar').lemma_names
```

__hyponyms__ = more specific concepts
````
motorcar = wn.snset('car.n.01')
types_of_motorcar = motorcar.hyponyms
```
__hypernyms__ = less specific concepts

__root hypernyms__ = least specific concept on tree

__lexical relations__ = relate one synset to another (e.g. hypernyms and hyponyms)

You can use lexical relations to determine __semantic similarity__ (how closely two words are related)