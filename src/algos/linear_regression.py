# Run this program on your local python 
# interpreter, provided you have installed 
# the required libraries.

#Reference : https://www.geeksforgeeks.org/decision-tree-implementation-python/
  
# Importing the required packages 
import numpy as np 
import pandas as pd 
import os
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn import linear_model
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
  
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
features_csv = project_dir + os.sep + "data" + os.sep + "features" + os.sep + "features.csv" 
labels_csv = project_dir + os.sep + "data" + os.sep + "labels" + os.sep + "labels.csv"
feature_vector = pd.read_csv(features_csv)
labels = pd.read_csv(labels_csv)
x = feature_vector.values
y = labels.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100) 
X_train = x_train[:, 3:]
X_test = x_test[:, 3:]
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train.ravel()) 
y_pred = regr.predict(X_test) 
y_pred_classify = []
for pred in y_pred:
    if pred > 0.5:
        y_pred_classify.append(1)
    else:
        y_pred_classify.append(0)
print("...Confusion Matrix...")
print(confusion_matrix(y_test,y_pred_classify))
print("...Classification Report...")
print(classification_report(y_test,y_pred_classify))
print("...Accuracy Score...")
print(accuracy_score(y_test, y_pred_classify))
