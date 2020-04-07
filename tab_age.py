# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 05:08:53 2020

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

train_na_age = len(train_df[train_df['Age'].isna()])
complete_na_age = len(complete_df[complete_df['Age'].isna()])

complete_df['Survived'].replace({0:'Dead', 1:'Alive'}, inplace = True)
train_df['Survived'].replace({0:'Dead', 1:'Alive'}, inplace = True)

train_dropped = train_df['Age'].dropna()
complete_dropped = complete_df['Age'].dropna()

train_df['Age'].fillna(28, inplace = True)
complete_df['Age'].fillna(28, inplace = True)



age_train_liste = train_df['Age']
age_complete_liste = complete_df['Age']

df_enfant = train_df[(train_df['Age']<=15)]
df_enfant_alive = train_df[(train_df['Age']<=15) & (train_df['Survived'] == 'Alive')]

df_jeune_adulte = train_df[(train_df['Age']>15) & (train_df['Age'] >= 30)]
df_jeunes_adultes_vivant = df_jeune_adulte[df_jeune_adulte.Survived == 'Alive']

df_adulte = train_df[(train_df['Age']>30) & (train_df['Age'] >= 50)]
df_adultes_vivant = df_adulte[df_adulte.Survived == 'Alive']

df_vieux =  train_df[(train_df['Age']>50)]
df_vieux_vivant = df_vieux[df_vieux.Survived == 'Alive']

fig1_train = px.histogram(
                x= age_train_liste,
                title='train set (177 Na (19.86%) replace by 28 yo)'
                )

fig2_complete = px.histogram(
                x= age_complete_liste,
                title='complete set (263 Na (20%) replace by 28 yo)'
                )

fig3_complete = px.histogram(
                x= age_train_liste,
                color= train_df['Survived'],
                title='complete set (263 Na (20%) replace by 28 yo)'
                
                )

fig4 = px.histogram(
                x= train_dropped,
                title='train set droped Na',
                )
fig5 = px.histogram(
                x= complete_dropped,
                title='complete set droped Na'
                )

fig4.update_yaxes(range=[0, 250])
fig5.update_yaxes(range=[0, 400])

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
                 html.Div([
              html.Div([
                      dcc.Graph(figure=fig4)
                      ],className='six columns'),
              
               html.Div([
                      dcc.Graph(figure=fig5)
                      ],className='six columns'),        
              
                ], className='row'),
    
    
         dcc.Graph(figure=fig3_complete),
         html.H5('taux de mortalité de 0 à 15 ans : 41%'),
         html.H5('taux de mortalité de 15 à 30 ans : 59%'),
         html.H5('taux de mortalité de 30 à 50 ans : 64%'),
         html.H5('taux de mortalité pour les + de 50 ans : 66%'),
          
          ])
