import numpy as np
import matplotlib.pyplot as plt

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')

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
score1 = [496,332,180,140,244,298,257,251]  # 658
score2 = [475,258,159,111,206,267,231,160] # 786
score3= [736,409,200,169,285,343,286,308]  # 2701
score1 = [x / 658 for x in score1]
score2 = [x / 786 for x in score2]
score3 = [x / 2701 for x in score3]

#语音通话整体满意度 低分
# score1 = [137,112,71,94,80,74,78,77]  # 145
# score2 = [23,18,18,15,17,13,14,16]  # 26
# score3= [48,41,24,36,33,26,36,33]  # 50
# score4 = [37,32,22,18,24,19,25,27]  # 37
# score5 = [123,93,70,76,85,63,79,74]  # 135
# score1 = [x / 145 for x in score1]
# score2 = [x / 26 for x in score2]
# score3 = [x / 50 for x in score3]
# score4 = [x / 37 for x in score4]
# score5 = [x / 135 for x in score5]

#网络覆盖与信号强度
# score1 = [222,180,124,121,138,129,129,172]  # 237
# score2 = [59,51,28,36,39,40,41,42]  #62
# score3= [89,70,52,46,62,60,61,63]  #90
# score4 = [85,69,43,40,48,49,46,53]  #90
# score5 = [195,141,92,91,110,123,112,122]  #211
# score1 = [x / 237 for x in score1]
# score2 = [x / 62 for x in score2]
# score3 = [x / 90 for x in score3]
# score4 = [x / 90 for x in score4]
# score5 = [x / 211 for x in score5]

# #语音通话清晰度
# score1 = [171,138,96,132,94,111,110,104]  # 184
# score2 = [38,32,23,26,22,24,32,28]  #40
# score3= [58,45,37,36,30,38,39,40]  #59
# score4 = [82,61,47,45,46,50,54,49]  #85
# score5 = [149,115,70,90,69,82,98,87]  #161
# score1 = [x / 184 for x in score1]
# score2 = [x / 40 for x in score2]
# score3 = [x / 59 for x in score3]
# score4 = [x / 85 for x in score4]
# score5 = [x / 161 for x in score5]

# 语音通话稳定性
# score1 = [216,172,119,157,124,150,139,132]  # 230
# score2 = [46,39,25,32,28,32,36,29]  #49
# score3 = [81,65,41,55,42,55,50,59]  #83
# score4 = [89,71,51,59,40,57,61,53]  #93
# score5 = [191,138,91,106,79,113,114,112]  #201
# score1 = [x / 230 for x in score1]
# score2 = [x / 49 for x in score2]
# score3 = [x / 83 for x in score3]
# score4 = [x / 93 for x in score4]
# score5 = [x / 201 for x in score5]

# # 手机上网整体满意度
# score1 = [232,172,268,195,243,219,156,193]  # 345
# score2 = [41,38,49,32,36,37,18,31]  #63
# score3 = [92,71,116,89,108,93,66,78]  #149
# score4 = [73,57,88,68,88,77,51,67]  #122
# score5 = [203,136,221,174,199,190,112,150]  #305
# score1 = [x / 345 for x in score1]
# score2 = [x / 64 for x in score2]
# score3 = [x / 149 for x in score3]
# score4 = [x / 122 for x in score4]
# score5 = [x / 305 for x in score5]

# 手机上网稳定性
# score1 = [317,233,354,276,321,287,201,239]  # 462
# score2 = [75,57,91,69,90,84,54,69]  #121
# score3 = [172,132,206,167,175,176,120,153]  #254
# score4 = [126,99,147,121,138,121,83,100]  #191
# score5 = [296,185,343,241,297,284,167,230]  #462
# score1 = [x / 462 for x in score1]
# score2 = [x / 121 for x in score2]
# score3 = [x / 254 for x in score3]
# score4 = [x / 191 for x in score4]
# score5 = [x / 462 for x in score5]

#手机上网速度
# score1 = [276,207,322,240,276,280,196,238]  # 415
# score2 = [71,52,77,67,80,73,55,61]  # 104
# score3 = [172,124,185,140,164,174,114,148]  # 235
# score4 = [123,103,148,105,140,136,79,107]  # 199
# score5 = [282,177,318,236,281,270,179,221]  # 454
# score1 = [x / 415 for x in score1]
# score2 = [x / 104 for x in score2]
# score3 = [x / 235 for x in score3]
# score4 = [x / 199 for x in score4]
# score5 = [x / 454 for x in score5]

#网络覆盖与信号强度——上网
# score1 = [300,210,348,246,289,281,293,242]  # 429
# score2 = [77,63,94,78,76,75,49,61]  # 117
# score3 = [151,122,187,140,161,158,113,137]  # 228
# score4 = [128,86,150,111,131,128,82,104]  # 198
# score5 = [281,168,317,236,271,260,156,208]  # 435
# score1 = [x / 429 for x in score1]
# score2 = [x / 117 for x in score2]
# score3 = [x / 228 for x in score3]
# score4 = [x / 198 for x in score4]
# score5 = [x / 435 for x in score5]

# feature = ["居民小区","办公室","网络信号差/没有信号","显示有信号上不了网","上网过程中网络时断时续或时快时慢","手机上网速度慢","看视频卡顿",'打开网页或APP图片慢']
feature = ["是否遇到过网络问题","居民小区","办公室","手机没有信号","通话中有杂音、听不清、断断续续","有信号无法拨通","通话过程中突然中断","通话过程中一方听不见"]
N = len(score1)

#设置雷达图的角度，用于平分切开一个平面
angles = np.linspace(0,2*np.pi,N,endpoint=False)

#使雷达图封闭起来
values = np.concatenate((score1,[score1[0]]))
angles = np.concatenate((angles,[angles[0]]))
feature=np.concatenate((feature,[feature[0]]))

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
ax.set_thetagrids(angles*180/np.pi,feature)

#设置极轴范围
ax.set_ylim(0,1)

#添加标题
plt.title('网络覆盖与信号强度-高分')

#增加网格纸
ax.grid(True)
plt.legend()
plt.show()
