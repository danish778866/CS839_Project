#Reference : https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/

import numpy as np  
import pandas as pd  
import os
from sklearn.model_selection import train_test_split  
from sklearn.svm import SVC 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score  

def find_inaccurate(Y_pred, Y_test, x_test) :
    for yp, yt, xt in zip(Y_pred, Y_test, x_test):
        if yp!=yt:
            print (xt[0:3], yt, yp)

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
features_csv = project_dir + os.sep + "data" + os.sep + "features" + os.sep + "features.csv"
labels_csv = project_dir + os.sep + "data" + os.sep + "labels" + os.sep + "labels.csv"
feature_vector = pd.read_csv(features_csv)
labels = pd.read_csv(labels_csv)
x = feature_vector.values
y = labels.values
x_train, x_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0)
X_train = x_train[:,3:]
X_test = x_test[:,3:]
#classifier = 'poly' or 'rbf' for gaussian or 'sigmoid'
svclassifier = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='scale', kernel='poly',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False) 
svclassifier.fit(X_train, Y_train.ravel())
Y_pred = svclassifier.predict(X_test)

print("...Confusion Matrix...")
print(confusion_matrix(Y_test,Y_pred))
print("...Classification Report...")
print(classification_report(Y_test,Y_pred))
print("...Accuracy Score...")
print(accuracy_score(Y_test, Y_pred))
find_inaccurate(Y_pred, Y_test, x_test)
