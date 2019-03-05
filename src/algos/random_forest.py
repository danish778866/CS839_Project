#Reference : https://stackabuse.com/random-forest-algorithm-with-python-and-scikit-learn/
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

dataset = pd.read_csv("/Users/somya/Desktop/sem2/CS839_Project/data/features/features.csv")
labels = pd.read_csv("/Users/somya/Desktop/sem2/CS839_Project/data/labels/all_labels.csv")

X = dataset.values
y = labels.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
sc = StandardScaler()  
X_train = sc.fit_transform(X_train)  
X_test = sc.transform(X_test)  
regressor = RandomForestRegressor(n_estimators=20, random_state=0)  
regressor.fit(X_train, y_train.ravel())
y_pred = regressor.predict(X_test)
thresh = []
for yi in y_pred:
    if yi<0.5:
        thresh.append(0)
    else:
        thresh.append(1)

print(confusion_matrix(y_test,thresh))
print(classification_report(y_test,thresh))
print(accuracy_score(y_test, thresh))

