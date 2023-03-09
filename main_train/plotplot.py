import matplotlib.pyplot as plt
import random
import pandas as pd
## 如遇中文显示问题，执行以下代码：
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

data = pd.read_excel('特征加权.xlsx')
x = data['特征加权和']
y = data['计数']
# 随机生成两列温度数据，一行时间x坐标轴
# y_guangzhou = [random.uniform(20,25) for i in range(60)]
# y_beijing = [random.uniform(1,3) for i in range(60)]
# x_label = ["11点{}分".format(i) for i in range(60)]

# 创建画布
plt.figure(figsize=(20,10),dpi=100)
# 放入x、y的数据，
plt.plot(x,y,color='g',linestyle='--',label='语音')
# plt.plot(x_label,y_beijing,color='b',linestyle='-.',label='北京')
# 为了让上面的图例label显示出来
plt.legend()
# 坐标轴隔多少显示一个（步长）
plt.yticks(range(0, 41)[::50])
plt.xticks(x[::10])
# 网格
plt.grid(True,linestyle='-.',alpha=0.5)
# x坐标、y坐标和标题
plt.xlabel("特征加权和")
plt.ylabel("计数")
plt.title("特征散点图")
plt.show()



