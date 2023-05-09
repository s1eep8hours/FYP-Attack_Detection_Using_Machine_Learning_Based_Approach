import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#读取训练集，并且训练模型
print("Training IDS...")
dataset_file_name = ".\Dataset\Car_Hacking.csv"
raw_data = pd.read_csv(dataset_file_name, header=None, low_memory=False)
features = raw_data.iloc[:, :raw_data.shape[1] - 1]
labels = raw_data.iloc[:, raw_data.shape[1] - 1:]
labels = labels.values.ravel()
clf = DecisionTreeClassifier()
IDS = clf.fit(features, labels)

#读取存有网络流量数据的文件，
print("Receiving Network Traffic...")
df = pd.read_csv(".\\network traffic.csv", header=None, low_memory=False)
with open(".\\network traffic.csv") as file:
    traffic = file.readlines()

#对包数据进行预处理
df = df.iloc[: , 1:]
df = df.drop(2, axis=1)
row = df.shape[0]
for i in range(row):
    df[1][i] = int(df[1][i], 16)
    for j in range(3,11):
        df[j][i] = int(df[j][i], 16)

#检测攻击，并将发出警报
print("Detecting...")
with open("./Alert.txt", "w") as alert:
    for i in range(row):
        result = clf.predict(np.array(df.iloc[i]).reshape(1, -1))
        if result.item() == 0:
            print("This is a normal access")
        else:
            print("This is an attack")
            alert.write(traffic[i])


