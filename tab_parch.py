# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:38:55 2020

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



parch0 = train_df[train_df['Parch']==0]
parch1 = train_df[train_df['Parch']==1]
parch2 = train_df[train_df['Parch']==2]
parch3 = train_df[train_df['Parch']==3]
parch4 = train_df[train_df['Parch']==4]
parch5 = train_df[train_df['Parch']==5]
parch6 = train_df[train_df['Parch']==6]
parch_more = train_df[train_df['Parch']>2]

parch0_dead = len(parch0[parch0.Survived=='Dead']) # 65.63
parch1_dead = len(parch1[parch1.Survived=='Dead']) # 44.91
parch2_dead = len(parch2[parch2.Survived=='Dead']) # 50
parch3_dead = len(parch_more[parch_more.Survived=='Dead']) # 73.33





liste_train_parch = train_df['Parch']
liste_complete_parch = complete_df['Parch']

fig1_train = px.histogram(
                x= liste_train_parch,
                title='from Train Set'
                )
fig2_complete = px.histogram(
                x= liste_complete_parch,
                title='From Complete Set'
                )
fig3_train = px.histogram(
                x= liste_train_parch,
                labels=['Dead','Alive'],
                
                color= train_df['Survived'],
                title='nombre mort par rapport à la variable Fraterie / conjoint',
                )

fig_finale = px.bar(train_df,
                     x=[0,1,2,3,4,5,6],
                     y=[66,45,50,40,100,80,100])
fig_finale.update_xaxes(title='Nombre de proche (enfant ou parent)')
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