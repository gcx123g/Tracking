import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = 'SimHei'


def read_column(path_1):
    with open(path_1, 'r') as file:
        lines = file.readlines()
    data_list = []
    for line in lines:
        # 提取目标数据
        start_index = line.index(']') + 2
        end_index = len(line) - 1
        data = line[start_index:end_index]
        data_list.append(data)
    return data_list


def read_data(path, file_lis, column, index):
    data = []
    for i in range(len(file_lis)):  # 打开index文件
        with open(path + file_lis[i], 'r') as file:
            lines = file.readlines()
        max_min = []
        for line in lines:
            value1 = float(line[1: 6])
            max_min.append(value1)
        max_min.sort()
        print(format(max_min[0]*100, '.1f'))
        index[i] = index[i] + '\n' + '['+str(format(max_min[0]*100, '.1f')+', '+format(max_min[-1]*100, '.1f'))+']'

        data_value = []
        for j in range(len(column)):
            value = 0.
            for line in lines:
                start_index = line.index(']') + 2
                end_index = len(line) - 1
                name = line[start_index:end_index]
                if name == column[j]:
                    value = float(line[1:6])
            data_value.append(value)
        data.append(data_value)
    return data, index
    # return list(np.transpose(np.array(data)))


path = 'D:/eval/result/'
file_list = os.listdir(path)
index = [filename[:-4] for filename in file_list if filename.endswith('.txt')]

columns = read_column(path + file_list[0])
data, idx = read_data(path, file_list, columns, index)

dataset = pd.DataFrame(data=data,
                       index=idx,
                       columns=columns)

radar_labels = dataset.index

nAttr = len(index)
data = dataset.values*100  # 数据值
data_labels = dataset.columns
# 设置角度
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))

# 设置画布
fig = plt.figure(facecolor="white", figsize=(10, 6))
ax = plt.subplot(111, polar=True)

# 绘图
ax.plot(angles, data[:, 0], '^-', color='yellow', markersize=7,
        linewidth=1.5, alpha=0.8)
ax.plot(angles, data[:, 1], 'h-', color='red', markersize=9,
        linewidth=1.5, alpha=0.8)
ax.plot(angles, data[:, 2], 'v-', color='pink', markersize=7,
        linewidth=1.5, alpha=0.8)
ax.plot(angles, data[:, 3], 'o-',
        linewidth=1.5, alpha=0.8, color='lime', markersize=8)
ax.plot(angles, data[:, 4], 'x-', markersize=5,
        linewidth=1.5, alpha=0.8)
ax.plot(angles, data[:, 5], 'D-', color='aquamarine',
        linewidth=1.5, alpha=0.8)
ax.plot(angles, data[:, 6], 'P-', color='blue',
        linewidth=1.5, alpha=0.8)


# 填充颜色
plt.fill(angles, data, alpha=0)
plt.thetagrids(angles[:-1] * 180 / np.pi, radar_labels)


# 设置指标标签
ax.set_xticklabels(radar_labels)
print(radar_labels)
ax.set_xticklabels(radar_labels, rotation=0, ha='right')
for i, label in enumerate(ax.get_xticklabels()):
    if i < 4:
        label.set_ha('left')
    if i == 4:
        label.set_ha('center')
    if 4 < i < 7:
        label.set_ha('right')
    if 6 < i < 10:
        label.set_ha('right')
    if i == 11 or i == 10:
        label.set_ha('center')
    if 11 < i < 15:
        label.set_ha('left')
    if  i == 10:
        label.set_ha('right')

# 设置图例
legend = plt.legend(data_labels, loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=len(columns))
plt.setp(legend.get_texts(), fontsize='large')
plt.grid(True, color='lightgray')
ax.spines['polar'].set_color('lightgray')
plt.savefig('tongshi.svg', format='svg')
plt.show()
