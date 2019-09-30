# -*- coding: utf-8 -*-

import pandas as pd
from html_similarity import style_similarity, structural_similarity, similarity

file1 = pd.read_parquet('/home/naman/dl/vt.edu/2014-01-01.warc.parquet/part-00000-96e82b89-d494-4c0c-9e45-a04769a4e8f9-c000.snappy.parquet', engine='pyarrow')
numRows = len(file1.index)

validPayloads = []
for i in range(numRows):
    payload = file1.iloc[i].payload
    if(len(payload) > 1):
        validPayloads.append(payload)
        
scores = [[-1 for i in range(len(validPayloads))] for j in range(len(validPayloads))]
for i in range(len(validPayloads)):
    payload1 = validPayloads[i]
    
    for j in range(len(validPayloads)):
       
        payload2 = validPayloads[2]
    
        print(i,j)
        if(len(payload2) < 1 or len(payload1) < 1):
            continue
        
        score = str(similarity(payload1, payload2))
        print(score)
        
