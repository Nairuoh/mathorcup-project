import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # 数据表处理

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')

title = '网络覆盖与信号强度'

features = ["居民小区", "办公室", "网络信号差/没有信号", "显示有信号上不了网", "上网过程中网络时断时续或时快时慢",
           "手机上网速度慢","看视频卡顿",'打开网页或APP图片慢']

data = pd.read_excel("data2/"+ title +"_上网_new.xls")

data_8 = data.loc[data[title].apply(lambda a:8 == a)]
data_9 = data.loc[data[title].apply(lambda a:9 == a)]
data_10 = data.loc[data[title].apply(lambda a:10 == a)]

size_8 = data_8.shape[0]
size_9 = data_9.shape[0]
size_10 = data_10.shape[0]

score1 = []
score2 = []
score3 = []
for feature in features:
    score1.append(data_8[feature].sum())
    score2.append(data_9[feature].sum())
    score3.append(data_10[feature].sum())

score1 = [x / size_8 for x in score1]
score2 = [x / size_9 for x in score2]
score3 = [x / size_10 for x in score3]

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
N = len(score1)

#设置雷达图的角度，用于平分切开一个平面
angles = np.linspace(0,2*np.pi,N,endpoint=False)

#使雷达图封闭起来
values = np.concatenate((score1,[score1[0]]))
angles = np.concatenate((angles,[angles[0]]))
features=np.concatenate((features, [features[0]]))

values_1 = np.concatenate((score2,[score2[0]]))
values_2 = np.concatenate((score3,[score3[0]]))
# values_3 = np.concatenate((score4,[score4[0]]))
# values_4 = np.concatenate((score5,[score5[0]]))

#绘图
fig = plt.figure()

#设置为极坐标格式
ax = fig.add_subplot(111, polar=True)

#绘制折线图
ax.plot(angles,values,'o-',linewidth=2,label='8分')
ax.plot(angles,values_1,'o-',linewidth=2,label='9分')
ax.plot(angles,values_2,'o-',linewidth=2,label='10分')

# ax.plot(angles,values,'o-',linewidth=2,label='1分')
# ax.plot(angles,values_1,'o-',linewidth=2,label='2分')
# ax.plot(angles,values_2,'o-',linewidth=2,label='3分')
# ax.plot(angles,values_3,'o-',linewidth=2,label='4分')
# ax.plot(angles,values_4,'o-',linewidth=2,label='5分')

#添加每个特质的标签
ax.set_thetagrids(angles * 180 / np.pi, features)

#设置极轴范围
ax.set_ylim(0,1)

#添加标题
plt.title(title+'_上网-高分')

#增加网格纸
ax.grid(True)
plt.legend()
plt.show()
