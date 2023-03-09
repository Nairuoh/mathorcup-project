import pandas as pd  # 数据表处理
from pandas import DataFrame, Series
import numpy as np  # 数值运算，线性代数
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
import time
import warnings
warnings.filterwarnings("ignore")


# 用于记录本地时间
def get_local_time():
    return time.strftime("%m%d%H%M", time.localtime())

##############
def plot(data, i):
    plt.subplot(2, 5, i)
    plt.boxplot(data, vert=False, patch_artist=True, widths=0.5, whis=1,
                boxprops=dict(facecolor="green", color="red"),
                capprops=dict(color="blue"),
                whiskerprops=dict(color="teal"),
                flierprops=dict(markersize=3.0, color="black", markeredgecolor="black"),
                medianprops=dict(color="orange"),
                meanprops=dict(color="brown"))
    plt.title(title + str(i) + '分')


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


def check(data):
    _, left, right, _, _ = minMax(data['特征加权和'])
    data_check = data.loc[data['特征加权和'].apply(lambda a: left <= a <= right)]
    return data_check

# **********************************************//异常数据的查看
title = '手机上网速度'
train_data_ = pd.read_excel('output/error/手机上网速度.xlsx', index_col=0)
# data = train_data_[[title, '特征加权和']]
data = pd.DataFrame.copy(train_data_, deep=True)

# 按打分分类
data_1 = data.loc[data[title].apply(lambda a: 1 == a)]
data_2 = data.loc[data[title].apply(lambda a: 2 == a)]
data_3 = data.loc[data[title].apply(lambda a: 3 == a)]
data_4 = data.loc[data[title].apply(lambda a: 4 == a)]
data_5 = data.loc[data[title].apply(lambda a: 5 == a)]
data_6 = data.loc[data[title].apply(lambda a: 6 == a)]
data_7 = data.loc[data[title].apply(lambda a: 7 == a)]
data_8 = data.loc[data[title].apply(lambda a: 8 == a)]
data_9 = data.loc[data[title].apply(lambda a: 9 == a)]
data_10 = data.loc[data[title].apply(lambda a: 10 == a)]

# 去除异常值
data_1_check = check(data_1)
data_2_check = check(data_2)
data_3_check = check(data_3)
data_4_check = check(data_4)
data_5_check = check(data_5)
data_6_check = check(data_6)
data_7_check = check(data_7)
data_8_check = check(data_8)
data_9_check = check(data_9)
data_10_check = check(data_10)


data_check =  pd.concat([data_1_check, data_2_check, data_3_check, data_4_check, data_5_check,
                         data_6_check, data_7_check, data_8_check, data_9_check, data_10_check])

data_check = data_check.drop(['特征加权和'], axis=1)


features = data_check.columns.values[1:]
# features = ['是否遇到过网络问题', '居民小区', '办公室', '商业街', '地铁', '手机没有信号', '有信号无法拨通',
#             '通话过程中突然中断', '通话中有杂音、听不清、断断续续', '通话过程中一方听不见']
for feature in features:
    data_check[feature].where(data_check[feature] == 0, 1, inplace=True)


data_check.to_excel('output/check/0.5/' + title + '.xlsx')