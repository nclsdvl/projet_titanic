# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:53:08 2020

@author: utilisateur
"""
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
import cufflinks as cf
import plotly.offline
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)
"""
df1 = pd.read_csv('gender_submission.csv')
df2 = pd.read_csv('test.csv')
df3 = pd.read_csv('train.csv')

df2['Survived'] = df1['Survived']

complete_df = pd.concat([df3,df2], sort=False)

complete_df.info()

complete_df.drop('Cabin', axis=1, inplace=True)

complete_df.to_csv('complete_dataframe.csv', index = False)
"""
df = pd.read_csv('complete_dataframe.csv')

profile = ProfileReport(df, title='Pandas Profiling Report', html={'style':{'full_width':True}})

profile.to_file(output_file="your_report.html")

df.iplot()
