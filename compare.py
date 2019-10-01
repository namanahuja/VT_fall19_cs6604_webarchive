# -*- coding: utf-8 -*-

import pandas as pd
from html_similarity import style_similarity, structural_similarity, similarity
from bs4 import BeautifulSoup, Doctype

file = pd.read_parquet('../data.parquet', engine='pyarrow')
numRows = len(file.index)

validPayloads = []
for i in range(numRows):
    payload = file.iloc[i].payload
    mime = file.iloc[i].mime
    soup = (BeautifulSoup(payload, "html.parser"))

   #check for only vt.edu
    
    if(mime == 'text/html' and len(payload) > 1):
        validPayloads.append(payload)
        
scores = [[-1 for i in range(len(validPayloads))] for j in range(len(validPayloads))]
for i in range(len(validPayloads)):
    payload1 = validPayloads[i]
    
    for j in range(len(validPayloads)):
       
        payload2 = validPayloads[j]
    
        try:
            #print(i,j)
            score = str(similarity(payload1, payload2))
            scores[i][j] = score
            #print(score)
        
        except:
            print(i,j)
        
