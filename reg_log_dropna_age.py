# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:47:54 2020

@author: MonOrdiPro
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score, roc_curve, auc
from sklearn.metrics import *
import sklearn.metrics as metrics


df_train = pd.read_csv('train.csv')
df_train.info()

# Cabin ne contient que 204 données / 891 (23%)-> on supprime la colonne
df_train.drop('Cabin', axis=1, inplace=True)
df_train.info()

# on supprime les lignes contenant des na
df_train.dropna(axis=0, how='any', inplace = True)
df_train.info()

# on supprime les colonnes sans grands interets
del df_train['PassengerId']
del df_train['Ticket']
del df_train['Name']

# on transforme les colonnes categorielles :
dummy = pd.get_dummies(df_train['Sex'])
df_train = pd.concat([df_train, dummy], axis=1)

dummy2 = pd.get_dummies(df_train['Embarked'])
df_train = pd.concat([df_train, dummy2], axis=1)

del df_train['Sex']
del df_train['Embarked']

# definition de X et y
y = df_train.Survived
del df_train['Survived']
X = df_train


#application de la regression logistique :
reg_log = LogisticRegression(solver='newton-cg')

res=0
for i in range (1,1000) :
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None)
    reg_log.fit(X_train, y_train)
    y_pred = reg_log.predict(X_test)
    reg_log.score(X_test, y_test)
    res += reg_log.score(X_test, y_test)

print(res/1000) #lblinear .792 | newton-cg .795 |


cm = confusion_matrix(y_test, y_pred)
cm = pd.DataFrame(cm, columns=['prédit ' + str(_) for _ in reg_log.classes_])
cm.index = ['vrai ' + str(_) for _ in reg_log.classes_]
cm


proba = reg_log.predict_proba(X)
fpr0, tpr0, thresholds0 = roc_curve(y, proba[:, 0], pos_label=reg_log.classes_[0], drop_intermediate=False)
thresholds0.shape

tp = pd.DataFrame(dict(fpr=fpr0, tpr=tpr0, threshold=thresholds0))
tp.drop(0, axis=0, inplace=True)
tp.head()

ax = tp.plot(x="threshold", y=['fpr', 'tpr'], figsize=(6,6))
ax.set_title("Evolution de FPR, TPR\nen fonction du seuil au delà duquel\n" + 
             "la réponse du classifieur est validée");
             
fig, ax = plt.subplots(1, 1, figsize=(6,6))
ax.plot([0, 1], [0, 1], 'k--')
aucf = auc(fpr0, tpr0)
ax.plot(fpr0, tpr0, label='auc=%1.5f' % aucf)
ax.set_title('Courbe ROC')
ax.text(0.5, 0.3, "plus mauvais que\nle hasard dans\ncette zone")
ax.legend();


precision, recall, thresholds = precision_recall_curve(y, proba[:, 0], pos_label=reg_log.classes_[0])

pr = pd.DataFrame(dict(precision=precision, recall=recall, 
                             threshold=[0] + list(thresholds)))

ax = pr.plot(x="threshold", y=['precision', 'recall'], figsize=(6,6))
ax.set_title("Evolution de la précision et du rappel\nen fonction du seuil au delà duquel\n" + 
             "la réponse du classifieur est validée");

roc_auc = metrics.auc(fpr0, tpr0)
plt.title('Receiver Operating Characteristic')
plt.plot(fpr0, tpr0, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
#plt.axis('off')

plt.show()            
             
modele_logit = LogisticRegression(penalty='none',solver='newton-cg')
modele_logit.fit(X_train,y_train)          
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred, average =None))
print("Recall:",metrics.recall_score(y_test, y_pred, average =None))
print("odds-ratio = \n"+  str(modele_logit.coef_))
modele_logit



             
             