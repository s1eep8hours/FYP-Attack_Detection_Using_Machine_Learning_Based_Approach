import pandas as pd

# 加载数据
trainset_file_name = ".\Dataset\KDDTrain.csv"
testset_file_name= ".\Dataset\KDDTest.csv"
print("Loading raw data...")
train_data = pd.read_csv(trainset_file_name, header=None, low_memory=False)
test_data = pd.read_csv(testset_file_name, header=None, low_memory=False)


# 查看标签数据情况
last_column_index = train_data.shape[1] - 1
print("print data labels:")
print(test_data[last_column_index].value_counts())


# 对原始数据进行切片，分离出特征和标签
X_train = train_data.iloc[:, :train_data.shape[1] - 1]
y_train = train_data.iloc[:, train_data.shape[1] - 1:]
X_test = test_data.iloc[:, :test_data.shape[1] - 1]
y_test = test_data.iloc[:, test_data.shape[1] - 1:]

#将标签降维
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

print("X_train,y_train:", X_train.shape, y_train.shape)
print("X_test,y_test:", X_test.shape, y_test.shape)