from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
import collections
from collections import OrderedDict
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


def get_keywords(texts):
    token_arr = WhitespaceTokenizer().tokenize(texts)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in token_arr]
    ns_tokens = []
    for t in tokens:
        # taking out words shorter length three and stop word
        if t.lower() not in stop_words and len(t) > 3:
            ns_tokens.append(t.lower())
    term_freq = collections.Counter(ns_tokens)
    sorted_d = OrderedDict(sorted(term_freq.items(), key=lambda x: -x[1]))
    return [k for k in list(sorted_d)[:10]]
