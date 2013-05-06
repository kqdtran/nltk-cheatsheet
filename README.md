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

__Machience translation__ = high-quality, idomatic translation between two languages
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

Chapter 3
---

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
