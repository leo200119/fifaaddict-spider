import pandas as pd
import numpy as np
import sys
import csv
import os
import matplotlib.pyplot as plt
import matplotlib

def radarpic(index):
    matplotlib.rcParams['font.family'] = 'SimHei'  # 将字体设置为黑体'SimHei'
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    labels = np.array(['PAC速度','SHO射门','PAS传球','DRI盘带','DEF防守','PHY体格'])
    dataLenth = 6  # 数据长度
    data = pd.read_csv("b.csv")
    angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)  # 根据数据长度平均分割圆周长

    # data0=data.iloc[:,4:10]
    # print(data0.apply(np.mean))
    # 闭合
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))  # 对labels进行封闭

    # data1=data.iloc[index,4:10]
    # name1=data.iloc[index,0:3]
    # s1=name1[0]+' '+name1[1]+' 总评:'+str(name1[2])
    # s2=' PAC速度'+str(data1[0])+' SHO射门'+str(data1[1])+' PAS传球'+str(data1[2])+' DRI盘带'+str(data1[3])+' DEF防守'+str(data1[4])+' PHY体格'+str(data1[5])
    print(data1)
    # 闭合
    data1 = np.concatenate((data1, [data1[0]]))

    fig = plt.figure(facecolor="white")  # facecolor 设置框体的颜色
    subplt=plt.subplot(111, polar=True)  # 将图分成1行1列，画出位置1的图；设置图形为极坐标图
    plt.plot(angles, data1,  color='g', linewidth=2)
    plt.fill(angles, data1, facecolor='g', alpha=0.25)  # 填充两条线之间的色彩，alpha为透明度
    plt.thetagrids(angles * 180 / np.pi, labels)  # 做标签
    subplt.set_ylim(40,120) # 设置范围

    plt.figtext(0.52,0.95,'球员能力雷达图',ha='center')   #添加雷达图标题
    plt.grid(True)
    plt.show()
    return