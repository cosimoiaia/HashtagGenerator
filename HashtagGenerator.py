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

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import gensim
from gensim import corpora
import string
import argparse

FLAGS = None


def main():

    stop = set(stopwords.words(FLAGS.language))
    exclude = set(string.punctuation) 
    lemma = WordNetLemmatizer()
    path=FLAGS.document

    fd = open(path)

    text = fd.read()
    
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

    for t in topic: print(t[1])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python script to extract hashtags from long text based on LDA model from GenSim')
    parser.add_argument('--document', type=str, required=True, default='', help='Path to the document')
    parser.add_argument('--language', type=str, required=False, default='english', help='Language of the text')
    parser.add_argument('--hashtags', type=int, required=False, default=4, help='Number of hashtags to extract')
    parser.add_argument('--passes', type=int, required=False, default=50, help='Iteration for the LDA model to perform')
    FLAGS = parser.parse_args()
    main()

