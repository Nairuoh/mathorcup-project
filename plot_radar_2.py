import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # 数据表处理

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')

title = '网络覆盖与信号强度'

titles = ['语音通话整体满意度', '语音通话稳定性', '语音通话清晰度', '网络覆盖与信号强度',
          '手机上网整体满意度', '手机上网稳定性', '手机上网速度', '网络覆盖与信号强度_上网']

features = ["居民小区", "办公室", "网络信号差/没有信号", "显示有信号上不了网", "上网过程中网络时断时续或时快时慢",
           "手机上网速度慢","看视频卡顿",'打开网页或APP图片慢']
# features = ["是否遇到过网络问题","居民小区","办公室","手机没有信号","通话中有杂音、听不清、断断续续","有信号无法拨通",
#            "通话过程中突然中断","通话过程中一方听不见"]

data = pd.read_excel("data2/"+ title +"_上网_new.xls")

# data_1 = data.loc[data[title].apply(lambda a:1 == a)]
# data_2 = data.loc[data[title].apply(lambda a:2 == a)]
# data_3 = data.loc[data[title].apply(lambda a:3 == a)]
# data_4 = data.loc[data[title].apply(lambda a:4 == a)]
# data_5 = data.loc[data[title].apply(lambda a:5 == a)]
# data_6 = data.loc[data[title].apply(lambda a:6 == a)]
# data_7 = data.loc[data[title].apply(lambda a:7 == a)]
data_8 = data.loc[data[title].apply(lambda a:8 == a)]
data_9 = data.loc[data[title].apply(lambda a:9 == a)]
data_10 = data.loc[data[title].apply(lambda a:10 == a)]
data_mean = data.loc[data[title].apply(lambda a:a <= 10 & a >= 8)]


# score1 = []
# score2 = []
# score3 = []
# score4 = []
# score5 = []
# score6 = []
# score7 = []
score8 = []
score9 = []
score10 = []
score_mean = []

for feature in features:
    # score1.append(data_1[feature].mean())
    # score2.append(data_2[feature].mean())
    # score3.append(data_3[feature].mean())
    # score4.append(data_4[feature].mean())
    # score5.append(data_5[feature].mean())
    # score6.append(data_6[feature].mean())
    # score7.append(data_7[feature].mean())
    score8.append(data_8[feature].mean())
    score9.append(data_9[feature].mean())
    score10.append(data_10[feature].mean())
    score_mean.append(data_mean[feature].mean())

# score1 = [x / size_1 for x in score1]
# score2 = [x / size_2 for x in score2]
# score3 = [x / size_3 for x in score3]
# score4 = [x / size_4 for x in score4]
# score5 = [x / size_5 for x in score5]
# score6 = [x / size_6 for x in score6]
# score7 = [x / size_7 for x in score7]
# score8 = [x / size_8 for x in score8]
# score9 = [x / size_9 for x in score9]
# score10 = [x / size_10 for x in score10]

# 语音通话稳定性 高分
# score1 = [516,345,189,240,162,260,312,284]  # 654
# score2 = [477,258,168,199,122,201,251,210] # 786
# score3= [773,435,205,338,176,271,362,301]  # 2800
# score1 = [x / 654 for x in score1]
# score2 = [x / 786 for x in score2]
# score3 = [x / 2800 for x in score3]

# 语音通话整体满意度 高分
# score1 = [445,286,192,232,277,156,233,228]  # 567
# score2 = [494,279,173,204,296,139,228,229] # 764
# score3= [1050,619,294,456,493,236,421,456]  # 3157
# score1 = [x / 567 for x in score1]
# score2 = [x / 764 for x in score2]
# score3 = [x / 3157 for x in score3]

# 语音通话清晰度 高分
# score1 = [503,340,194,262,173,256,308,270]  # 643
# score2 = [518,293,187,206,136,239,290,233] # 805
# score3= [926,528,260,403,213,368,410,395]  # 2981
# score1 = [x / 643 for x in score1]
# score2 = [x / 805 for x in score2]
# score3 = [x / 2981 for x in score3]

# 网络覆盖与信号强度 高分
# score1 = [496,332,180,140,244,298,257,251]  # 658
# score2 = [475,258,159,111,206,267,231,160] # 786
# score3= [736,409,200,169,285,343,286,308]  # 2701
# score1 = [x / 658 for x in score1]
# score2 = [x / 786 for x in score2]
# score3 = [x / 2701 for x in score3]


# feature = ["居民小区","办公室","网络信号差/没有信号","显示有信号上不了网","上网过程中网络时断时续或时快时慢","手机上网速度慢","看视频卡顿",'打开网页或APP图片慢']
# feature = ["是否遇到过网络问题","居民小区","办公室","手机没有信号","通话中有杂音、听不清、断断续续","有信号无法拨通","通话过程中突然中断","通话过程中一方听不见"]
N = len(score8)

#设置雷达图的角度，用于平分切开一个平面
angles = np.linspace(0, 2*np.pi, N, endpoint=False)

#使雷达图封闭起来

angles = np.concatenate((angles,[angles[0]]))
features = np.concatenate((features, [features[0]]))


# values_1 = np.concatenate((score1,[score1[0]]))
# values_2 = np.concatenate((score2,[score2[0]]))
# values_3 = np.concatenate((score3,[score3[0]]))
# values_4 = np.concatenate((score4,[score4[0]]))
# values_5 = np.concatenate((score5,[score5[0]]))
# values_6 = np.concatenate((score6,[score6[0]]))
# values_7 = np.concatenate((score7,[score7[0]]))
values_8 = np.concatenate((score8,[score8[0]]))
values_9 = np.concatenate((score9,[score9[0]]))
values_10 = np.concatenate((score10,[score10[0]]))
values_mean = np.concatenate((score_mean,[score_mean[0]]))


#绘图
fig = plt.figure()

#设置为极坐标格式
ax = fig.add_subplot(111, polar=True)

#绘制折线图

# ax.plot(angles, values_1, '|-', linewidth=2, label='1分')
# ax.plot(angles, values_2, '|-', linewidth=2, label='2分')
# ax.plot(angles, values_3, '|-', linewidth=2, label='3分')
# ax.plot(angles, values_4, '|-', linewidth=2, label='4分')
# ax.plot(angles, values_5, '|-', color='teal', linewidth=2, label='5分')
# ax.plot(angles, values_6, 'v-', color='aquamarine', linewidth=2, label='6分')
# ax.plot(angles, values_7, 'v-', color='chartreuse', linewidth=2, label='7分')
ax.plot(angles, values_8, '*-', color='darkorange', linewidth=2, label='8分')
ax.plot(angles, values_9, '*-', color='yellow', linewidth=2, label='9分')
ax.plot(angles, values_10, '*-', color='black', linewidth=2, label='10分')
ax.plot(angles, values_mean, 'o-', color='hotpink', linewidth=2, label='平均分')


#添加每个特质的标签
ax.set_thetagrids(angles * 180 / np.pi, features)

#设置极轴范围
ax.set_ylim(0,1)

#添加标题
plt.title(title)

#增加网格纸
ax.grid(True)
plt.legend(loc='upper right', bbox_to_anchor=(1.15,1.05))
plt.show()
