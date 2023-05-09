import pandas as pd

df = pd.read_csv("D:\Academic\FYP\Car-Hacking Dataset\\2.drop_feature\gear_dataset.csv", header=None)
df = df.sample(frac=0.05)
print(df.shape)
df.to_csv("D:\Academic\FYP\Car-Hacking Dataset\\3.sample_0.05\gear_dataset.csv", index=False, header=False)