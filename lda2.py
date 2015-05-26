import logging
import sys
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities



# remove common words and tokenize


if (sys.argv[1] == 'save'):
    documents = open("output.txt", "r+")
    stoplist = open("stopwords.txt")
    #set('for it im i\'m :) or to it\'s all also more than up oh your (: a an about only / at # - + much alot be as little ! with a from of the and we by just not go do to in me you u with from he she i my they them is are were was so on got going but can have that this those there'.split())

    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

    # remove words that appear only once
    from collections import defaultdict
    frequency = defaultdict(int)

    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > 1]
        for text in texts]

    print ("saving")
    dictionary = corpora.Dictionary(texts)
    dictionary.save('deerwester.dict') # store the dictionary, for future reference
    corpus = [dictionary.doc2bow(text) for text in texts]
    model = models.ldamodel.LdaModel(corpus, id2word=dictionary,passes=4, alpha='auto', num_topics=50)
    model.save('twitter.lda')
    texts.close()
    print lda.print_topics()
else:
    print ("loading")
    dictionary = corpora.Dictionary()
    dictionary.load('deerwester.dict') # load the dictionary, for future reference
    model = models.LdaModel.load('twitter.lda')
    for i in range(0, model.num_topics-1):
        print "Topic ", i, ": \n"
        print model.print_topic(i)


new_doc = sys.argv[2]
print (new_doc)

doc_bow = dictionary.doc2bow(new_doc.lower().split())

a = list(sorted(model[doc_bow], key=lambda x: x[1]))

topic1= model.print_topic(a[-1][0])
topic2= model.print_topic(a[-2][0])
topic1 = topic1.split(" ", 1)
topic2 = topic2.split(" ", 1)
print(topic1)
print(topic2)
#print(topic1[0][6:])
#print(topic2[0][6:])
