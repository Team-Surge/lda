from gensim import corpora, models, similarities, utils
import os
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
def iter_documents(reuters_dir):
    """Iterate over Reuters documents, yielding one document at a time."""
    for fname in os.listdir(reuters_dir):
        # read each document as one big string
        document = open(os.path.join(reuters_dir, fname)).read()
        # parse document into a list of utf8 tokens
        yield utils.simple_preprocess(document)

class ReutersCorpus(object):
    def __init__(self, reuters_dir):
        self.reuters_dir = reuters_dir
        self.dictionary = corpora.Dictionary(iter_documents(reuters_dir))
        self.dictionary.filter_extremes()  # remove stopwords etc

    def __iter__(self):
        for tokens in iter_documents(self.reuters_dir):
            yield self.dictionary.doc2bow(tokens)


#corpus = ReutersCorpus('/home/eagl3eye/Downloads/news/all')
# remove common words and tokenize



#lda = models.LdaModel.load('/home/eagl3eye/Documents/lda/model.lda')


lda = models.LdaModel(corpus,alpha='auto',passes=5, num_topics=25, id2word=corpus.dictionary)

lda.save('/home/eagl3eye/Documents/lda/twitter.lda')


doc ="My genius friend adds words onto the ends of eassay paragraphs then changes the text color to white to increase the word count!"

bow = corpus.dictionary.doc2bow(utils.simple_preprocess(doc))
print lda[bow]

a = list(sorted(lda[bow], key=lambda x: x[1]))

print(lda.print_topic(a[-1][0]))
print(lda.print_topic(a[-2][0]))
