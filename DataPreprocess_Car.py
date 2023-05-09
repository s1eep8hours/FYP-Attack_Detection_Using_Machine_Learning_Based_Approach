import pandas as pd
from sklearn.model_selection import train_test_split




# 加载数据
dataset_file_name = ".\Dataset\Car_Hacking.csv"
print("Loading raw data...")
raw_data = pd.read_csv(dataset_file_name, header=None, low_memory=False)





# 查看标签数据情况
last_column_index = raw_data.shape[1] - 1
print("print data labels:")
print(raw_data[last_column_index].value_counts())



# 对原始数据进行切片，分离出特征和标签
features = raw_data.iloc[:, :raw_data.shape[1] - 1]
labels = raw_data.iloc[:, raw_data.shape[1] - 1:]



# 将多维的标签转为一维的数组
labels = labels.values.ravel()

# 将数据分为训练集和测试集,并打印维数
df = pd.DataFrame(features)
X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.7, test_size=0.3, stratify=labels)

print("X_train,y_train:", X_train.shape, y_train.shape)
print("X_test,y_test:", X_test.shape, y_test.shape)