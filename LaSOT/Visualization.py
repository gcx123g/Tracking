import cv2
import os
import matplotlib.pyplot as plt
import numpy as np


def success_overlap(gt_bb, result_bb, n_frame):
    thresholds_overlap = np.arange(0, 1.05, 0.05)
    success = np.zeros(len(thresholds_overlap))
    iou = np.ones(len(gt_bb)) * (-1)
    mask = np.sum(gt_bb[:, 2:] > 0, axis=1) == 2
    # print(len(gt_bb))
    # print(len(result_bb))
    iou[mask] = overlap_ratio(gt_bb[mask], result_bb[mask])
    suc = 0
    for i in range(len(thresholds_overlap)):
        success[i] = np.sum(iou > thresholds_overlap[i]) / float(n_frame)
        if thresholds_overlap[i] == 0.5:
            suc = success[i]
    return success, suc


def overlap_ratio(rect1, rect2):
    """Compute overlap ratio between two rects
    Args
        rect:2d array of N x [x,y,w,h]
    Return:
        iou
    """

    left = np.maximum(rect1[:, 0], rect2[:, 0])
    right = np.minimum(rect1[:, 0] + rect1[:, 2], rect2[:, 0] + rect2[:, 2])
    top = np.maximum(rect1[:, 1], rect2[:, 1])
    bottom = np.minimum(rect1[:, 1] + rect1[:, 3], rect2[:, 1] + rect2[:, 3])

    intersect = np.maximum(0, right - left) * np.maximum(0, bottom - top)
    union = rect1[:, 2] * rect1[:, 3] + rect2[:, 2] * rect2[:, 3] - intersect
    iou = intersect / union
    iou = np.maximum(np.minimum(1, iou), 0)
    return iou


data_root = 'E:/data/LaSOT/test'  # LaSOT测试数据集路径
vis = False
frames = os.listdir(data_root)
frames = [frame for frame in frames if os.path.isdir(data_root + '/' + frame)]

for frame in frames:

    # 读取图片
    path = data_root + '/' + frame + '/img/'
    images_list = os.listdir(path)
    images_path = [path + image for image in images_list]

    # 读取真实值
    with open(data_root + '/' + frame + '/groundtruth.txt', 'r') as file:
        lines = file.readlines()
    ground_truth = [[int(float(line.rstrip('\n').split(',')[i])) for i in range(4)] for line in lines]

    # 读取tracker_result
    trackers_truth = []
    trackers = os.listdir('./tracker_results')
    for tracker in trackers:
        with open('./tracker_results/' + tracker + '/' + frame + '.txt', 'r') as file:
            lines = file.readlines()
        truth = [[int(float(line.rstrip('\n').split(',')[i])) for i in range(4)] for line in lines]
        trackers_truth.append(truth)
        _, success = success_overlap(np.array(ground_truth), np.array(truth), len(images_path))
        print(tracker, success)
        if success < 0.3:
            vis = True

    # 可视化展示
    if vis:
        for image_idx in range(len(images_path)):
            # 读取图像
            image = cv2.imread(images_path[image_idx])

            # 绘制真值框
            x, y, width, height = ground_truth[image_idx]
            cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
            # 绘制tracker框
            for tracker_truth in trackers_truth:
                x, y, width, height = tracker_truth[image_idx]
                cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 255), 2)

            cv2.putText(image, "#" + str(image_idx+1), (10, 50), cv2.FONT_ITALIC, 1.5, (130, 220, 238), 3)

            if not os.path.exists('./vis_results/'+frame+'(%.3f)' % success):
                os.makedirs('./vis_results/'+frame+'(%.3f)' % success)

            cv2.imwrite('./vis_results/' + frame + ('(%.3f)' % success) + '/' + str(image_idx+1) + '.jpg', image)
            vis = False
    print(frame)


