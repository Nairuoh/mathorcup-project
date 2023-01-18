import pandas as pd  # 数据表处理
import numpy as np  # 数值运算，线性代数
import matplotlib.pyplot as plt  # 数据可视化绘图
plt.rcParams['figure.facecolor']=(1,1,1,1) # pycharm 绘图白底，看得清坐标
plt.rcParams['font.family'] = 'SimHei'
import seaborn as sns  # 数据可视化绘图
from scipy import stats  # 分布
from collections import Counter
from sklearn.model_selection import train_test_split,cross_val_score  # 划分训练集测试集、交叉验证
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,OrdinalEncoder, MinMaxScaler, MaxAbsScaler  # 特征编码
from sklearn.decomposition import PCA  # 数据降维
import time
import pickle as pkl  # 序列化
from sklearn.metrics import mean_squared_error, make_scorer, accuracy_score  # 评估指标
from pandas import DataFrame, Series
from sklearn.model_selection import KFold, StratifiedKFold  # 交叉验证
from sklearn.model_selection import GridSearchCV  # 网格搜索
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier # 随机森林回归模型
from xgboost import XGBClassifier


import warnings
warnings.filterwarnings("ignore")

train_data = pd.read_excel("output/语音训练集.xlsx",index_col='用户id')
test_data = pd.read_excel("output/语音测试集.xlsx",index_col='用户id')


# x_test = test_data.drop(['用户id'], axis=1)
# x_train = train_data.drop(col, axis=1)  # 训练集数据去掉这几列

corr = train_data.corr().abs()    # 相关系数绝对值
k = 9
col = corr.nlargest(k, '语音通话整体满意度')['语音通话整体满意度'].index   #Top10索引
col = col.delete(0)

y_train = train_data['语音通话整体满意度']  # 标签数据

x_train = train_data.loc[:, col]
x_test = test_data.loc[:, col]


# 用于记录本地时间
def get_local_time():
    return time.strftime("%m%d%H%M", time.localtime())


# 切分训练集和验证集
x_tr, x_va, y_tr, y_va = train_test_split(x_train, y_train, test_size = 0.2)

# 初始化随机森林回归模型
# random_forest_reg = RandomForestRegressor()

# 初始化分类模型
random_forest_cla = RandomForestClassifier()  # 随机森林
# model = XGBClassifier(learning_rate=0.001,
#                       max_depth=2,
#                       min_child_weight = 1,      # 叶子节点最小权重
#                       gamma=0.,                  # 惩罚项中叶子结点个数前的参数
#                       subsample=1,               # 所有样本建立决策树
#                       colsample_btree=1,         # 所有特征建立决策树
#                       scale_pos_weight=1,        # 解决样本个数不平衡的问题
#                       random_state=30,           # 随机数
#                       slient = 0,
#                       )


# 从里面搜索出让模型有最优表现的参数
param_grid = {'n_estimators': [10,50,100,200,300]}

# 定义网格搜索--从里面搜索出让模型有最优表现的参数
grid_search_cv = GridSearchCV(estimator=random_forest_cla, param_grid=param_grid,
                              scoring=make_scorer(mean_squared_error), n_jobs=-1, pre_dispatch=1, cv=5, verbose=1)
# 开始搜
grid_search_cv.fit(x_tr, y_tr)

x_va_pre = grid_search_cv.predict(x_va)
print('测试集上的MSE:', mean_squared_error(x_va_pre, y_va))  # 测试集上的MSE


# 回归时的四舍五入取整（回归的效果不如直接分类）
# for i in range(len(x_va_pre)):
#     x_va_pre[i] = round(x_va_pre[i])  # 取整
# print('取整后测试集上的MSE:', mean_squared_error(x_va_pre, y_va))  # 测试集上的MSE

val_acc = accuracy_score(y_va, x_va_pre)
print('预测正确率:', val_acc)  # 测试集上的MSE


# 查看最优的参数
print(grid_search_cv.best_params_)

# 特征重要性可视化----知道是可视化特征的重要性就行了
# feat_labels = x_train.columns[1:]
feat_labels = x_train.columns[:]
importances = grid_search_cv.best_estimator_.feature_importances_
indices = np.argsort(importances)[::-1]

plot_x = list()
plot_y = list()

# 获取特征名字
for f in range(x_train.shape[1]):
    try:
        plot_x.append(feat_labels[indices[f]])
        plot_y.append(importances[indices[f]])
#         print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))
    except:
        pass

plot_xy = pd.DataFrame({'Feature': plot_x, 'Importances': plot_y})

figure = plt.figure(figsize=(10, 10))
plt.subplots_adjust(bottom=0.25)
plt.xticks(rotation=90)
sns.barplot(x='Feature', y='Importances', data=plot_xy)
plt.savefig('output/特征-重要性图.png', dpi=300)

# 提交数据

test_predict = grid_search_cv.predict(x_test)
for i in range(len(test_predict)):
    test_predict[i] = round(test_predict[i])  # 取整

result = pd.DataFrame({'用户id': test_data.index, '语音通话整体满意度': test_predict})
time_stamp = get_local_time()
result.to_excel('output/语音通话整体满意度_randomforset-%s.xlsx'%time_stamp, index=False)



