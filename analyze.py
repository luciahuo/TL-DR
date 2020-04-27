from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
import collections
from collections import OrderedDict
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


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


def get_topics(texts):
    df = pd.DataFrame({'original_doc': texts})

    # removing punctuation or extra characters
    df['cleaned_doc'] = df['original_doc'].str.replace("[^a-zA-Z#]", " ")

    # getting rid of short words of length less than 4
    df['cleaned_doc'] = df['cleaned_doc'].apply(lambda x: ' '.join([word for word in x.split() if len(word) > 4]))

    # makes all words lowercase
    df['cleaned_doc'] = df['cleaned_doc'].apply(lambda x: x.lower())

    # convert into tokens
    tokenized_doc = df['cleaned_doc'].apply(lambda x: x.split())

    # get rid of stop-words
    tokenized_doc = tokenized_doc.apply(lambda x: [token for token in x if token not in stop_words])
    num = max(len(texts) // 2, 1)

    # convert tokens back to doc
    detokenized_doc = []
    for i in range(len(df)):
        token = " ".join(tokenized_doc[i])
        detokenized_doc.append(token)
    df['cleaned_doc'] = detokenized_doc

    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.5, max_features=800, smooth_idf=True)
    X = vectorizer.fit_transform(df['cleaned_doc']) #fit shape of model

    # create SVD model for documents and terms 
    svd_model = TruncatedSVD(n_components=num, n_iter=110, algorithm='randomized', random_state=98)
    svd_model.fit(X)

    terms = vectorizer.get_feature_names()
    topics_list = []

    print("-----Topics you seem to be interested in: -----")
    for i, comp in enumerate(svd_model.components_):
        term_stats = zip(terms, comp)
        sorted_terms = sorted(term_stats, key=lambda x:x[1], reverse=True)[:6]
        topic_string = "Topic " + str(i) + ": "  + ", ".join([term[0] for term in sorted_terms])
        print(topic_string)
        topics_list.append(topic_string)
    return topics_list
    
