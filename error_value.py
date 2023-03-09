import pandas as pd  # 数据表处理
from pandas import DataFrame, Series
import numpy as np  # 数值运算，线性代数
import matplotlib.pyplot as plt
import time
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文
train_data = pd.read_excel("./data2/手机上网稳定性.xls")

import warnings
warnings.filterwarnings("ignore")

# 用于记录本地时间
def get_local_time():
    return time.strftime("%m%d%H%M", time.localtime())


# **********************************************//异常数据的查看
train_data_ = pd.read_excel("F:\mathorcup-project\复赛\weight_values.xls")
x1=train_data_['更新权重']
# plt.subplot(1,1,1)
plt.boxplot(x1, vert=False, patch_artist=True, widths=5, whis=0.5,
            boxprops=dict(facecolor="green", color="red"),
            capprops=dict(color="blue"),
            whiskerprops=dict(color="teal"),
            flierprops=dict(markersize=3.0, color="black", markeredgecolor="black"),
            medianprops=dict(color="orange"),
            meanprops=dict(color="brown"))
plt.title("语音通话整体满意度")


# x2=train_data_['mos质差次数']
# plt.subplot(7,2,2)
# plt.boxplot(x2,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("mos质差次数")
#
# x3=train_data_['未接通掉话次数']
# plt.subplot(7,2,3)
# plt.boxplot(x3,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("未接通掉话次数")
#
# x4=train_data_['套外流量（MB）']
# plt.subplot(7,2,4)
# plt.boxplot(x4,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("套外流量（MB）")
#
# x5=train_data_['套外流量费（元）']
# plt.subplot(7,2,5)
# plt.boxplot(x5,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("套外流量费（元）")
#
# x6=train_data_['语音通话-时长（分钟）']
# plt.subplot(7,2,6)
# plt.boxplot(x6,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("语音通话-时长（分钟）")
#
# x7=train_data_['当月ARPU']
# plt.subplot(7,2,7)
# plt.boxplot(x7,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("当月ARPU")
#
# x8=train_data_['当月MOU']
# plt.subplot(7,2,8)
# plt.boxplot(x8,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("当月MOU")
#
# x9=train_data_['前3月ARPU']
# plt.subplot(7,2,9)
# plt.boxplot(x9,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("前3月ARPU")
#
# x10=train_data_['前3月MOU']
# plt.subplot(7,2,10)
# plt.boxplot(x10,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("前3月MOU")
#
# x11=train_data_['GPRS总流量（KB）']
# plt.subplot(7,2,11)
# plt.boxplot(x11,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("GPRS总流量（KB）")
#
# x12=train_data_['GPRS-国内漫游-流量（KB）']
# plt.subplot(7,2,12)
# plt.boxplot(x12,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("GPRS-国内漫游-流量（KB）")
#
# x13=train_data_['外省语音占比']
# plt.subplot(7,2,13)
# plt.boxplot(x13,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("外省语音占比")
#
# x14=train_data_['外省流量占比']
# plt.subplot(7,2,14)
# plt.boxplot(x14,vert=False,patch_artist=True,widths=0.5,
#             boxprops=dict(facecolor="green", color="red"),
#             capprops=dict(color="blue"),
#             whiskerprops=dict(color="teal"),
#             flierprops=dict(markersize=3.0,color="black", markeredgecolor="black"),
#             medianprops=dict(color="orange"),
#             meanprops=dict(color="brown"))
# plt.title("外省流量占比")

# plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.8)
plt.savefig('./output/离群值查看1.png', dpi=300)
#
# *************************************************************************************************