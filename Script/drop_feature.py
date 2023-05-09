import pandas as pd

df = pd.read_csv("D:\Academic\FYP\Car-Hacking Dataset\\1.label_transform\RPM_dataset.csv", names=[0,1,2,3,4,5,6,7,8,9,10,11])
print(df.shape)

df = df.iloc[: , 1:]
print(df.shape)
dropList = df[df[2] != 8].index.tolist()
df = df.drop(dropList)
df = df.drop(2, axis=1)
print(df.shape)
print(df.head())
df.to_csv("D:\Academic\FYP\Car-Hacking Dataset\\2.drop_feature\RPM_dataset.csv", index=False, header=False)