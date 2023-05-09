import sys
import time
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, zero_one_loss
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

data = input("\nChoose a dataset:\nNSL-KDD : 1\nCICIDS 2017 : 2\nCar-Hacking : 3\n")
if data == "1":
    from DataPreprocess_KDD import X_train, X_test, y_train, y_test
elif data == "2":
    from DataPreprocess_CICIDS import X_train, X_test, y_train, y_test
elif data == "3":
    from DataPreprocess_Car import X_train, X_test, y_train, y_test
else:
    sys.exit()

model = input("\nChoose a model:\nDT : 1\nKNN : 2\nSVM : 3\nRF : 4\nNB : 5\nMLP : 6\n")
if model == "1":
    clf = DecisionTreeClassifier()
    clfName = "DT"
elif model == "2":
    clf = KNeighborsClassifier()
    clfName = "KNN"
elif model == "3":
    clf = LinearSVC()
    clfName = "SVM"
elif model == "4":
    clf = RandomForestClassifier()
    clfName = "RF"
elif model == "5":
    clf = MultinomialNB()
    clfName = "NB"
elif model == "6":
    clf = MLPClassifier(hidden_layer_sizes=(10,), alpha=0.01, max_iter=10000)
    clfName = "MLP"
else:
    sys.exit()


# 训练模型
t1 = time.time()

print("Training model " + clfName + ": " ,t1)


trained_model = clf.fit(X_train, y_train)


# 预测
t2 = time.time()
print("Predicting: " ,t2)
y_pred = clf.predict(X_test)
t3 = time.time()
print("Computing performance metrics: " ,t3)
results = confusion_matrix(y_test, y_pred)
print(results)
error = zero_one_loss(y_test, y_pred)
print(error)

# 根据混淆矩阵求预测精度
list_diag = np.diag(results)
list_raw_sum = np.sum(results, axis=1)
print("Training duration:", t2 - t1)
print("Predicting duration:", t3 - t2)
print("Predict accuracy of model " + clfName +" is", np.sum(list_diag) / np.sum(list_raw_sum))