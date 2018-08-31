# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu
pdata = []
fileids = nc.movie_reviews.fileids('pos')
for fileid in fileids:
    feature = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        feature[word] = True
    pdata.append((feature, 'POSITIVE'))
ndata = []
fileids = nc.movie_reviews.fileids('neg')
for fileid in fileids:
    feature = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        feature[word] = True
    ndata.append((feature, 'NEGATIVE'))
pnumb, nnumb = \
    int(len(pdata) * 0.8), int(len(ndata) * 0.8)
train_data = pdata[:pnumb] + ndata[:nnumb]
test_data = pdata[pnumb:] + ndata[nnumb:]
model = cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print(ac)
tops = model.most_informative_features()
print(tops[:10])
reviews = [
    'It is an amazing movie.',
    'This is a dull movie. I would never recommend it to anyone.',
    'The cinematography is pretty great in this movie.',
    'The direction was terrible and the story was all over the place.']
sents, probs = [], []
for review in reviews:
    feature = {}
    words = review.split()
    for word in words:
        feature[word] = True
    pcls = model.prob_classify(feature)
    sent = pcls.max()
    prob = pcls.prob(sent)
    sents.append(sent)
    probs.append(prob)
for review, sent, prob in zip(reviews, sents, probs):
    print(review, '->', sent, round(prob, 2))
