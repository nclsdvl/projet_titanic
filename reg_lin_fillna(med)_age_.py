# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 07:55:45 2020

@author: MonOrdiPro
"""

import pandas as pd
from pandas_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing


df_train = pd.read_csv('train.csv')

df_train.info()

# Cabin ne contient que 204 données / 891 (23%)-> on supprime la colonne
df_train.drop('Cabin', axis=1, inplace=True)

df_train.info()

# il manque 177 age soit 19.86%
print(df_train.Age.isna().sum()) # -> 177
# on remplace les na par la mediane
med_age = df_train.Age.median()
df_train['Age'].fillna(28, inplace = True)

df_train.info()
# il reste deux ligne ou embarked n'est pas renseigné
# on supprime ces deux lignes
df_train.dropna(axis=0, how='any', inplace = True)
df_train.info()


modeleReg=LinearRegression()

y = df_train.Survived

# gestion de la colonne sex -> variable quantitative :

dummy = pd.get_dummies(df_train['Sex'])
df_train = pd.concat([df_train, dummy], axis=1)

dummy2 = pd.get_dummies(df_train['Embarked'])
df_train = pd.concat([df_train, dummy2], axis=1)


X = df_train.drop(['Survived', 'Name', 'Sex', 'PassengerId', 'Ticket', 'Embarked'], axis=1) # R²=0.37

#X = df_train[['Pclass','Age','Fare', 'C', 'Q','S']] # R² = 0.15

r2 = 0
for i in range (0,1000) :
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None)

    modeleReg.fit(X_train,y_train)
    r2 += modeleReg.score(X_test,y_test)
    
print(r2/1000)



"""
print(modeleReg.intercept_)
print(modeleReg.coef_)

#calcul du R²
modeleReg.score(X_test,y_test)

RMSE=np.sqrt(((y_test-modeleReg.predict(X_test))**2).sum()/len(y_test))

plt.plot(y_test, modeleReg.predict(X_test),'.')
plt.show()

plt.plot(y_test, y_test-modeleReg.predict(X_test),'.')
plt.show()

"""

