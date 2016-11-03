# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 17:20:04 2016

@author: S042285
"""

import numpy as np
import scipy
import pandas as pd
import matplotlib
import pylab as P
import io

df = pd.read_csv('kaggle titanic/train.csv',header=0)
df['Gender']=df['Sex'].map({'female':0,'male':1}).astype(int)
df['Depart']=4
df.loc[(df.Embarked=='C'),'Depart']=0
df.loc[(df.Embarked=='Q'),'Depart']=1
df.loc[(df.Embarked=='S'),'Depart']=2

median_ages=np.zeros((2,3))
for i in range(0,2):
	for j in range(0,3):
		median_ages[i,j]=df[(df['Gender']==i) & (df['Pclass']==j+1)]['Age'].dropna().median()

df['AgeFill']=df['Age']
for i in range(0,2):
	for j in range(0,3):
		df.loc[(df.Age.isnull())&(df.Gender ==i)&(df.Pclass==j+1),'AgeFill']=median_ages[i,j]

df['AgeIsNull']=pd.isnull(df.Age).astype(int)
df['FamilySize']=df['SibSp']+df['Parch']
df=df.drop(['Name','Sex','Ticket','Cabin','Embarked','Age','PassengerId'],axis=1)
train_data=df.values

dft = pd.read_csv('kaggle titanic/test.csv',header=0)
dft['Gender']=dft['Sex'].map({'female':0,'male':1}).astype(int)
dft['Depart']=4
dft.loc[(dft.Embarked=='C'),'Depart']=0
dft.loc[(dft.Embarked=='Q'),'Depart']=1
dft.loc[(dft.Embarked=='S'),'Depart']=2

median_ages=np.zeros((2,3))
for i in range(0,2):
	for j in range(0,3):
		median_ages[i,j]=dft[(dft['Gender']==i) & (dft['Pclass']==j+1)]['Age'].dropna().median()

dft['AgeFill']=dft['Age']
for i in range(0,2):
	for j in range(0,3):
		dft.loc[(dft.Age.isnull())&(dft.Gender ==i)&(dft.Pclass==j+1),'AgeFill']=median_ages[i,j]

dft.loc[dft['Fare'].isnull(),'Fare']=35 
dft['AgeIsNull']=pd.isnull(dft.Age).astype(int)
dft['FamilySize']=dft['SibSp']+dft['Parch']
dft=dft.drop(['Name','Sex','Ticket','Cabin','Embarked','Age'],axis=1)


ids = dft.PassengerId.values
dft=dft.drop(['PassengerId'],axis=1)
test_data = dft.values

from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier(n_estimators = 20)
forest=forest.fit(train_data[0::,1::],train_data[0::,0])
output = forest.predict(test_data)

with io.open('kaggle titanic/sub4.csv','wb') as csv_out:
    csv_writer=csv.writer(csv_out)
    csv_writer.writerow(['PassengerId','Survived'])
    csv_writer.writerows(zip(ids,output.astype(int)))
