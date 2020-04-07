# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:56:28 2020

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

train_df['Embarked'].fillna('S', inplace=True)

s_train = train_df[train_df.Embarked == 'S']
c_train = train_df[train_df.Embarked == 'C']
q_train = train_df[train_df.Embarked == 'Q']

emb_train_list = train_df['Embarked']
emb_complete_list = complete_df['Embarked']

dead_s = len(s_train[s_train.Survived == "Dead"])
dead_q = len(q_train[q_train.Survived == "Dead"])
dead_c = len(c_train[c_train.Survived == "Dead"])

fig1_train = px.histogram(
                x= emb_train_list,
                title='train set Embarked'
                )
fig2_complete = px.histogram(
                x= emb_complete_list,
                title='complete set Embarked'
                )

fig3 = px.histogram(
                x=  emb_train_list,
                labels=['Dead','Alive'],
                color= train_df['Survived'],
                title="nombre mort par rapport au port d'embarquement",
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
          dcc.Graph(figure=fig3),
         html.H5('taux de mortalité pour un embarquement à Southampton : 66.01%'),
         html.H5('taux de mortalité pour un embarquement à Queenstown : 61.04%'),
         html.H5('taux de mortalité pour un embarquement à Cherbourg : 44.64%'),
          ])