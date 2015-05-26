import logging
import sys
import os
from pprint import pprint
from gensim import corpora, models, similarities
from model import startModel


# remove common words and tokenize

fpath = os.path.dirname(os.path.realpath(__file__))

if (sys.argv[1] == 'save'):
    #print ("saving")
    stoplist = set(map(str.strip, open('stopwords.txt')))

    documents = open("output.txt")

    texts = [[word for word in document if word not in stoplist]
        for document in documents]

    # remove words that appear only once
    from collections import defaultdict
    frequency = defaultdict(int)

    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > 1]
        for text in texts]


    dictionary = corpora.Dictionary(texts)
    dictionary.save('deerwester.dict') # store the dictionary, for future reference
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(corpus)

    model = models.ldamodel.LdaModel(corpus, id2word=dictionary,passes=1, alpha='auto', num_topics=50)
    model.save('twitter.lda')
    stoplist.close()
    #for i in range(0, model.num_topics-1):
    #    print "Topic ", i, ": \n"
    #    print model.print_topic(i)

else:
    #print ("loading")
    dictionary = corpora.Dictionary()
    dictionary.load(fpath + '/deerwester.dict') # load the dictionary, for future reference
    model = models.LdaModel.load(fpath + '/twitter.lda')


new_doc = sys.argv[2]
print (new_doc)

doc_bow = dictionary.doc2bow(new_doc.lower().split())

a = list(sorted(model[doc_bow], key=lambda x: x[1]))

topic1= a[-1][0]
topic2= a[-2][0]
startModel(new_doc)
