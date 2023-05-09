import os
import numpy as np
import math
#.txt文件的路径
path = "D:\Academic\FYP\Car-Hacking Dataset\\normal_run_data.txt"

#open(path)打开.txt文件
with open(path) as f1:
    cNames = f1.readlines()  #.readlines()读取.txt文件的每行
    for i in range(0,len(cNames)):
        cNames[i] = cNames[i].strip()+',0\n'  #.strip()用于移除字符串头尾指定的字符(默认为空格或换行符）

#open(path,'w')以可写方式打开.txt文件，将处理过的cNames写入新的文件中
with open(path,'w') as f2:
    f2.writelines(cNames)
