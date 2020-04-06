# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:13:19 2020

@author: MonOrdiPro
"""

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.graph_objs import *

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('complete_dataframe.csv')
df['Survived'].replace({0:'Dead', 1:'Alive'}, inplace = True)



surviveH = df[df['Sex']=="male"]['Survived']
surviveF = df[df['Sex']=="female"]['Survived']



fig = px.histogram(df, x="Age", color="Survived")


fig2 = go.Figure(data=[go.Pie(labels=df.Sex)])

"""
fig3 = go.Figure(data=[go.Pie(labels=surviveH)])


fig4 = go.Figure(data=[go.Pie(labels=surviveF)])

"""

fig3 = {
    'data': [{'labels': ['Dead', 'Alive'],
              'values': [19, 26, 55],
              'type': 'pie',
              'sort': False,
              'marker': {'colors': ['rgb(255, 0, 0)',
                                    'rgb(0, 255, 0)',
                                    'rgb(0, 0, 255)']
                        }
            }]
     }

fig4 = {
    'data': [{'labels': ['Residential', 'Non-Residential', 'Utility'],
              'values': [100, 10, 25],
              'type': 'pie',
              'sort': False,
              'marker': {'colors': ['rgb(255, 0, 0)',
                                    'rgb(0, 255, 0)',
                                    'rgb(0, 0, 255)']
                        }
            }]
     }






external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div([
            html.H1(children ='Titanic Dash',
                    style={
                        'textAlign': 'center',}),
            html.Hr(),
            html.Br(),
            html.Div([
                html.H3(children = 'Variable age',
                    style={
                        'textAlign': 'center'}),
                    dcc.Graph(id='g1', figure=fig)
                ]),
           html.Div([
               html.H3(children = 'Repartition des voyageurs par genre',
                    style={
                        'textAlign': 'center'}),
                    dcc.Graph(id='g2', figure=fig2)
                ]),


            html.Div([
                html.Div([
                    html.H3(children = 'survie chez les Hommes',
                    style={
                        'textAlign': 'center'}),
                    dcc.Graph(id='g3', figure=fig3)
                    
                    ],className="six columns"),
               html.Div([
                    html.H3(children = 'Survie chez les femmes',
                    style={
                        'textAlign': 'center'}),
                    dcc.Graph(id='g4', figure=fig4)
                    
                    ],className="six columns"),

            ], className="row",)    
    
    
    ])
        





if __name__ == '__main__':

    app.run_server(debug=True, use_reloader=False)
