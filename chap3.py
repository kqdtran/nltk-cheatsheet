from __future__ import division
import nltk,re, pprint
from urllib import urlopen

"""P.24: convert text hAck3r using regular expressions and substitution"""
def hacker(s):
	s = s.lower()
	if re.search('ate', s):
		s = s.replace('ate', '8')
	if re.search('e', s):
		s = s.replace('e', '3')
	if re.search('i', s):
		s = s.replace('i', '1')
	if re.search('o', s):
		s = s.replace('o', '0')
	if re.search('1', s):
		s = s.replace('1', '|')
	if re.search('s', s):
		s = s.replace('s', '5')
	if re.search('.', s):
		s = s.replace('.', '5w33t!')
	return s

print hacker('hacker')

"""P. 39: Soundex algorithm """

def soundex(s):
	original = s
	first = s[0]
	s = s[1:]
	found = re.findall(r'[bfpv]', s)
	for v in found:
		s = s.replace(v, '1')
	found = re.findall(r'[cgjkqsxz]', s)
	for v in found:
		s = s.replace(v, '2')
	found = re.findall(r'[dt]', s)
	for v in found:
		s = s.replace(v, '3')
	found = re.findall(r'[l]', s)
	for v in found:
		s = s.replace(v, '4')
	found = re.findall(r'[mn]', s)
	for v in found:
		s = s.replace(v, '5')
	found = re.findall(r'[r]', s)
	for v in found:
		s = s.replace(v, '6')
	found = re.findall(r'([0-9]+)\1', s)
	for v in found:
		s = re.sub(r'([0-9]+)\1', r'\1', s)
	while re.findall(r'([0-9])[wh]\1', s):
		s = re.sub(r'([0-9])[wh]\1', r'\1', s)
	found = re.findall(r'[aeiouyhw]', s)
	for v in found:
		s = s.replace(v, '')
	while len(s) < 3:
		s = s + '0'
	s = first+s
	return s
print soundex('Tymczak')

"""P. 37: Remove HTML tags from at html file and normalize whitespace"""
def remove_tags(site):
	url = site
	html = urlopen(url).read()
	raw = nltk.clean_html(html)
	tokens = nltk.word_tokenize(raw)
	ct = 0
	for t in tokens:
		if t.find(r'^<head'+r'>$') and t.find(r'^</head'+r'>$'):
			tokens.pop(ct)
		ct += 1
	# for t in tokens:
	# 	print t, len(t)
	text = nltk.Text(tokens)
	return text

print remove_tags('http://www.google.com')
