# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:13:19 2020

@author: MonOrdiPro
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.graph_objs import *
from dash.dependencies import Input, Output
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import tab_age as tab_age
import tab_sexe as tab_sexe
import tab_sibling as tab_sibling
import tab_parch as tab_parch
import tab_fare as tab_fare
import tab_embarked as tab_embarked
import tab_Pclass as tab_Pclass
import tab_correlation as tab_correlation

complete_df = pd.read_csv('complete_dataframe.csv')
train_df = pd.read_csv('train_dataframe.csv')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div([
            html.H1(children ='Titanic Dash',
                    style={
                        'textAlign': 'center',}),
            html.Hr(),
            html.Br(),
            dcc.Tabs(id="tabs", value='Age', children=[
                dcc.Tab(label='Age', value='Age'),
                dcc.Tab(label='Sexe', value='Sexe'),
                dcc.Tab(label='Sibling', value='Sibling'),
                dcc.Tab(label='Parch', value='Parch'),
                dcc.Tab(label='Fare', value='Fare'),
                dcc.Tab(label='Embarked', value='Embarked'),
                dcc.Tab(label='Pclass', value='Pclass'),
                dcc.Tab(label='Correlation', value='Correlation')
            ]),
            html.Div(id='tabs-content')
            ])
        


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'Age':
        return tab_age.get_content()
    elif tab == 'Sexe':
        return tab_sexe.get_content()
    elif tab == 'Sibling':
        return tab_sibling.get_content()
    elif tab == 'Parch' :
        return tab_parch.get_content()
    elif tab == 'Fare' :
        return tab_fare.get_content()
    elif tab == 'Embarked' :
        return tab_embarked.get_content()
    elif tab == 'Pclass' :
        return tab_Pclass.get_content()
    elif tab == 'Correlation' :
        return tab_correlation.get_content()

if __name__ == '__main__':

    app.run_server(debug=True, use_reloader=False)
