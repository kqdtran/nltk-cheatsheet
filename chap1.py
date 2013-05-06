from nltk.book import *

""" P. 25: Define "sent" to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']. 
Now write code to: print all the words begining with sh, print all the words longer than 4 chars."""
def find_sh(sent):
	sh_words = []
	for word in sent:
		if word[:2] == "sh":
			sh_words.append(word)
	return sh_words

def larger_than_four(sent):
	four_words = []
	for word in sent:
		if len(word) > 4:
			four_words.append(word)
	return four_words

# sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
# print find_sh(sent)
# print larger_than_four(sent)

""" P. 26: What does the following Python code do? sum([len(w) for w in text1]). Can you use it to work 
out the average word length of a text?"""

def avg_word_length(text):
	return sum([len(w) for w in text]) / len(text)

# print avg_word_length(text1)

"""" P.27 Define a function called vocab-size(text) that has a single parameter for the text
 and returns the vocabulary size of the text"""

def vocab_size(text):
 	fdist = FreqDist(text)
	vocabulary = fdist.keys()
	return len(vocabulary)

# print vocab_size(text1)

""" P. 28: Define a function percent(word, text) that calculates how often a given word 
occurs and expresses the result as a percentage"""

def percent(word, text):
	num_occurances = float(text.count(word))
	num_total = float(len(text))
	return str(round(100 * (num_occurances / num_total),2)) + ' %'

# print percent("the", text1)

""" P. 29: We have been using sets to store vocabularies. Try the following Python expression: set(sent3) < set(text1).
Experiment with the using different arguments to set(). What does it do? Can you think of a practical application for 
this? """

def compare_data(sent, text):
	return set(sent) < set(text)

print compare_data(sent9, text1)
"""It returns a boolean value indicating if the sent or the text has more unique words. This can be used to help 
determine if sent is a subset to text or visa versa"""




