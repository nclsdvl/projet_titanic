# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 06:15:43 2020

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



train_homme = train_df[train_df['Sex']=='male']
train_femme = train_df[train_df['Sex']=='female']

train_nb_h = len(train_homme)
train_nb_f = len(train_femme)

complete_nb_h = len(complete_df[complete_df['Sex']=='male'])
complete_nb_f = len(complete_df[complete_df['Sex']=='female'])


nb_h_mort = len(train_homme[train_homme['Survived']=='Dead'])
nb_f_mort = len(train_femme[train_femme['Survived']=='Dead'])

nb_h_vivant = train_nb_h - nb_h_mort
nb_f_vivant = train_nb_f - nb_f_mort


fig1_train = px.pie(values=[train_nb_h, train_nb_f], 
                    labels=['Homme','Femme'],
                    names = ['Homme','Femme'],
                    color_discrete_sequence=['#4169E1', '#DB7093'],
                    title='Proportion Homme Femme Training Set',
                    )


fig2_complete = px.pie(values=[complete_nb_h, complete_nb_f], 
                       labels=['Homme','Femme'], 
                       names = ['Homme','Femme'],
                       color_discrete_sequence=['#4169E1', '#DB7093'],
                       title='Proportion Homme Femme complete Set',
                       )





fig3 = px.pie(values=[nb_h_mort, nb_h_vivant], 
              labels=['Dead','Alive'],
              names = ['mort','vivant'],
              color_discrete_sequence=['#F08080','#2E8B57' ],
              title='Proportion Homme Mort / Vivant',
              )
fig4 = px.pie(values=[nb_f_mort, nb_f_vivant],
              labels=['Dead','Alive'],
              names = ['mort','vivant'],
              color_discrete_sequence=['#2E8B57', '#F08080'],
              title='Proportion Femme Mort / Vivant')








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
                      dcc.Graph(figure=fig3)
                      ],className='six columns'),
              
               html.Div([
                      dcc.Graph(figure=fig4)
                      ],className='six columns')         
              
                ], className='row'),
          
          ])
