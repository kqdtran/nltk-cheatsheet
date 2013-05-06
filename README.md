Notes From The NLTK Book
========

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
text2.concortance(["montrous", "very"])
```
__dispersion plot__ = positional information of a word within text

- each stripe on plot = an occurance of the word

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

- Neither the very infreqeunt or very frequent words (common English plumbing) help.
- You want the words in the middle (they occur more than x times and less than y times e.g. 7)

__frequency distribiution__ = the frequency of each vocabulry item in the text

```
fdist = FreqDist(text1)
vocabulary = fdist.keys()
fdist.plot(50, cumulative)
```
__hapaxes__ = words that occur only once

__collocation__ = a series of words that appears together unusually often (e.g. red wine)

__bigrams__ = a list of word pairs
```
biagrams(['more', 'is', 'said', 'than', 'done'])
```
Essentially, collocations are frequent bigrams, except that we want to pay more attention to the cases that involve rare words.
```
text4.collocations()
```

__AUTOMATIC NATURAL LANGUAGE UNDERSTANDING__
Getting a computer to answer a "human" question automatically involves a lot of NLP:
- information extration
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

Figuring out "who did what to whom" involves finding the __antecendent__ of the pronoun "they" (thieves or paintings?)
NLP uses:

- __Anaphora resolution__ = identifying whar a pronoun or noun phrase refers to
- __Sematic role labeling__ = identifying how a noun phrase relates to the verb (agent, patient, instrument, etc.)

__Machience translation__ = high-quality, idomatic translation between two languages.
NLTK's MT = babelizer

```
>>> babelize.shell()
>>> How long are final exams?
>>> german
>>> run
```

How this works: given a document in English and German and a bilingual dictionary, we can automatically pair up the sentences in a method called __text alignment__. Once we have a million+ sentences, we can detect corresponding words and phrases and build a model that can be used to translate new text.

Spoken Dialogue Systems:

__Turning test__ = can a dialogue system, repsonding to a user's text input, perform so naturally that we cannot distinguish it from a human-generated response?


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
- Web text

```
from nltk.corpus import webtext
```

- Chatroom conversations 

```
from nltk.corpus import nps_chat
```

- Brown corpus -- first million-word electronic corpus in English
-- Catagoried by genre (news, editorial, etc.)
-- Resource for studying systematic differences between genres -- a kind of linguistics called __stylistics__
-- e.g. Compare genere's use of modal verbs

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
- Inagural address corpus
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

__Conditional frequency distributions__ = collection of frequency distributions, each for a different condition (e.g. a catagory)

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

__Lexical entry__ = consists of a __headword__ (aka a __lemma__) and additional ifo such as (part of speech and sense).

__Homonyms__ = two distinct words having the same spelling

__stopwords__ = high-frequency, eglish plumbing words (the, is, to)s
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

__WordNet__ = sematically oriented English dictionary (righer than a regular thesaurus)
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
- __+__ = one or more instances of the precending item (closure)
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

Chapter 5
---

Chapter 6
---

Chapter 7
---

Chapter 8
---

Chapter 9
---

Chapter 10
---

Chapter 11
---

Chapter 12
---

Chapter 13
---
