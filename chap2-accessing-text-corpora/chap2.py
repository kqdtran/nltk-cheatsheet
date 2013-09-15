from nltk.corpus import udhr
from nltk.corpus import wordnet as wn

"""P. 25: Define a function find_langauge() that takes a string as its input arg and returns a list of languages that 
have that string as a word."""

def find_language(s):
	latin = []
	final_langs = []
	ct = 0
	for id in udhr.fileids():
		if '-Latin1' in id:
			latin.append(id)
	for lang in latin:
		for word in udhr.words(lang):
			if word == s:
				final_langs.append(lang)
				print "Found word: " + word, "Search word: " + s
				break
	return final_langs

print find_language("bye")

"""P. 26: What is the branching factor of the noun hypernym hierachry? """

def branching_factor():
	all_syn = wn.all_synsets('n')
	total_ratio = 0
	all = 0
	for syn in all_syn:
		leaves = len(syn.hyponyms())
		if leaves > 0:
			ratio = float(leaves)
			total_ratio = total_ratio + ratio
			all += 1
	return total_ratio / float(all)

print branching_factor()

""" P. 27: Compute the average polysemy of nouns, verbs, adjectives, and adverbs according to WordNet"""

def polysemy(pos):
	p = 0
 	lemmas = []
 	syns = list(wn.all_synsets(pos))
 	for synset in syns:
  		lemmas.extend(synset.lemma_names)
 	for lemma in lemmas:
  		new = len(wn.synsets(lemma, pos))
  		p = p + new
  	length = len(syns)
 	return p/length

def all_polysemy():
	print "Noun: ", polysemy('n')
	print "Verb: ", polysemy('v')
	print "Adjective: ", polysemy('a')
	print "Adverb: ", polysemy('r')

all_polysemy()