import pandas as pd  # 数据表处理
from pandas import DataFrame, Series
import numpy as np  # 数值运算，线性代数
import matplotlib.pyplot as plt  # 数据可视化绘图
import seaborn as sns  # 数据可视化绘图
plt.rcParams['figure.facecolor']=(1,1,1,1) # pycharm 绘图白底，看得清坐标
plt.rcParams['font.family'] = 'SimHei'

import time
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,OrdinalEncoder, MinMaxScaler, MaxAbsScaler  # 特征编码


train_data = pd.read_excel("dataset/附件1语音业务用户满意度数据.xlsx")
test_data = pd.read_excel("dataset/附件3语音业务用户满意度预测数据.xlsx")

import warnings
warnings.filterwarnings("ignore")


y_train = train_data['语音通话整体满意度']  # 标签数据

# 训练测试数据不统一，删除部分数据
x_train = train_data.drop(['网络覆盖与信号强度', '语音通话清晰度', '语音通话稳定性', '重定向次数',
                           '重定向驻留时长', '语音方式', '是否去过营业厅', 'ARPU（家庭宽带）', '是否实名登记用户', '当月欠费金额',
                           '前第3个月欠费金额', '终端品牌', '终端品牌类型', '用户描述', '用户描述.1'], axis=1)
x_test = test_data.drop(['是否不限量套餐到达用户', '性别', '终端品牌', '终端品牌类型', '用户描述', '用户描述.1'], axis=1)

x_train.insert(loc=19, column='是否投诉',value=0)
x_train['是否投诉'] = x_train['家宽投诉'] + x_train['资费投诉']
x_train = x_train.drop(['家宽投诉', '资费投诉'], axis=1)
x_train['是否投诉'] = x_train['是否投诉'].mask(x_train['是否投诉'] > 0, 1)


# 用于记录本地时间
def get_local_time():
    return time.strftime("%m%d%H%M", time.localtime())

# 用于数据预处理
def _encode(data):
    result = pd.DataFrame.copy(data, deep=True)

    result['是否关怀用户'] = result['是否关怀用户'].fillna(0)
    result = result.replace({
        '是否投诉': {'是': 1, '否': 0},
        '是否关怀用户': {'是': 1,'否': 0},
        '4\\5G用户': {'2G': 1, '4G': 2, '5G': 3},
        '是否4G网络客户（本地剔除物联网）': {'是': 1, '否': 0},
        '是否5G网络客户': {'是': 1, '否': 0},
        '客户星级标识': {'未评级': 1, '准星': 2, '一星': 3, '二星': 4, '三星': 5,
                   '白金卡': 6, '钻石卡': 7, '银卡': 8,'金卡': 9},

        '居民小区': {-1: 0},
        '办公室': {-1: 0, 2: 1},
        '高校': {-1: 0, 3: 1},
        '商业街': {-1: 0, 4: 1},
        '地铁': {-1: 0, 5: 1},
        '农村': {-1: 0, 6: 1},
        '高铁': {-1: 0, 7: 1},
        '其他，请注明': {-1: 0, 98: 1},

        '手机没有信号': {-1: 0},
        '有信号无法拨通': {-1: 0, 2: 1},
        '通话过程中突然中断': {-1: 0, 3: 1},
        '通话中有杂音、听不清、断断续续': {-1: 0, 4: 1},
        '串线': {-1: 0, 5: 1},
        '通话过程中一方听不见': {-1: 0, 6: 1},
        '其他，请注明.1': {-1: 0, 98: 1},

    })

    # 对两个连续值的特征进行无量纲化
    # for col in ['脱网次数', 'mos质差次数','未接通掉话次数','套外流量（MB）','套外流量费（元）','语音通话-时长（分钟）',
    #             '省际漫游-时长（分钟）','当月ARPU','当月MOU','前3月ARPU','前3月MOU','GPRS总流量（KB）','GPRS-国内漫游-流量（KB）']:
    #     # maxAbsEnc = MaxAbsScaler()    # 归一到[-1，1]
    #     minMaxEnc = MinMaxScaler()    # 归一到[0，1]
    #     result[col] = minMaxEnc.fit_transform(result[col].values.reshape(-1, 1))

    return result


# 对加载进来的数据集进行预处理
x_train_temp = _encode(x_train)
x_test_temp = _encode(x_test)

x_train_temp = x_train_temp.dropna()
x_test_temp = x_test_temp.dropna()

x_train_temp.to_excel('output/语音训练查看缺失集2.xlsx', index=False)
x_test_temp.to_excel('output/语音测试查看缺失集2.xlsx', index=False)




