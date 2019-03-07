#Reference : https://stackabuse.com/random-forest-algorithm-with-python-and-scikit-learn/
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
features_csv = project_dir + os.sep + "data" + os.sep + "features" + os.sep + "features.csv" 
labels_csv = project_dir + os.sep + "data" + os.sep + "labels" + os.sep + "labels.csv"
feature_vector = pd.read_csv(features_csv)
labels = pd.read_csv(labels_csv)
x = feature_vector.values
y = labels.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
X_train = x_train[:,3:]
X_test = x_test[:,3:]
classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(X_train, y_train.ravel())
y_pred = classifier.predict(X_test)
print("...Confusion Matrix...")
print(confusion_matrix(y_test,y_pred))
print("...Classification Report...")
print(classification_report(y_test,y_pred))
print("...Accuracy Score...")
print(accuracy_score(y_test, y_pred))

