import pandas as pd  # 数据表处理
from pandas import DataFrame, Series
import numpy as np  # 数值运算，线性代数
import matplotlib.pyplot as plt
import time
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文

import warnings
warnings.filterwarnings("ignore")

# 用于记录本地时间
def get_local_time():
    return time.strftime("%m%d%H%M", time.localtime())

def plot(data, i, whis=0.5) :
    plt.subplot(2, 5, i)
    plt.boxplot(data, vert=False, patch_artist=True, widths=0.5, whis=whis,
                boxprops=dict(facecolor="green", color="red"),
                capprops=dict(color="blue"),
                whiskerprops=dict(color="teal"),
                flierprops=dict(markersize=3.0, color="black", markeredgecolor="black"),
                medianprops=dict(color="orange"),
                meanprops=dict(color="brown"))
    plt.title('手机上网'+title + str(i) + '分')

def minMax(data, whis=0.5):
    _, bp = pd.DataFrame.boxplot(data, whis=whis, return_type='both')

    # outliers = [flier.get_ydata() for flier in bp["fliers"]]  # 离群点的值
    # boxes = [box.get_ydata() for box in bp["boxes"]]  # 四分位点
    medians = [median.get_ydata() for median in bp["medians"]]  # 中位数
    whiskers = [whiskers.get_ydata() for whiskers in bp["whiskers"]]  # 四分位点和边界点

    mid = medians[0][0]
    left = whiskers[0][1]
    right = whiskers[1][1]
    box_left = whiskers[0][0]
    box_right = whiskers[1][0]

    return [mid, left, right, box_left, box_right]


# **********************************************//异常数据的查看
title = '网络覆盖与信号强度'
train_data_ = pd.read_excel('output/error/手机上网网络覆盖与信号强度.xlsx', index_col=0)
data = train_data_[[title, '特征加权和']]

data_1 = data.loc[data[title].apply(lambda a:1 == a)]
data_2 = data.loc[data[title].apply(lambda a:2 == a)]
data_3 = data.loc[data[title].apply(lambda a:3 == a)]
data_4 = data.loc[data[title].apply(lambda a:4 == a)]
data_5 = data.loc[data[title].apply(lambda a:5 == a)]
data_6 = data.loc[data[title].apply(lambda a:6 == a)]
data_7 = data.loc[data[title].apply(lambda a:7 == a)]
data_8 = data.loc[data[title].apply(lambda a:8 == a)]
data_9 = data.loc[data[title].apply(lambda a:9 == a)]
data_10 = data.loc[data[title].apply(lambda a:10 == a)]


plot(data_1['特征加权和'], 1)
plot(data_2['特征加权和'], 2)
plot(data_3['特征加权和'], 3)
plot(data_4['特征加权和'], 4)
plot(data_5['特征加权和'], 5)
plot(data_6['特征加权和'], 6)
plot(data_7['特征加权和'], 7)
plot(data_8['特征加权和'], 8)
plot(data_9['特征加权和'], 9)
plot(data_10['特征加权和'], 10)


# plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.8)
# plt.savefig('./output/离群值查看1.png', dpi=300)
plt.show()


# *************************************************************************************************