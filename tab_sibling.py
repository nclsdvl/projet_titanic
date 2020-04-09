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
train_df.SibSp.unique()

y = [65,46,54,75,83,100,100]

fig_finale = px.bar(train_df,
                     x=[0,1,2,3,4,5,8],
                     y=y,
                     text=y,
                     title="mortalité par nombre de proche de la même cohorte")
fig_finale.update_xaxes(title='Nombre de proche (conjoint ou fraterie)')
fig_finale.update_yaxes(title='Mortalité en pourcentage')
fig_finale.update_traces(textposition='inside')


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