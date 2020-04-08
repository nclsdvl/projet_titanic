# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:59:26 2020

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





class_1 = train_df[train_df.Pclass == 1]
class_2 = train_df[train_df.Pclass == 2]
class_3 = train_df[train_df.Pclass == 3]

dead_c1 = len(class_1[class_1.Survived == "Dead"]) #80 --> 37.04%
dead_c2 = len(class_2[class_2.Survived == "Dead"]) #97 --> 52.72%
dead_c3 = len(class_3[class_3.Survived == "Dead"]) #372--> 75.76%

class_train_list = train_df['Pclass']
class_complete_list = complete_df['Pclass']

fig1_train = px.histogram(
                x= class_train_list,
                title='train set Embarked'
                )
fig1_train.update_layout(xaxis_type='category')

fig2_complete = px.histogram(
                x= class_complete_list,
                title='complete set Embarked'
                )
fig2_complete.update_layout(xaxis_type='category')

fig3 = px.histogram(
                x=  class_train_list,
                labels=['Dead','Alive'],
                color= train_df['Survived'],
                title="nombre mort par rapport au port d'embarquement",
                )
fig3.update_layout(xaxis_type='category')


fig_finale = px.bar(
                     x=['premiere classe','deuxieme classe','troisieme classe'],
                     y=[37,53,75],
                     )
fig_finale.update_xaxes(title='premiere, deuxieme ou troisieme classe')
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
          dcc.Graph(figure=fig3),
          dcc.Graph(figure=fig_finale),
          ])
    
    
"""
         html.H5('taux de mortalité pour une premiere classe : 37.04%'),
         html.H5('taux de mortalité pour une seconde classe  : 52.72%'),
         html.H5('taux de mortalité pour une troisieme classe : 75.76%'),
"""