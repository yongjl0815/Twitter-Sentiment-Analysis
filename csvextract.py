# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:21:21 2018

@author: yongj
"""

import pandas as pd
import re

#read the training data file using panda
df = pd.read_csv('trainingdata.csv', error_bad_lines=False)

arrayA = []
#add the sentimenttext column (sentence) to arrayA
for i in df['SentimentText']:
    arrayA.append(re.sub(r'([^\s\w]|_)+', '', i).lstrip()) 
    
arrayB = []
#add the sentiment column (0 r 1) to arrayB
for i in df['Sentiment']:
    if i == 1: #change the values to positive or negative
        arrayB.append('positive')
    else:
        arrayB.append('negative')
        
arrayC = []
z = 0 #index
#add text and sentiment to a single array, c
sentimentCount = 3000
for i in range(0,sentimentCount):
    arrayC.append(tuple([arrayA[z], arrayB[z]]))
    z = z + 1

#print (arrayC)

