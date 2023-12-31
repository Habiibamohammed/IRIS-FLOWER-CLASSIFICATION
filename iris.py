# -*- coding: utf-8 -*-
"""IRIS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VcL22dZT-w7EooI3I64rFLyJiWIMgyM2
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('/content/IRIS.csv')
data.head()

# to display stats about data
data.describe()

# to basic info about datatype
data.info()

# to display no. of samples on each class
data['species'].value_counts()

# check for null values
data.isnull().sum()

"""Exploratory Data Analysis"""

# histograms
data['sepal_length'].hist()

data['sepal_width'].hist()

data['petal_length'].hist()

data['petal_width'].hist()

# scatterplot
colors = ['pink', 'yellow', 'black']
species = ['Iris-virginica','Iris-versicolor','Iris-setosa']

for i in range(3):
    x = data[data['species'] == species[i]]
    plt.scatter(x['sepal_length'], x['sepal_width'], c = colors[i], label=species[i])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()

data.corr()

"""Label Encoder"""

le = LabelEncoder()

data['species'] = le.fit_transform(data['species'])
data.head()

"""Model Training"""

X = data.drop(columns=['species'])
Y = data['species']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)

model = LogisticRegression()
model.fit(x_train, y_train)

# Print accuracy
accuracy = model.score(x_test, y_test) * 100
print("Accuracy: ", accuracy)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Create a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)  # You can adjust the number of estimators as needed

# Train the Random Forest model
rf_model.fit(x_train, y_train)

# Make predictions
y_pred = rf_model.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred) * 100
print("Accuracy: {:.2f}%".format(accuracy))





