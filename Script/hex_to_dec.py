import numpy as np
import pandas as pd

# def conv(string):
#     my_dict = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
#     li = []
#     line = string
#     for i in range(len(line)):
#         li.append(my_dict.get(line[i]) if line[i] in my_dict else int(line[i]))
#     return sum([li[i]*pow(16,len(li)-i-1) for i in range(len(li))])

dataset_file_name = "D:\Academic\FYP\Car-Hacking Dataset\\3.sample_0.05\gear_dataset.csv"
print("Loading raw data...")
raw = pd.read_csv(dataset_file_name, header=None, low_memory=None)

print(raw)
col = raw.shape[1]-1
row = raw.shape[0]-1
print(col)
print(row)
df=raw.copy()
for i in range(0, row+1):
    for j in range(0,9):
        df[j][i]=int(df[j][i],16)
    print(i)
print(df)
print("writing")

df.to_csv("D:\Academic\FYP\Car-Hacking Dataset\\4.05hex_to_dec\gear_dataset.csv", index=False, header=False)


