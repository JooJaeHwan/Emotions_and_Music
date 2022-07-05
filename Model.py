import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Kkma
import pandas as pd
import os
import numpy as np
import keras
import tensorflow as tf
from datetime import datetime

def Tfidf_padding(sentence):
    def clean_text(d):
        pattern = r'[^가-힣0-9\s]'
        text = re.sub(pattern, '', d)
        text = re.sub("\n", ' ', text)
        text = re.sub("  +", " ", text)
        return text
        
    documents = [clean_text(sentence)]
    def tokenizer (sentences):
        kkma = Kkma()
        error_list = []
        #불용어처리
        current_path = os.getcwd()
        f = open(current_path + "/stop_words.txt", 'r', encoding='utf-8')
        stop_words= [line.replace('\n','') for line in f.readlines()]

        #영어로 Nan된 document 삭제
        tokens = []
        for i, sentence in enumerate(sentences) :
            try : 
                tokens.append([word[0] for word in kkma.pos(sentence) if len(word) > 1 
                                and (word[0] not in stop_words)
                                and (not word[1].startswith('J'))
                                and (not word[1].startswith('E'))])
            except Exception:
                print('error', sentence, i)
                error_list.append(i)
                tokens.append("error")
        tokens = pd.Series(tokens).drop(index = error_list)
        
        return tokens
    tfidf = TfidfVectorizer(tokenizer=tokenizer, analyzer='char', ngram_range=(1,3),
                    smooth_idf=True, sublinear_tf=True, max_features=460)
    vectors = tfidf.fit_transform(documents)
    vectors = np.array(vectors.todense())
    padded = np.array([np.append(np.array(vector), np.array([0])) for vector in vectors])
    return padded

def model_prediect(padded):
    model = keras.models.load_model('model.h5')
    try:
        score = model.predict(padded)
        index = np.argmax(score, axis=1)[0]
        return index
    except:
        print("다시 작성해주세요")

def cosine(name, music, sentences):
    music = music.append({'artist_name':name, "song_name":name, "lyrics" : sentences}, ignore_index=True)
    tfidf = TfidfVectorizer(analyzer='char', ngram_range=(1,3), smooth_idf=True, sublinear_tf=True)
    tfidf_matrix = tfidf.fit_transform(music["lyrics"] )
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    title_to_index = dict(zip(music["song_name"], music.index))
    def get_recommendations(title, cosine_sim=cosine_sim):
        idx = title_to_index[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        music_list = [(music['artist_name'].iloc[idx[0]], music['song_name'].iloc[idx[0]]) for idx in sim_scores]
        return music_list
    return get_recommendations(name)
