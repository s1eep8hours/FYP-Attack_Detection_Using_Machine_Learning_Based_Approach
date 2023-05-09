import pandas as pd

# def clearDirtyData(df):
#     dropList = df[(df[14]=="NaN")|(df[14]=="Infinity")|(df[15]=="NaN")|(df[15]=="Infinity")].index.tolist()
#     return dropList

# 按行合并多个Dataframe数据
def mergeData():
    Dos = pd.read_csv("D:\Academic\FYP\Car-Hacking Dataset\\4.05hex_to_dec\DoS_dataset.csv")
    Fuzzy = pd.read_csv("D:\Academic\FYP\Car-Hacking Dataset\\4.05hex_to_dec\Fuzzy_dataset.csv")
    gear = pd.read_csv("D:\Academic\FYP\Car-Hacking Dataset\\4.05hex_to_dec\gear_dataset.csv")
    RPM = pd.read_csv("D:\Academic\FYP\Car-Hacking Dataset\\4.05hex_to_dec\RPM_dataset.csv")

    frame = [Dos, Fuzzy, gear, RPM]

    print("Start merging")
    # # # 合并数据
    result = pd.concat(frame)

    return result


raw_data = mergeData()
file = 'D:\Academic\FYP\Car-Hacking Dataset\\total_0.05.csv'
raw_data.to_csv(file, index=False, header=False)
print("over")