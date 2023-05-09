import matplotlib.pyplot as plt

data = {'DT': 15, 'KNN': 96, 'SVM': 13, 'RF': 14,
        'MLP': 73}

# 获取x y轴数据
x_data = list(data.keys())
y_data = list(data.values())

# 设置图形大小
plt.figure(figsize=(6, 4))

# 绘制柱状图
plt.bar(x_data, y_data, color='green')

# 在柱子上添加数值标签
for x, y in zip(x_data, y_data):
    plt.text(x, y, '%d' % y, ha='center', va='bottom')

# 设置 x y 轴标签
plt.xlabel('Models')
plt.ylabel('CPU Usage(%)')

# 显示网格线
plt.grid(True, axis='y', linestyle='--', color='gray', alpha=0.5)

# 显示图形
plt.show()
