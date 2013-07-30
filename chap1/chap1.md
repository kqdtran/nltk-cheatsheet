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