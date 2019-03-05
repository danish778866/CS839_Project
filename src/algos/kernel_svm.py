#Reference : https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/

import numpy as np  
import pandas as pd  
import os
from sklearn.model_selection import train_test_split  
from sklearn.svm import SVC 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score  

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
features_csv = project_dir + os.sep + "data" + os.sep + "features" + os.sep + "features.csv" 
labels_csv = project_dir + os.sep + "data" + os.sep + "labels" + os.sep + "labels.csv"
feature_vector = pd.read_csv(features_csv)
labels = pd.read_csv(labels_csv)
x = feature_vector.values
y = labels.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
#classifier = 'poly' or 'rbf' for gaussian or ''sigmoid'
svclassifier = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False) 
svclassifier.fit(x_train, y_train.ravel())
y_pred = svclassifier.predict(x_test)  
print("...Confusion Matrix...")
print(confusion_matrix(y_test,y_pred))
print("...Classification Report...")
print(classification_report(y_test,y_pred))
print("...Accuracy Score...")
print(accuracy_score(y_test, y_pred))
