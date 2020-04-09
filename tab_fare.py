# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:16:11 2020

@author: MonOrdiPro
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.graph_objs import *
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

train_df = pd.read_csv('train_dataframe.csv')
complete_df = pd.read_csv('complete_dataframe.csv')

complete_df['Survived'].replace({0:'Dead', 1:'Alive'}, inplace = True)
train_df['Survived'].replace({0:'Dead', 1:'Alive'}, inplace = True)

fare_train_liste = train_df['Fare']
fare_complete_liste = complete_df['Fare']

t=pd.qcut(train_df.Fare,10)

decile1 = train_df[train_df.Fare <= 7.55]
decile2 = train_df[(train_df.Fare > 7.55) & (train_df.Fare <= 7.854)]
decile3 = train_df[(train_df.Fare > 7.854) & (train_df.Fare <= 8.05)]
decile4 = train_df[(train_df.Fare > 8.05) & (train_df.Fare <= 10.05)]
decile5 = train_df[(train_df.Fare > 10.05) & (train_df.Fare <= 14.454)]
decile6 = train_df[(train_df.Fare > 14.454) & (train_df.Fare <= 21.679)]
decile7 = train_df[(train_df.Fare > 21.679) & (train_df.Fare <= 27)]
decile8 = train_df[(train_df.Fare > 27) & (train_df.Fare <= 39.688)]
decile9 = train_df[(train_df.Fare > 39.688) & (train_df.Fare <= 77.958)]
decile10 = train_df[(train_df.Fare > 77.958)]

decile1_dead = len(decile1[decile1.Survived=='Dead']) # 85.87
decile2_dead = len(decile2[decile2.Survived=='Dead']) # 68.92
decile3_dead = len(decile3[decile3.Survived=='Dead']) # 81.51
decile4_dead = len(decile4[decile4.Survived=='Dead']) # 82.35
decile5_dead = len(decile5[decile5.Survived=='Dead']) # 57.69
decile6_dead = len(decile6[decile6.Survived=='Dead']) # 59.57
decile7_dead = len(decile7[decile7.Survived=='Dead']) # 48.89
decile8_dead = len(decile8[decile8.Survived=='Dead']) # 62.64
decile9_dead = len(decile9[decile9.Survived=='Dead']) # 48.84
decile10_dead = len(decile10[decile10.Survived=='Dead']) # 23.33

mortalite_y = [85.87,68.92,81.51,82.35,57.69,59.57,48.89,62.64,48.84,23.33]
interv_x = ['0 - 7.55','7.56 - 7.85','7.85 - 8.05','8.06 - 10.05','10.06 - 14.45','14.45 - 21.67','21.68 - 27','27 - 39.68','39.68 - 77.95','77.65 - 512']

fig1_train = px.histogram(
                x= fare_train_liste,
                title='train set Fare'
                )
fig2_complete = px.histogram(
                x= fare_complete_liste,
                title='complete set Fare'
                )

fig3_train = px.histogram(
                x= fare_train_liste,
                labels=['Dead','Alive'],
                color= train_df['Survived'],
                title='nombre mort par rapport au prix du billet',
                )
fig_finale = px.line(train_df,
                     x=interv_x,
                     y=mortalite_y)
fig_finale.update_xaxes(title='Interval de prix de billet (en decile)')
fig_finale.update_yaxes(title='Mortalité en pourcentage')

def get_content():
  return html.Div([
          
             html.Div([
              html.Div([
                      dcc.Graph(figure=fig1_train)
                      ],className='six columns'),
              
               html.Div([
                      dcc.Graph(figure=fig2_complete)
                      ],className='six columns')         
              
                ], className='row'),
         dcc.Graph(figure=fig3_train),
         dcc.Graph(figure=fig_finale),
          ])
