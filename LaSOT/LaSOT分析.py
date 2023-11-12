import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

trackers = ['aiatrack', 'mixformer', 'ours']
path = 'E:/LaSOT分析/'
success = {}

for tracker in trackers:
    success_value = pd.read_csv(path + tracker + '/success.txt', header=None).values
    success[tracker] = list(success_value)

    plt.subplot(221)
    plt.xlabel("序列", fontproperties="SimSun")
    plt.ylabel("Success")
    plt.plot(range(0, 280), success[tracker], label=tracker)
    plt.legend()

path = 'E:/data/LaSOT/test'
lasot_list = os.listdir(path)
for i in range( 280):
    print(lasot_list[i])
lasot_list.remove('LaSOT.json')
aia_ours_idx = [i for i in range(280) if (success['aiatrack'][i] - success['ours'][i]) > 0.2]
_aia_ours_idx = [i for i in range(280) if (success['ours'][i] - success['aiatrack'][i]) > 0.2]

mix_ours_idx = [i for i in range(280) if (success['mixformer'][i] - success['ours'][i]) > 0.2]
_mix_ours_idx = [i for i in range(280) if (success['ours'][i] - success['mixformer'][i]) > 0.2]

colors=[]
for i in range(280):
    if (success['aiatrack'][i] - success['ours'][i]) > 0.2 and (success['mixformer'][i] - success['ours'][i]) > 0.2:
        colors.append('r')
    elif (success['ours'][i] - success['aiatrack'][i]) > 0.2 or (success['ours'][i] - success['mixformer'][i]) >0.2:
        colors.append('green')
    else:
        colors.append('b')


plt.subplot(222)
plt.xlabel("序列", fontproperties="SimSun")
plt.ylabel("Success")
plt.title('aiatrack-ours')
plt.scatter(range(0, 280), [success['aiatrack'][i] - success['ours'][i] for i in range(280)], c=colors)
for idx in aia_ours_idx:
    plt.annotate(lasot_list[idx], xy=(idx, success['aiatrack'][idx] - success['ours'][idx]),
                 xytext=(idx + 0.01, success['aiatrack'][idx] - success['ours'][idx] + 0.01))
for idx in _aia_ours_idx:
    plt.annotate(lasot_list[idx], xy=(idx, success['aiatrack'][idx] - success['ours'][idx]),
                 xytext=(idx + 0.05, success['aiatrack'][idx] - success['ours'][idx] + 0.05))

plt.subplot(212)
plt.xlabel("序列", fontproperties="SimSun")
plt.ylabel("Success")
plt.title('mixformer-ours')
plt.scatter(range(0, 280), [success['mixformer'][i] - success['ours'][i] for i in range(280)], c=colors)
for idx in mix_ours_idx:
    plt.annotate(lasot_list[idx], xy=(idx, success['mixformer'][idx] - success['ours'][idx]),
                 xytext=(idx + 0.01, success['mixformer'][idx] - success['ours'][idx] + 0.01))
for idx in _mix_ours_idx:
    plt.annotate(lasot_list[idx], xy=(idx, success['mixformer'][idx] - success['ours'][idx]),
                 xytext=(idx + 0.05, success['mixformer'][idx] - success['ours'][idx] + 0.05))
plt.show()
