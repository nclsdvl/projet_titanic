# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:53:08 2020

@author: utilisateur
"""
import pandas as pd

df1 = pd.read_csv('gender_submission.csv')
df2 = pd.read_csv('test.csv')
df3 = pd.read_csv('train.csv')

df2['Survived'] = df1['Survived']

complete_df = pd.concat([df3,df2])