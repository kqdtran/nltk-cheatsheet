Chapter 3
---

How to import text from the web:
```
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
```   
The raw content of a book includes many details we are not interested in such as whitespace, line breaks and blank lines.  

**Tokenization**: break up the string into a list of words and punctuation.   


Cleaning HTML:
```
url = "http://www.google.com"
html = urlopen(url).read()
raw = nltk.clean_html(html)
tokens = word_tokenize(raw)
text = nltk.Text(tokens)
txt.concordance('search')
```   
For more sophisticated processing of HTML, use the [Beautiful Soup package](http://www.crummy.com/software/BeautifulSoup/)  


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