import pandas as pd  # 数据表处理
from pandas import DataFrame, Series
import numpy as np  # 数值运算，线性代数
import matplotlib.pyplot as plt  # 数据可视化绘图
import seaborn as sns  # 数据可视化绘图
plt.rcParams['figure.facecolor']=(1,1,1,1) # pycharm 绘图白底，看得清坐标
plt.rcParams['font.family'] = 'SimHei'

import time
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,OrdinalEncoder, MinMaxScaler, MaxAbsScaler  # 特征编码


train_data = pd.read_excel("dataset/附件2上网业务用户满意度数据.xlsx")
test_data = pd.read_excel("dataset/附件4上网业务用户满意度预测数据.xlsx")
# print(test_data.columns)

import warnings
warnings.filterwarnings("ignore")


y_train = train_data['手机上网整体满意度']  # 标签数据
x_train = train_data.drop(['网络覆盖与信号强度','手机上网速度','手机上网稳定性','重定向次数','2G驻留时长','王者荣耀质差次数',
                           '高单价超套客户（集团）','高频高额超套客户（集团）','是否全月漫游用户','年龄','王者荣耀使用次数',
                           '游戏类APP使用天数','游戏类APP使用次数','王者荣耀使用天数','游戏类APP使用流量','抖音使用流量（MB）',
                           '今日头条使用流量','快手使用流量','优酷视频使用流量','腾讯视频使用流量','小视频系APP流量','阿里系APP流量',
                           '网易系APP流量','腾讯系APP流量','王者荣耀APP使用流量','蜻蜓FMAPP使用流量','饿了么使用流量','美团外卖使用流量',
                           '天猫使用流量','大众点评使用流量','滴滴出行使用流量','通信类应用流量','游戏类应用流量','网页类应用流量',
                           '音乐类应用流量','视频类应用流量','邮箱类应用流量','终端类型','操作系统','终端制式','是否校园套餐用户',
                           '校园卡无校园合约用户','校园卡校园合约捆绑用户','当月高频通信分公司','畅享套餐档位','畅享套餐名称',
                           '主套餐档位','近3个月平均消费（剔除通信账户支付）','近3个月平均消费（元）','本年累计消费（元）',
                           '码号资源-激活时间','码号资源-发卡时间','场景备注数据','现象备注数据','APP大类备注','APP小类视频备注',
                           'APP小类游戏备注','APP小类上网备注','终端品牌类型'], axis=1)  # 训练集数据去掉这几列

x_test = test_data.drop(['是否遇到网络问题','学习强国','学习强国.1','是否投诉','4\\5G用户','是否关怀用户',
                         '是否4G网络客户（本地剔除物联网）','外省语音占比','语音通话-时长（分钟）','省际漫游-时长（分钟）',
                         '当月ARPU','前3月ARPU','前3月MOU','外省流量占比','GPRS-国内漫游-流量（KB）','注明内容','注明内容.1',
                         '注明内容.2','注明内容.3','注明内容.4', np.nan,'终端品牌类型'], axis=1)


# 用于记录本地时间
def get_local_time():
    return time.strftime("%m%d%H%M", time.localtime())

# 用于数据预处理
def train_encode(data):
    result = pd.DataFrame.copy(data, deep=True)

    result['终端品牌'] = result['终端品牌'].fillna(0)
    result = result.replace({
        '是否不限量套餐到达用户': {'是': 1, '否': 0},
        '性别': {'性别不详': 0, '女': 1, '男': 2},
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

        '网络信号差/没有信号': {-1: 0},
        '显示有信号上不了网': {-1: 0, 2: 1},
        '上网过程中网络时断时续或时快时慢': {-1: 0, 3: 1},
        '手机上网速度慢': {-1: 0, 4: 1},
        '其他，请注明.1': {-1: 0, 98: 1},

        '看视频卡顿': {-1: 0},
        '打游戏延时大': {-1: 0, 2: 1},
        '打开网页或APP图片慢': {-1: 0, 3: 1},
        '下载速度慢': {-1: 0, 4: 1},
        '手机支付较慢': {-1: 0, 5: 1},
        '其他，请注明.2': {-1: 0, 98: 1},

        '爱奇艺': {-1: 0},
        '优酷': {-1: 0, 2: 1},
        '腾讯视频': {-1: 0, 3: 1},
        '芒果TV': {-1: 0, 4: 1},
        '搜狐视频': {-1: 0, 5: 1},
        '抖音': {-1: 0, 6: 1},
        '快手': {-1: 0, 7: 1},
        '火山': {-1: 0, 8: 1},
        '咪咕视频': {-1: 0, 9: 1},
        '其他，请注明.3': {-1: 0, 98: 1},

        '全部都卡顿': {-1: 0, 99: 1},
        '和平精英': {-1: 0},
        '王者荣耀': {-1: 0, 2: 1},
        '穿越火线': {-1: 0, 3: 1},
        '梦幻西游': {-1: 0, 4: 1},
        '龙之谷': {-1: 0, 5: 1},
        '梦幻诛仙': {-1: 0, 6: 1},
        '欢乐斗地主': {-1: 0, 7: 1},
        '部落冲突': {-1: 0, 8: 1},
        '炉石传说': {-1: 0, 9: 1},
        '阴阳师': {-1: 0, 10: 1},
        '其他，请注明.4': {-1: 0, 98: 1},

        '全部游戏都卡顿': {-1: 0, 99: 1},
        '微信': {-1: 0},
        '手机QQ': {-1: 0, 2: 1},
        '淘宝': {-1: 0, 3: 1},
        '京东': {-1: 0, 4: 1},
        '百度': {-1: 0, 5: 1},
        '今日头条': {-1: 0, 6: 1},
        '新浪微博': {-1: 0, 7: 1},
        '拼多多': {-1: 0, 8: 1},
        '其他，请注明.5': {-1: 0, 98: 1},
        '全部网页或APP都慢': {-1: 0, 99: 1},

    })


    pinpailist = ['realme', '锤子', '黑鲨', '联通', '联想', '魅族', '摩托罗拉', '诺基亚','欧博信','酷比','索尼爱立信','金立'
                  '欧珀', '其他', '奇酷', '三星', '万普', '万普拉斯', '中兴', '中邮通信', '中国移动','TD',
                  '北京珠穆朗玛移动通信有限公司','飞利浦','捷开通讯科技','维图','甄十信息科技（上海）有限公司','中国电信']
    for x in pinpailist:
        result.loc[result['终端品牌'] == x, '终端品牌'] = '其它品牌'


    # 对两个连续值的特征进行无量纲化
    # for col in ['脱网次数', 'mos质差次数','未接通掉话次数','套外流量（MB）','套外流量费（元）','语音通话-时长（分钟）',
    #             '省际漫游-时长（分钟）','当月ARPU','当月MOU','前3月ARPU','前3月MOU','GPRS总流量（KB）','GPRS-国内漫游-流量（KB）']:
    #     # maxAbsEnc = MaxAbsScaler()    # 归一到[-1，1]
    #     minMaxEnc = MinMaxScaler()    # 归一到[0，1]
    #     result[col] = minMaxEnc.fit_transform(result[col].values.reshape(-1, 1))

    # 独热编码
    result = pd.get_dummies(result, columns=['终端品牌'])

    return result

def test_encode(data):
    result = pd.DataFrame.copy(data, deep=True)

    result['终端品牌'] = result['终端品牌'].fillna(0)
    result = result.replace({
        '是否不限量套餐到达用户': {'是': 1, '否': 0},
        '性别': {'性别不详': 0, '女': 1, '男': 2},
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

        '网络信号差/没有信号': {-1: 0},
        '显示有信号上不了网': {-1: 0, 2: 1},
        '上网过程中网络时断时续或时快时慢': {-1: 0, 3: 1},
        '手机上网速度慢': {-1: 0, 4: 1},
        '其他，请注明.1': {-1: 0, 98: 1},

        '看视频卡顿': {-1: 0},
        '打游戏延时大': {-1: 0, 2: 1},
        '打开网页或APP图片慢': {-1: 0, 3: 1},
        '下载速度慢': {-1: 0, 4: 1},
        '手机支付较慢': {-1: 0, 5: 1},
        '其他，请注明.2': {-1: 0, 98: 1},

        '爱奇艺': {-1: 0},
        '优酷': {-1: 0, 2: 1},
        '腾讯视频': {-1: 0, 3: 1},
        '芒果TV': {-1: 0, 4: 1},
        '搜狐视频': {-1: 0, 5: 1},
        '抖音': {-1: 0, 6: 1},
        '快手': {-1: 0, 7: 1},
        '火山': {-1: 0, 8: 1},
        '咪咕视频': {-1: 0, 9: 1},
        '其他，请注明.3': {-1: 0, 98: 1},

        '全部都卡顿': {-1: 0, 99: 1},
        '和平精英': {-1: 0},
        '王者荣耀': {-1: 0, 2: 1},
        '穿越火线': {-1: 0, 3: 1},
        '梦幻西游': {-1: 0, 4: 1},
        '龙之谷': {-1: 0, 5: 1},
        '梦幻诛仙': {-1: 0, 6: 1},
        '欢乐斗地主': {-1: 0, 7: 1},
        '部落冲突': {-1: 0, 8: 1},
        '炉石传说': {-1: 0, 9: 1},
        '阴阳师': {-1: 0, 10: 1},
        '其他，请注明.4': {-1: 0, 98: 1},

        '全部游戏都卡顿': {-1: 0, 99: 1},
        '微信': {-1: 0},
        '手机QQ': {-1: 0, 2: 1},
        '淘宝': {-1: 0, 3: 1},
        '京东': {-1: 0, 4: 1},
        '百度': {-1: 0, 5: 1},
        '今日头条': {-1: 0, 6: 1},
        '新浪微博': {-1: 0, 7: 1},
        '拼多多': {-1: 0, 8: 1},
        '其他，请注明.5': {-1: 0, 98: 1},
        '全部网页或APP都慢': {-1: 0, 99: 1},

    })


    pinpailist = ['realme', '锤子', '黑鲨', '联通', '联想', '魅族', '摩托罗拉', '诺基亚','欧博信','酷比','索尼爱立信','金立'
                  '欧珀', '其他', '奇酷', '三星', '万普', '万普拉斯', '中兴', '中邮通信', '中国移动','TD','天翼',
                  '北京珠穆朗玛移动通信有限公司','飞利浦','捷开通讯科技','维图','甄十信息科技（上海）有限公司','中国电信']
    for x in pinpailist:
        result.loc[result['终端品牌'] == x, '终端品牌'] = '其它品牌'


    # 对两个连续值的特征进行无量纲化
    # for col in ['脱网次数', 'mos质差次数','未接通掉话次数','套外流量（MB）','套外流量费（元）','语音通话-时长（分钟）',
    #             '省际漫游-时长（分钟）','当月ARPU','当月MOU','前3月ARPU','前3月MOU','GPRS总流量（KB）','GPRS-国内漫游-流量（KB）']:
    #     # maxAbsEnc = MaxAbsScaler()    # 归一到[-1，1]
    #     minMaxEnc = MinMaxScaler()    # 归一到[0，1]
    #     result[col] = minMaxEnc.fit_transform(result[col].values.reshape(-1, 1))

    # 独热编码
    result = pd.get_dummies(result, columns=['终端品牌'])

    return result

# 对加载进来的数据集进行预处理
x_train_temp = train_encode(x_train)
x_test_temp = test_encode(x_test)


corr = x_train_temp.corr().abs()    # 相关系数绝对值
corr.to_excel('output/上网相关系数矩阵.xlsx')

k = 11
col = corr.nlargest(k, '手机上网整体满意度')['手机上网整体满意度'].index   #Top10索引
corr = corr.loc[col, col]   # Top10结果筛选
corr = corr.round(2)    # 保留两位小数

plt.subplots(figsize=(10, 10))
plt.subplots_adjust(left=0.25, bottom=0.25)
sns.heatmap(corr, annot=True, fmt="g", cmap='viridis')
plt.savefig('output/上网Top10相关性热图.png', dpi=300)
plt.show()

x_train = train_data.drop(['手机上网整体满意度'], axis=1)

x_train_temp.to_excel('output/上网训练集.xlsx',index=False)
x_test_temp.to_excel('output/上网测试集.xlsx',index=False)