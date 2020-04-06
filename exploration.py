# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:53:08 2020

@author: utilisateur
"""
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt




"""
#########################################################################################
#######################  Création d'un dataSet unique  ##################################
#######################     Preparation des données    ##################################
#########################################################################################
df1 = pd.read_csv('gender_submission.csv')
df2 = pd.read_csv('test.csv')
df3 = pd.read_csv('train.csv')

# on rajoute la colonne survived de DF1 a DF2
df2['Survived'] = df1['Survived']

# on concatene nos deux dataFrames en un seul DF unique
complete_df = pd.concat([df3,df2], sort=False)

complete_df.info()

# Cabin ne contient que 295 données / 1309 -> on supprime la colonne
complete_df.drop('Cabin', axis=1, inplace=True)


# On profile le restant de nos données
profile = ProfileReport(df, title='Pandas Profiling Report', html={'style':{'full_width':True}})

# enregistrement du profile en html
profile.to_file(output_file="your_report.html")

# la colonne age contient 263 données manquantes on choisit de les remplacé par la medianne (28)
# on testera par la suite eventuellement par la moyenne
#moy_age = df.Age.mean()
med_age = df.Age.median()

df['Age'].fillna(med_age, inplace = True)
df = df.dropna()

df.describe()

# on enregistre notre dataframe finale
df.to_csv('complete_dataframe.csv', index = False)
"""


df = pd.read_csv('complete_dataframe.csv')


#########################################################################################
#######################       Regression linéaire      ##################################
#########################################################################################


modeleReg=LinearRegression()

y = df.Survived

# gestion de la colonne sex -> variable quantitative :

dummy = pd.get_dummies(df['Sex'])
df = pd.concat([df, dummy], axis=1)

dummy2 = pd.get_dummies(df['Embarked'])
df = pd.concat([df, dummy2], axis=1)


X = df.drop(['Survived', 'Name', 'Sex', 'PassengerId', 'Ticket', 'Embarked'], axis=1)
#X = df[['Fare', 'Pclass']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None)
"""
from sklearn.preprocessing import StandardScaler
X_train = StandardScaler().fit_transform(X_train.values.reshape(-1, 1))
"""
modeleReg.fit(X_train,y_train)


print(modeleReg.intercept_)
print(modeleReg.coef_)

#calcul du R²
modeleReg.score(X_test,y_test)

RMSE=np.sqrt(((y_test-modeleReg.predict(X_test))**2).sum()/len(y_test))

plt.plot(y_test, modeleReg.predict(X_test),'.')
plt.show()

plt.plot(y_test, y_test-modeleReg.predict(X_test),'.')
plt.show()


