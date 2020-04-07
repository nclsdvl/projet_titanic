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

quartile1 = train_df[train_df.Fare <= 7.91]
quartile2 = train_df[(train_df.Fare > 7.91) & (train_df.Fare <= 14.45)]
quartile3 = train_df[(train_df.Fare > 14.45) & (train_df.Fare <= 31)]
quartile4 = train_df[train_df.Fare > 31]

dead_quart1 = len(quartile1[quartile1.Survived == 'Dead'])
dead_quart2 = len(quartile2[quartile2.Survived == 'Dead'])
dead_quart3 = len(quartile3[quartile3.Survived == 'Dead'])
dead_quart4 = len(quartile4[quartile4.Survived == 'Dead'])



quart = pd.qcut(train_df.Fare,4)

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
         html.H5('taux de mortalité du 1° quartile (0 - 7.91) : 80.26%'),
         html.H5('taux de mortalité du 2° quartile (7.91 - 14.45) : 69.12%'),
         html.H5('taux de mortalité du 3° quartile (14.45 - 31) : 55.46%'),
         html.H5('taux de mortalité du 4° quartile (31 - 512.33) : 41.9%'),
          ])
