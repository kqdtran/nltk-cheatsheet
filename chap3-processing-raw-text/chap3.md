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
, which searchs for all words ending in 'ed'    

__wildcard__ = '.' = symbol that matches any character

__textonyms__ = two or more words that are entered with the same sequence of keystokes (phones)
```
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
```

<table border="1">
  <colgroup>
    <col width="15%" />
    <col width="85%" />
  </colgroup>
  <thead valign="bottom">
    <tr><th class="head">Operator</th>
      <th class="head">Behavior</th>
    </tr>
  </thead>
  <tbody valign="top">
    <tr><td><pre>.</pre></td>
      <td>Wildcard, matches any character</td>
    </tr>
    <tr><td><pre>^abc</pre></td>
      <td>Matches some pattern <span class="math">abc</span> at the start of a string</td>
    </tr>
    <tr><td><pre>abc$</pre></td>
      <td>Matches some pattern <span class="math">abc</span> at the end of a string</td>
    </tr>
    <tr><td><pre>[abc]</pre></td>
      <td>Matches one of a set of characters</td>
    </tr>
    <tr><td><pre>[A-Z0-9]</pre></td>
      <td>Matches one of a range of characters</td>
    </tr>
    <tr><td><pre>ed|ing|s</pre></td>
      <td>Matches one of the specified strings (disjunction)</td>
    </tr>
    <tr><td><pre>*</pre></td>
      <td>Zero or more of previous item, e.g. <pre>a*</pre>, <pre>[a-z]*</pre> (also known as <em>Kleene Closure</em>)</td>
    </tr>
    <tr><td><pre>+</pre></td>
      <td>One or more of previous item, e.g. <pre>a+</pre>, <pre>[a-z]+</pre></td>
    </tr>
    <tr><td><pre>?</pre></td>
      <td>Zero or one of the previous item (i.e. optional), e.g. <pre>a?</pre>, <pre>[a-z]?</pre></td>
    </tr>
    <tr><td><pre>{n}</pre></td>
      <td>Exactly <span class="math">n</span> repeats where n is a non-negative integer</td>
    </tr>
    <tr><td><pre>{n,}</pre></td>
      <td>At least <span class="math">n</span> repeats</td>
    </tr>
    <tr><td><pre>{,n}</pre></td>
      <td>No more than <span class="math">n</span> repeats</td>
    </tr>
    <tr><td><pre>{m,n}</pre></td>
      <td>At least <span class="math">m</span> and no more than <span class="math">n</span> repeats</td>
    </tr>
    <tr><td><pre>a(b|c)+</pre></td>
      <td>Parentheses that indicate the scope of the operators</td>
    </tr>
  </tbody>
</table>

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