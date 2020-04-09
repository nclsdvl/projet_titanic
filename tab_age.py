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


#################################################################
#Preparation des données

train_df = pd.read_csv('train_dataframe.csv')
complete_df = pd.read_csv('complete_dataframe.csv')

train_na_age = len(train_df[train_df['Age'].isna()])
complete_na_age = len(complete_df[complete_df['Age'].isna()])

complete_df['Survived'].replace({0:'Dead', 1:'Alive'}, inplace = True)
train_df['Survived'].replace({0:'Dead', 1:'Alive'}, inplace = True)

train_dropped = train_df['Age'].dropna()
train_dropped_cplt = train_df.dropna()
complete_dropped = complete_df['Age'].dropna()

train_df_ffill = train_df
train_df_ffill = train_df_ffill.fillna(method='ffill') 

complete_ffill = complete_df
complete_ffill = complete_ffill.fillna(method='ffill') 

train_df['Age'].fillna(28, inplace = True)
complete_df['Age'].fillna(28, inplace = True)



################################################################
#print(pd.qcut(train_df['Age'],10).unique())
print(pd.qcut(train_df.Age,duplicates='drop',q=7).unique())

age_train_liste = train_df['Age']
age_complete_liste = complete_df['Age']
age_ffill = train_df_ffill['Age']
age_complete_ffill = complete_ffill['Age']

# age fillna by med
septile1_med = train_df[train_df.Age < 18]
septile2_med = train_df[(train_df.Age >= 18) & (train_df.Age <= 24)]
septile3_med = train_df[(train_df.Age > 24) & (train_df.Age <= 28)]
septile4_med = train_df[(train_df.Age > 28) & (train_df.Age <= 33)]
septile5_med = train_df[(train_df.Age > 33) & (train_df.Age <= 43)]
septile6_med = train_df[(train_df.Age > 43)]

septile1_med_dead = len(septile1_med[septile1_med.Survived=='Dead']) #46
septile2_med_dead = len(septile2_med[septile2_med.Survived=='Dead']) #75
septile3_med_dead = len(septile3_med[septile3_med.Survived=='Dead']) #72
septile4_med_dead = len(septile4_med[septile4_med.Survived=='Dead']) #70
septile5_med_dead = len(septile5_med[septile5_med.Survived=='Dead']) #72
septile6_med_dead = len(septile6_med[septile6_med.Survived=='Dead']) #62

mortalite_y_med = [46,75,72,70,72,62]
interv_x_med = ['0-18','18-24','24-28','28-33','33-43','43-90']


# age drpped
print(pd.qcut(train_dropped_cplt.Age,duplicates='drop',q=6).unique())

septile1_drp = train_dropped_cplt[train_dropped_cplt.Age < 18]
septile2_drp = train_dropped_cplt[(train_dropped_cplt.Age >= 18) & (train_dropped_cplt.Fare <= 23)]
septile3_drp = train_dropped_cplt[(train_dropped_cplt.Age > 23) & (train_dropped_cplt.Fare <= 28)]
septile4_drp = train_dropped_cplt[(train_dropped_cplt.Age > 28) & (train_dropped_cplt.Fare <= 34)]
septile5_drp = train_dropped_cplt[(train_dropped_cplt.Age > 34) & (train_dropped_cplt.Fare <= 44)]
septile6_drp = train_dropped_cplt[(train_dropped_cplt.Age > 44)]

septile1_drp_dead = len(septile1_drp[septile1_drp.Survived=='Dead']) #46
septile2_drp_dead = len(septile2_drp[septile2_drp.Survived=='Dead']) #74
septile3_drp_dead = len(septile3_drp[septile3_drp.Survived=='Dead']) #70
septile4_drp_dead = len(septile4_drp[septile4_drp.Survived=='Dead']) #70
septile5_drp_dead = len(septile5_drp[septile5_drp.Survived=='Dead']) #74
septile6_drp_dead = len(septile6_drp[septile6_drp.Survived=='Dead']) #62

mortalite_y_drp = [46,74,70,70,74,63]
interv_x_drp = ['0-18','18-23','23-28','28-34','34-44','44-90']





nb_mineur = train_df[(train_df['Age']<18)]
nb_mineur_alive = len(nb_mineur[nb_mineur['Survived']=='Alive'])
nb_mineur_dead = len(nb_mineur[nb_mineur['Survived']=='Dead'])

nb_adulte = train_df[(train_df['Age']>=18)]
nb_adulte_alive = len(nb_adulte[nb_adulte['Survived']=='Alive'])
nb_adulte_dead = len(nb_adulte[nb_adulte['Survived']=='Dead'])
###################################################################




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

fig_ffill = px.histogram(
                x= age_ffill,
                title='train set with ffill method'
                )

fig_complete_ffill = px.histogram(
                x= age_complete_ffill,
                title='train set with ffill method'
                )
fig_ffill.update_yaxes(range=[0, 250])
fig_complete_ffill.update_yaxes(range=[0, 400])



fig_min = px.pie(values=[nb_mineur_alive, nb_mineur_dead], 
                    labels=['survivant','mort'],
                    names = ['survivant','mort'],
                    color_discrete_sequence=['#DB7093', '#4169E1'],
                    title='Proportion mineur Mort / Survivant Training Set',
                    )
fig_adulte = px.pie(values=[nb_adulte_alive, nb_adulte_dead], 
                    labels=['survivant','mort'],
                    names = ['survivant','mort'],
                    color_discrete_sequence=['#4169E1', '#DB7093'],
                    title='Proportion adulte Mort / Survivant Training Set',
                    )



fig_finale_fill = px.bar(
                     x=interv_x_med,
                     y=mortalite_y_med,
                     text=mortalite_y_med,
                     title="mortalité par tranche d'age avec la methode fillna Medianne")
fig_finale_fill.update_xaxes(title="Interval d'age (en sixtile)")
fig_finale_fill.update_yaxes(title='Mortalité en pourcentage')
fig_finale_fill.update_traces( textposition='inside')

fig_finale_drp = px.bar(train_df,
                     x=interv_x_drp,
                     y=mortalite_y_drp,
                     text=mortalite_y_drp,
                     title="mortalité par tranche d'age avec la methode dropna")
fig_finale_drp.update_xaxes(title="Interval d'age (en sixtile)")
fig_finale_drp.update_yaxes(title='Mortalité en pourcentage')
fig_finale_drp.update_traces(textposition='inside')

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
    
                 html.Div([
              html.Div([
                      dcc.Graph(figure=fig_ffill)
                      ],className='six columns'),
              
               html.Div([
                      dcc.Graph(figure=fig_complete_ffill)
                      ],className='six columns'),        
              
                ], className='row'),    
    
            html.Div([
                  html.Div([
                      dcc.Graph(figure=fig_min)
                      ],className='six columns'),
              
               html.Div([
                      dcc.Graph(figure=fig_adulte)
                      ],className='six columns')         
              
                ], className='row'),
    
    

         
         
         
         dcc.Graph(figure=fig3_complete),
         dcc.Graph(figure=fig_finale_fill),
         dcc.Graph(figure=fig_finale_drp),

          
          ])
