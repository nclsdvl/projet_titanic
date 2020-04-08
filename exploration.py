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
import random




#########################################################################################
#######################  Création d'un dataSet unique  ##################################
#######################     Preparation des données    ##################################
#########################################################################################
#df_exemple = pd.read_csv('gender_submission.csv')
#df_prediction = pd.read_csv('test.csv')
df_train = pd.read_csv('train.csv')




df_train.info()

# Cabin ne contient que 204 données / 891 (23%)-> on supprime la colonne
df_train.drop('Cabin', axis=1, inplace=True)



# il manque 177 age soit 19.86%
print(df_train.Age.isna().sum()) # -> 177


#création d'un vecteur age correspondant aux decile de notre distribution
print(pd.qcut(df_train.Age,10).unique())
#[(0.419, 14.0] < (14.0, 19.0] < (19.0, 22.0] < (22.0, 25.0] < (25.0, 28.0] <
# (28 31] (31.8, 36.0] < (36.0, 41.0] < (41.0, 50.0] < (50.0, 80.0]]


s = [random.randint(0, 15) for i in range(17)]
s += [random.randint(15, 19) for i in range(17)]
s += [random.randint(19, 22) for i in range(18)]
s += [random.randint(22, 25) for i in range(18)]
s += [random.randint(25, 28) for i in range(18)]
s += [random.randint(28, 32) for i in range(18)]
s += [random.randint(32, 36) for i in range(18)]
s += [random.randint(36, 41) for i in range(18)]
s += [random.randint(41, 50) for i in range(18)]
s += [random.randint(50, 80) for i in range(17)]




# On profile le restant de nos données
#complete_profile = ProfileReport(complete_df, title='complete Profiling Report', html={'style':{'full_width':True}})
#train_profile =  ProfileReport(df_train, title='training Profiling Report', html={'style':{'full_width':True}})
# enregistrement du profile en html
#complete_profile.to_file(output_file="complete_report.html")
#train_profile.to_file(output_file="train_report.html")


# la colonne age contient 263 données manquantes on choisit de les remplacé par la medianne (28)
# on testera par la suite eventuellement par la moyenne
#moy_age = complete_df.Age.mean()
#med_age = complete_df.Age.median()





#df.describe()

# on enregistre notre dataframe finale
#complete_df.to_csv('complete_dataframe.csv', index = False)
#df_train.to_csv('train_dataframe.csv', index = False)





#########################################################################################
#######################       Regression linéaire      ##################################
#########################################################################################
train_df = pd.read_csv('train_dataframe.csv')

"""
# A REVOIR

train_df['Age'].fillna(28, inplace = True)
train_df = df_train.dropna()

complete_df['Age'].fillna(s, inplace = True)
complete_df = complete_df.dropna()
"""


modeleReg=LinearRegression()

y = train_df.Survived

# gestion de la colonne sex -> variable quantitative :

dummy = pd.get_dummies(train_df['Sex'])
train_df = pd.concat([train_df, dummy], axis=1)

dummy2 = pd.get_dummies(train_df['Embarked'])
train_df = pd.concat([train_df, dummy2], axis=1)


X = train_df.drop(['Survived', 'Name', 'Sex', 'PassengerId', 'Ticket', 'Embarked'], axis=1)
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


