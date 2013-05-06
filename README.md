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
__ HOW DO WE IDENTIFY THE WORDS OF A TEXT THAT ARE MOST INFORMATIVE ABOUT  TOPIC?__
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
