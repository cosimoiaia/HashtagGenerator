#!/usr/bin/env python
##########################################
#
# HashtagGenerator.py: A simple python script to extract hashtags from long text
#                      using LDA model from GenSim
#
# Author: Cosimo Iaia <cosimo.iaia@gmail.com>
# Date: 15/05/2018
#
# This file is distribuited under the terms of GNU General Public
#
#########################################

from __future__ import print_function

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import gensim
from gensim import corpora
import string
import argparse
import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


FLAGS = None


def main():

    stop = set(stopwords.words(FLAGS.language))
    exclude = set(string.punctuation) 
    lemma = WordNetLemmatizer()
    path=FLAGS.document

    text = ''
    if(re.match(regex, path) != None):
        import bs4
        import requests

        print('[Url found]')

        html = bs4.BeautifulSoup(requests.get(path).text, "html.parser")

        data = html.find_all(text=True)
        def visible(element):
            if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
                return False
            elif re.match('<!--.*-->', str(element.encode('utf-8'))):
                return False
            return True

        results = filter(visible, data)
        text = u" ".join(t.strip() for t in results)
    else:
        text = open(path).read()

    
    doc_complete = text.split('\n')

    def clean(doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        return normalized

    doc_clean = [clean(doc).split() for doc in doc_complete]    
    dictionary = corpora.Dictionary(doc_clean)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=FLAGS.hashtags, id2word = dictionary, passes=FLAGS.passes)
    topic = ldamodel.print_topics(num_topics=5, num_words=5)

    hashtags = []
    for t in topic: 
        for h in t[1].split('+'):
            hashtags.append('#'+h[h.find('"')+1:h.rfind('"')])

    print("HashTags: ")
    for ht in list(set(hashtags)):
        print(ht, end=' ')
    print()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python script to extract hashtags from URL or long text based on LDA model from GenSim')
    parser.add_argument('--document', type=str, required=True, default='', help='Path or URL to the document')
    parser.add_argument('--language', type=str, required=False, default='english', help='Language of the text')
    parser.add_argument('--hashtags', type=int, required=False, default=4, help='Number of hashtags to extract')
    parser.add_argument('--passes', type=int, required=False, default=50, help='Iteration for the LDA model to perform')
    FLAGS = parser.parse_args()
    main()

