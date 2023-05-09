import pandas as pd

dataset_file_name = "D:\Academic\FYP\\NSL_KDD\KDDTest.csv"
raw_data = pd.read_csv(dataset_file_name, header=None, low_memory=False)
print(raw_data.shape)
raw_data = raw_data.iloc[:, 4:raw_data.shape[1]-1]
print(raw_data.shape)

last_row_index = raw_data.shape[0]
print(last_row_index)
raw_data=raw_data.copy()
for i in range(0, last_row_index):
    if raw_data[41][i]=="normal": raw_data[41][i]=0
    else: raw_data[41][i]=1
    print(i)
print(raw_data[41])

file_name = "D:\Academic\FYP\\NSL_KDD\KDDTest+.csv"
raw_data.to_csv(file_name, index=False, header=False)
