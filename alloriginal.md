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