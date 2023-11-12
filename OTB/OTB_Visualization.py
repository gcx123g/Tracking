"""
绘制OTB数据集的的可视化结果，提供OTB数据集位置、跟踪器结果位置、可视化图保存位置。
"""
import cv2
import os

image_path = 'E:/data/OTB/'
result_path = 'D:/OTBresults/'

items = os.listdir(image_path)
scenes = []
scenes_result = []
for item in items:
    if os.path.isdir(image_path + '/' + item):
        scenes.append(item + '/img/')
        scenes_result.append('/' + item)
    else:
        print(item)
scenes_result[scenes_result.index('/Human4')] = '/Human4-2'
scenes_result[scenes_result.index('/Jogging')] = '/Jogging-1'
scenes_result[scenes_result.index('/Skating2')] = '/Skating2-1'

trackers = ['Ground-Truth', 'PrDimp', 'DiMP', 'TransT', 'Ours1', 'KeepTrack']

for name_idx in range(len(scenes)):
    print(scenes[name_idx])
    image_list = os.listdir(image_path + scenes[name_idx])
    color = [(0, 255, 0), (28, 28, 28), (218, 112, 214), (255, 0, 0), (0, 0, 255), (250, 240, 230)]  # 绿 黑 粉 蓝 红 灰色

    for i in range(len(image_list)):
        try:
            image = cv2.imread(image_path + scenes[name_idx] + image_list[i])
            color_idx = 0
            for tracker in trackers:  # 打开每一个track的结果
                with open(result_path + tracker + scenes_result[name_idx] + '.txt', 'r') as file:
                    lines = file.readlines()
                ground_truth = lines[i].rstrip('\n').split(',')
                ground_value = [int(float(item)) for item in ground_truth]
                x, y, width, height = ground_value
                cv2.rectangle(image, (x, y), (x + width, y + height), color[color_idx], 2)
                cv2.putText(image, "#" + str(i), (10, 50), cv2.FONT_ITALIC, 1.5, (130, 220, 238), 3)
                color_idx += 1

            # cv2.imshow('Image', image)
            # cv2.waitKey(0)  # 等待用户按下任意键
            # cv2.destroyAllWindows()  # 关闭显示窗口
            # print('D:/OTBresults/compare_results'+scenes_result[name_idx]+'/'+str(i)+'.jpg')

            if not os.path.exists('D:/OTBresults/compare_results' + scenes_result[name_idx]):
                os.makedirs('D:/OTBresults/compare_results' + scenes_result[name_idx])
            cv2.imwrite('D:/OTBresults/compare_results' + scenes_result[name_idx] + '/' + str(i) + '.jpg', image)

        except:
            print(i)
            continue
