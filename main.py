# import gensim.models
from gensim.models import Word2Vec
import pandas as pd
import gensim.downloader as api
wv = api.load('word2vec-google-news-300')
for index, word in enumerate(wv.index_to_key):
    if index == 10:
        break
    print(f"word #{index}/{len(wv.index_to_key)} is {word}")
# sentences = "iran ey saraye omid"
# model = gensim.models.Word2Vec(sentences=sentences)

vec_king = wv['king']
vec_woman = wv['woman']

vec_queen = vec_king + vec_woman
print(vec_queen)
print(wv.most_similar(positive=['woman', 'king'], negative=['man'], topn=1))
print('hello world')
