# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:04:08 2020

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
import os

train_df = pd.read_csv('train_dataframe.csv')
complete_df = pd.read_csv('complete_dataframe.csv')


col = list(train_df.columns)
data = [train_df.corr('spearman')]


image_filename = os.path.join(os.getcwd(), './corr_spearman.JPG')



def get_content():
  return html.Div([
         html.Img(src=image_filename)

          ])