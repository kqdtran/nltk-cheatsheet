from __future__ import division
import nltk,re, pprint
from nltk.corpus import brown
import operator

""" P.14: Use sorted and set to get a sorted list of tags used in the Brown Corpus """
def sort_tags():
	brown_news_tagged = brown.tagged_words(simplify_tags=True)
	tags = []
	for (word, tag) in brown_news_tagged:
		if tag not in tags:
			tags.append(tag)
	return sorted(set(tags))

# print sort_tags()

""" P. 15: Write programs to process the Brown Corpus and find answers to the following questions:
	a. Which nouns are more common in their plural form
	b. Which word has the greatest number of distinct tags?
	c. List tags in decreasing order of frequency?
	d. Which tags are nouns most commonly after?"""

def often_plural():
	brown_news_tagged = brown.tagged_words()
	sing = {}
	plural = {}
	normally_plural = []
	for (word, tag) in brown_news_tagged:
		if re.findall(r'^N', tag):
			if re.findall(r'^N+.+S$', tag):
				if word in plural:
					plural[word] = plural[word] + 1
				else:
					plural[word] = 1
				if word not in sing:
					sing[word] = 0
			else:
				if word in sing:
					sing[word] = sing[word] + 1
				else:
					sing[word] = 1
	for word in plural:
		if word in sing:
			if plural[word] > sing[word]:
				normally_plural.append(word)
	return normally_plural

# print often_plural()

def most_popular_tags():
	brown_news_tagged = brown.tagged_words()
	tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
	sorted_pos = sorted(tag_fd.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sorted_pos

# print most_popular_tags()

def nouns_after():
	brown_news_tagged = brown.tagged_words(simplify_tags=True)
	previous = {}
	ct = 0
	for (word, tag) in brown_news_tagged:
		if ct != 0:
			if re.findall(r'^N', tag):
			 	previous_pos = prev
				if previous_pos not in previous:
					previous[previous_pos] = 1
				else:
					previous[previous_pos] = previous[previous_pos] + 1
		prev = tag
		ct += 1
	return sorted(previous.iteritems(), key=operator.itemgetter(1), reverse=True)

# print nouns_after()

def distinct_tags():
	brown_news_tagged = brown.tagged_words(simplify_tags=True)
	distinct = {}
	for (word, tag) in brown_news_tagged:
		if word not in distinct:
			distinct[word]=[tag]
		else:
			if tag not in distinct[word]:
				distinct[word].append(tag)
	for word in distinct:
		distinct[word] = len(distinct[word])
	return sorted(distinct.iteritems(), key=operator.itemgetter(1), reverse=True)

print distinct_tags()[0]
