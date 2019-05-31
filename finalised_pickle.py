#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:02:21 2019

@author: spiglobal
"""

import pickle
import pandas as pd
data=pd.read_pickle('batch1.pickle')
for line in data:
    print(line)
print(data)
#data.to_csv('out', sep='\t')
print(data.iloc[1449])
data=data.drop(columns="title")
data=data.drop(columns="phase")
data=data.drop(columns="lenwords")
pickle_out=open("final_pickle.pkl","wb")

pickle.dump(data,pickle_out)
#print(data.iloc[899])
#[(900, 0.4435845613479614), (1976, 0.42374610900878906), (667, 0.422349750995636), (594, 0.4189079701900482), (1000, 0.41827064752578735), (1986, 0.4152243733406067), (929, 0.4144706130027771), (641, 0.413410484790802), (561, 0.4132295250892639), (1991, 0.410800576210022)]
#[(821, -0.1620548665523529), (910, -0.20789845287799835), (666, -0.24038369953632355), (34, -0.2526808977127075), (1064, -0.27465713024139404), (1450, -0.28789180517196655), (1318, -0.2934408187866211), (1400, -0.3167341351509094), (1795, -0.31705278158187866), (443, -0.3207663297653198)]