import argparse
import os
from plyfile import PlyData, PlyElement
import numpy as np
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
g_classes = [x.rstrip() for x in open(os.path.join(BASE_DIR, 'meta/class_duiying.txt'))]
g_class2label = {str(float(cls.split('\t')[0])): float(cls.split('\t')[1]) for i, cls in enumerate(g_classes)}

g_classes_cn = [x.rstrip() for x in open(os.path.join(BASE_DIR, 'meta/class_duiying_CN.txt'))]
g_class2label_cn = {float(cls.split('\t')[0]): cls.split('\t')[1] for i, cls in enumerate(g_classes_cn)}


if __name__ == '__main__':
    #input path
    input_folder = ''
    datanames = os.listdir(input_folder)
    list = []
    for i in datanames:
        list.append(i)
    #output path
    output_folder = ''
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    #output graph and data
    for file_name in list:
        #print(file_name)
        elements = file_name.split('.')
        in_path = os.path.join(input_folder, file_name)
        output_name = elements[0]
        output_path = os.path.join(output_folder, output_name)
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        data = np.load(in_path)
        object_total = np.unique(data[:,-2])
        print(file_name+':'+str(np.shape(object_total)[0]))
        g_objectlabel = {cls.split('\t')[1]: 0 for i, cls in enumerate(g_classes_cn)} #用于计object的数目
        for i in range(np.shape(object_total)[0]):
            object_num = object_total[i]
            index = (data[:,-2] == object_num)
            ori_class = str(Counter(data[index][:, -1]).most_common()[0][0])
            new_class = g_class2label [ori_class]
            new_class_CN = g_class2label_cn[new_class]
            new_data = data[index]
            g_objectlabel[new_class_CN] = g_objectlabel[new_class_CN] + 1
            #if new_class_CN != 'unclassified':
            np.save(os.path.join(output_path, new_class_CN+ "_" + str(g_objectlabel[new_class_CN])), new_data)