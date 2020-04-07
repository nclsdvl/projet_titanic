# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 07:09:01 2020

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

liste_train_sibling = train_df['SibSp']
liste_complete_sibling = complete_df['SibSp']




# epouse ou fraterie

fig1_train = px.histogram(
                x= liste_train_sibling,
                title='from Train Set'
                )
fig2_complete = px.histogram(
                x= liste_complete_sibling,
                title='From Complete Set'
                )
fig3_train = px.histogram(
                x= liste_train_sibling,
                labels=['Dead','Alive'],
                
                color= train_df['Survived'],
                title='nombre mort par rapport à la variable Fraterie / conjoint',
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
         html.H5('taux de décés à 0 conjoint / fraterie : 65%'),
         html.H5('taux de décés à 1 conjoint / fraterie : 46%'),
         html.H5('taux de décés à 2 conjoint / fraterie : 54%'),
         html.H5('taux de décés à 3 conjoint / fraterie : 75%'),
         html.H5('taux de décés à 4 conjoint / fraterie : 83%'),
         html.H5('taux de décés à +4 conjoint / fraterie : 100%'),
          
          ])