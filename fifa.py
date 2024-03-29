import pandas as pd
import numpy as np
import sys
import csv
import os

import matplotlib.ticker as ticker
from matplotlib import pyplot as plt

import matplotlib.dates as mdate
import fifa1

def graph2():
    data = pd.read_csv("a.csv")
    sum1 = data.shape
    print("数据量的大小为：")
    print(sum1)
    sum2 = data.duplicated().sum()
    # if (sum2 == 0):
    #     print("没有重复的数据，爬出的数据信息比较整洁，不需要删除重复值")
    # else:
    #     print("有重复数据需要处理")

    print(data.head())

    data["birth_year"] = data.birth.str.split(".").str[2]
    data["birth_month"] = data.birth.str.split(".").str[1]
    data["birth_day"] = data.birth.str.split(".").str[0]

    # print(data.head(10))
    # print(data.info())

    # 分隔事件后的数据转换为int类型
    data['birth_year'] = data.birth_year.astype('int')
    data['birth_month'] = data.birth_month.astype('int')
    data['birth_day'] = data.birth_day.astype('int')
    # 再次检查数据类型
    print(data.info())
    # 将数据通过出生年份进行排序，整理数据，可以在网页里做出选出年龄最大等的效果
    data = data.sort_values(by=['birth_year', 'birth_month', 'birth_day'])
    #
    print(data.head(10))

    # 重置索引值
    data = data.reset_index(drop=True)

    print(data.head(10))

    print(data.columns)
    data2 = data
    del data2['card']
    del data2['ovr']
    del data2['pac']
    del data2['pas']
    del data2['sho']
    del data2['dri']
    del data2['defend']
    del data2['phy']

    print(data2.duplicated().sum())
    data2.drop_duplicates(inplace=True)
    data2 = data2.reset_index(drop=True)
    print(data2.head(10))

    count_year = data.groupby('birth_year').count()['name'].reset_index(drop=True)
    print(count_year)
    print(data.columns)
    data2.to_csv('data2.csv')

    filename = 'data2.csv'
    with open(filename) as f:
        # 创建阅读器，调用csv.reader()将前面存储的文件对象作为实参传给他
        reader = csv.reader(f)
        # 调用next()一次，将文件的第一行存储在header_now中
        header_now = next(reader)

        year = []
        for row in reader:
            year.append(row[6])

        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        seven = 0
        eight = 0
        nine = 0
        for a in year:
            i = int(a)
            if 1920 < i <= 1930:
                one += 1
            elif 1930 < i <= 1940:
                two += 1
            elif 1940 < i <= 1950:
                three += 1
            elif 1950 < i <= 1960:
                four += 1
            elif 1960 < i <= 1970:
                five += 1
            elif 1970 < i <= 1980:
                six += 1
            elif 1980 < i <= 1990:
                seven += 1
            elif 1990 < i <= 2000:
                eight += 1
            elif 2000 < i <= 2010:
                nine += 1
        print(one, two, three, four, five, six, seven, eight, nine)

        # 年龄分布图
        plt.rcParams['font.sans-serif'] = ['SimHei']
        labels = ['1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s']
        values = [one, two, three, four, five, six, seven, eight, nine]
        colors = ['orange', 'pink', 'b', 'g', 'red', 'blue', 'yellow', 'green', 'pink']
        plt.title("球员年龄分布饼状图", fontsize=16, pad=15)
        plt.tick_params(axis='both', which='major', labelsize=26)
        plt.pie(values, labels=labels, colors=colors, pctdistance=0.6, startangle=180,
                autopct='%0.2f%%')
        # plt.(values, labels=labels, colors=colors, pctdistance=0.6,startangle=180,
        #         autopct='%0.2f%%')
        # 将横、纵坐标轴标准化处理,保证饼图是一个正圆,否则为椭圆
        plt.axis('equal')
        plt.gca().spines['right'].set_color('none')
        plt.gca().spines['top'].set_color('none')
        plt.gca().spines['left'].set_color('none')
        plt.gca().spines['bottom'].set_color('none')
        plt.savefig('pics/1.png')

        fig, axes = plt.subplots()
        axes.plot(labels, values, c='red')
        axes.set_title("年龄分布图", fontproperties="SimHei", fontsize=24)
        axes.set_xlabel('年龄', fontproperties="SimHei", fontsize=16)
        fig.autofmt_xdate()
        axes.set_ylabel("计数", fontproperties="SimHei", fontsize=16)
        axes.tick_params(axis='both', which='major', labelsize=16)
        plt.savefig('pics/2.png')
    return
