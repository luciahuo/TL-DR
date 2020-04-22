from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
import collections
from collections import OrderedDict
from nltk.corpus import stopwords
import math
stop_words = set(stopwords.words('english'))

def get_keywords(text):
    token_arr = WhitespaceTokenizer().tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in token_arr]
    ns_tokens = []
    for t in tokens:
        if t.lower() not in stop_words:
            ns_tokens.append(t.lower())
    term_freq = collections.Counter(ns_tokens)
    sorted_d = OrderedDict(sorted(term_freq.items(), key=lambda x: -x[1]))
    return [k for k in list(sorted_d)[:10]]
