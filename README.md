Notes From The NLTK Book ([http://nltk.org/book/](http://nltk.org/book/))
========
Juliana Nazaré - May 2013 - Artificial Intelligence Class    
Modified by Khoa Tran

Install Python and NLTK
---
- Install Setuptools: [http://pypi.python.org/pypi/setuptools](http://pypi.python.org/pypi/setuptools)
- Install Pip: run `sudo easy_install pip`
- Install Numpy and Matplotlib (optional - for graphical purpose): run `sudo pip install -U numpy`, `sudo apt-get install python-matplotlib`
- Install PyYAML and NLTK: run `sudo pip install -U pyyaml nltk`
- Test installation: run `python` then type `import nltk` into the REPL    

Chapter 1
---
__concordance__ = allows us to see the words in context. It can be used to observe the connotation that an author often uses with the word.
```
text1.concordance("monstrous")
```

__similar__ = allows us to see words used in similar contexts
```
text1.similar("monstrous")
```

__common contexts__ = examines just the contexts shared by 2+ words
```
text2.concordance(["monstrous", "very"])
```

__dispersion plot__ = positional information of a word within text

- each stripe on plot = an occurrence of the word


__generate__ = generates random text in the style of the text defined.
```
text3.generate()
```

__tokens__ = a sequence of characters representing a word or punctuation that we want to treat as a group.


__vocabulary__ = the set of tokens used in a text (duplicates are not counted)


__count__ = easily count up individual words in a text
```
text3.count("smote")
```

__lexical diversity__ = how diverse a body of text is (different words used)


__HOW DO WE IDENTIFY THE WORDS OF A TEXT THAT ARE MOST INFORMATIVE ABOUT  TOPIC?__

- Neither the very infrequent or very frequent words (common English plumbing) help.
- You want the words in the middle (they occur more than x times and less than y times e.g. 7)


__frequency distribution__ = the frequency of each vocabulry item in the text

```
fdist = FreqDist(text1)
vocabulary = fdist.keys()
fdist.plot(50, cumulative)
```

- __Functions defined for frequency distribution__:

<table>
	<tr>
		<td>Example</td>
		<td>Description</td>
	</tr>

	<tr>
		<td><pre>fdist = FreqDist(samples)</pre></td>
		<td>create a frequency distribution containing the given samples</td>
	</tr>

	<tr>
		<td><pre>fdist.inc(sample)</pre></td>
		<td>increment the count for this sample</td>
	</tr>

	<tr>
		<td><pre>fdist['monstrous']</pre></td>
		<td>count of the number of times a given sample occurred</td>
	</tr>

	<tr>
		<td><pre>fdist.freq('monstrous')</pre></td>
		<td>frequency of a given sample</td>
	</tr>

	<tr>
		<td><pre>fdist.N()</pre></td>
		<td>total number of samples</td>
	</tr>

	<tr>
		<td><pre>fdist.keys()</pre></td>
		<td>the samples sorted in order of decreasing frequency</td>
	</tr>

	<tr>
		<td><pre>for sample in fdist:</pre></td>
		<td>iterate over the samples, in order of decreasing frequency</td>
	</tr>
		
	<tr>
		<td><pre>fdist.max()</pre></td>
		<td>sample with the greatest count</td>
	</tr>
	
	<tr>
		<td><pre>fdist.tabulate()</pre></td>
		<td>tabulate the frequency distribution</td>
	</tr>
	
	<tr>
		<td><pre>fdist.plot()</pre></td>
		<td>graphical plot of the frequency distribution</td>
	</tr>

	<tr>
		<td><pre>fdist.plot(cumulative=True)</pre></td>
		<td>cumulative plot of the frequency distribution</td>
	</tr>

	<tr>
		<td><pre>fdist1 &lt; fdist2</pre></td>
		<td>test if samples in fdist1 occur less frequently than in fdist2</td>
	</tr>
</table>


__hapaxes__ = words that occur only once


__collocation__ = a series of words that appears together unusually often (e.g. red wine)


__bigrams__ = a list of word pairs
```
bigrams(['more', 'is', 'said', 'than', 'done'])
```
Essentially, collocations are frequent bigrams, except that we want to pay more attention to the cases that involve rare words.
```
text4.collocations()
```

__AUTOMATIC NATURAL LANGUAGE UNDERSTANDING__
Getting a computer to answer a "human" question automatically involves a lot of NLP:
- information extraction
- inference
- summarization
- scalable and robust

__Word sense disambiguation__ = work out which sense of a word was intended in a given context
e.g. 
- serve: help with food or drink; hold office; put ball into play
- dish: course of a meal, communications device

In the sentence "he served the dish", you can detect that serve and dish are being used with their food meanings.

A deeper kind of language understanding is needed to work out "who did what to whom" -- identifying subjects and objects of sentences.
e.g.

- The thieves stole the paintings. They were subsequently sold.
- The theives stole the paintings. They were subsequently caught.
- The thieves stole the paintings. They were subsequently found.

Figuring out "who did what to whom" involves finding the __antecedent__ of the pronoun "they" (thieves or paintings?)
NLP uses:

- __Anaphora resolution__ = identifying what a pronoun or noun phrase refers to
- __Semantic role labeling__ = identifying how a noun phrase relates to the verb (agent, patient, instrument, etc.)

__Machine translation__ = high-quality, idiomatic translation between two languages.
NLTK's MT = babelizer

```
>>> babelize.shell()
>>> How long are final exams?
>>> german
>>> run
```

How this works: given a document in English and German and a bilingual dictionary, we can automatically pair up the sentences in a method called __text alignment__. Once we have a million+ sentences, we can detect corresponding words and phrases and build a model that can be used to translate new text.

Spoken Dialog Systems:

__Turning test__ = can a dialog system, responding to a user's text input, perform so naturally that we cannot distinguish it from a human-generated response?


Chapter 2
---

__Corpa__ = large amounts of text / linguistic data

NLTK contains many corpa

- Project Gutenberg

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


- Web text

```
from nltk.corpus import webtext
```


- Chatroom conversations 

```
from nltk.corpus import nps_chat
```


- Brown corpus -- first million-word electronic corpus in English
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
- Reuter's corpus -- 11,000 news documents. Classified in 90 topics. Groups into two sets: "training" and "test" (used to auto detect the topic of a document)
- Inaugural address corpus
- Corpuses in different languages

```
from nltk.cprpus inport udhr
langauges = ['German_Deutsch']
```

- Loading your own corpus

```
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
```

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


Chapter 3
---

How to import text from the web:
```
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
```

Cleaning HTML:
```
url = "http://www.google.com"
html = urlopen(url).read()
raw = nltk.clean_html(html)
tokens = word_tokenize(raw)
text = nltk.Text(tokens)
txt.concordance('search')
```

The NLP Pipeline:
__HTML__ to __ASCII__
```
html = urlopen(url).read()
raw = nltk.clean_html(html)
```
__ASCII__ to __Text__
```
tokens = nltk.wordpunct_tokenize(raw)
text = nltk.Text(tokens)
```

__Text__ to __Vocab__
```
words = [w.lower() for w in text]
vocab = sorted(set(words))
```

__Regular expressions for detecting word patterns__
```
import re
[w for w in wordlist if re.search('ed$', w)]
```

__wildcard__ = '.' = symbol that matches any character

__textonyms__ = two or more words that are entered with the same sequence of keystokes (phones)
```
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
```
Operators:
- __+__ = one or more instances of the preceding item (closure)
- __[]__ = indicates a set
- __[-]__ = indicates a range
- __*__ = zero or more instances of the preceding item (closure)
- __^__ = matches any character that is not a vowel
- __r'__ = raw string (used for regular expressions)

Finding word stems:
```
def stem(word):
	for suffix in ['ing', 'ly', 'ed', 'ious', 'ive', 'es', 's', 'ment']:
		if word.endswith(suffix):
			return word[:-len(suffix)]
		return word
```
or
```
re.findall(r'^.*(ing|ly|ed|ious|ive|ies|es|s|ment)$', 'processing')
```
Stemmers:
```
porter = nltk.PorterStemmer()
[porter.stem(t) for t in tokens]
```

Lemmatization:
```
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]
```

Tokenization: uses regular expressions
```
re.split(r'[ \t\n]+', raw)
```

Chapter 4
---
Python basics -- skipped

Chapter 5: Categorizing and Tagging Words
---
__POS Tagger__ = processes a sequence of words and attaches a part of speech to each word
```
nltk.pos_tag(text)
```
- CC = coordinating conjunction
- RB = adverbs
- IN = preposition
- NN = noun
- NNP = noun proper
- JJ = adjective
- VBP = present-tense verb

Taggers help with generation of similar words, since you want to make sure they are the same part of speech.
- Tagged tokens often represented by tuples ('dog', 'NN')
- Can find out what type of works are most common in different catagories of text (e.g. news)

Nouns = used after a determiner or as the subject of a verb
- the __woman__ who I saw yesterday --> determiner
- the __woman__ sat down --> subject of a verb

Verbs = express a relation involving the referents of one or more noun phrases
- Rome __fell__ --> Simple
- Dot com stocks suddenly __fell__ like a stone --> with modifiers and adjuncts

Adjectives = describe nouns and used a modifiers (e.g. the large pizza) or predicates (e.g. the pizza is large)

Adverbs = modify verbs to specify the time, manner, place, or direction of the event described by the verb (e.g. the stocks fell __quickly__). They can also modify adjectives (e.g. Mary's teachers was __really__ nice.)

Articles = determiners (the, a)

Modals = (should, may)

Personal pronouns = (she, they)

Searching for 3-word phrases using POS tagging
```
from nltk.corpus import brown
def process(sentence):
	for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
		if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
			print w1, w2, w3

for tagged_sent in brown.tagged_sents():
	process(tagged_sent)
```

To create a POS-tagger:
- Default tag everything w/ most common POS (NN)
- Use a regular expression tagger
- Use a lookup tagger -- aka reference against a previously tagged piece of text (useful for the top 100 common words)
- Unigram tagging -- a trained lookup tagger (uses two data sets, training and test sets)

How to determine the category of a word (in general)?
- Morphological clues (suffixes, prefixes)
- Synatic clues = the typical contexts in which words occur
- Sematic clues = the meaning of the word

__open class__ = a POS that new words are typically added to (e.g. muggles, n00bs, added to noun class)

__closed class__ = a POS that new words are not added to often (e.g. above, along, below, between have no changed)


Chapter 6: Learning to Classify Text
---
__Classifiers:__ choosing the correct __class label__ for a given input
- eg. email spam filters
- topic of a news article
- classifying "bank" as a noun or verb

__Supervised__ = when a classifier is built based on a training corpa containing the correct label for each input

Steps in creating a classifier:
- Deciding what features are relevant and how to encode those features (this is a lost of the work in a good classifier)
- Examine the likelihood ratios = the listings in the training set that meet the features and are correct

Classifiers used for document classification (e.g. news, romance, horror)

__Joint classifier model__ = examines a bunch of related inputs and makes a label
__Sequence classier model__ = first find the most likely class label for the first input, then use this to find the best label for the second input and so on.
- Shortcoming: committed to all decisions, and one decision influences the next

__Hidden Markov Analysis__ = assigns scores to all the possible sequences and then chooses which sequence has the highest score (employ probability distribution, which a sequence classifier does not.)

Ways to measure classifiers:
- Accuracy
- Precision = how many of the items were identified as relevant
- Recall = how many of the relevant items we identified

__Confusion Matrix__ = table where each cell [i,j] indicates how often a label j was predicated when the correct label was i

__Cross Validation__ = perform multiple evaluations of different test tests and combine the scores
- To do this, subdivide the original corpus into N subsets called __folds__
- For each fold, we train the model using all but that fold, and then test on this fold

__Decision Trees__ = simple flowchart that selects labels for input values
- decision nodes = check feature value
- leaf nodes - assign labels
- root value = flowcharts initial decision
- decision stump = tree with a single node that decides to to classify inputs based on a single feature

__Information gain__ = how much more organized the input values become when we divide them up using a given feature (by calculating the entropy of their labels. This will be high if the input values have slightly varied labels and low if many inputs have the same label)

__Naive Bayes__: every features gets a say in determining which label should be assigned to a given input. 
- Each classifier starts by looking at the __prior probability__ of the label (aka the frequency of the label in the training set)
- Contribution from each feature combined with prior probability to achieve a likelihood estimate


Chapter 7 - Extracting Information from Text
---
__Structured data__ = regular and predictable organization of entities and relationships

__Named entity recognition__ = search for mentions of entities (locations, businesses, etc.)

__Relation recognition__ = search for relationships between entities in the text

__Chunking__ = technique used for entity recognition. Smaller chunks are tagged with POS, while larger chunks are used to identify multiple-word entities (e.g. San Francisco). These use tag patterns to re-factor chunks.
- __Tag patterns__ = a sequence of pos-tags eg <NN><VB><NN> that help identify a chunk
- __Noun phrase chunking__ = search for a sequence of proper nouns and chunk them together

__Chink__ = a sequence of tokens that we do not want to include in a chunk
