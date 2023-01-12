import pandas as pd  # 数据表处理
from pandas import DataFrame, Series
import numpy as np  # 数值运算，线性代数
import matplotlib.pyplot as plt  # 数据可视化绘图
import seaborn as sns  # 数据可视化绘图
plt.rcParams['figure.facecolor']=(1,1,1,1) # pycharm 绘图白底，看得清坐标
plt.rcParams['font.family'] = 'SimHei'
from sklearn.linear_model import Lasso


train_data = pd.read_excel("output/上网训练集.xlsx",index_col='用户')
# test_data = pd.read_excel("output/上网测试集.xlsx",index_col='用户id')

# x_train = train_data.drop(['网络覆盖与信号强度','手机上网速度','手机上网稳定性'])

x, y = train_data.iloc[:, 4:], train_data.iloc[:, 0:4]

# 取alpha=1000进行特征提取
lasso = Lasso(alpha=0.01, random_state=1)
lasso.fit(x, y)

# 相关系数
print('相关系数为', np.round(lasso.coef_, 5))
coef = pd.DataFrame(lasso.coef_.T, index=x.columns, columns=y.columns)

print('相关系数数组为\n', coef)
coef.to_excel('output/Lasso相关系数上网数组.xlsx')

# # 返回相关系数是否为0的布尔数组
# mask = lasso.coef_ != 0.0
#
# # 对特征进行选择
# x = x.loc[:, mask]
# new_reg_data = pd.concat([x, y], axis=1)
# new_reg_data.to_excel('output/Lasso_reg_data.xlsx',index=False)