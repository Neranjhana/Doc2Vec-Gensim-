#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:13:20 2019

@author: spiglobal
"""
import string
from nltk.corpus import stopwords 
import nltk
import pickle
stop_words = set(stopwords.words('english')) 
data=pd.read_pickle('final_pickle.pkl')
data['body'] = data['body'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
pickle_out=open("final_pickle.pkl","wb")
pickle.dump(data,pickle_out)
# Out[40]: