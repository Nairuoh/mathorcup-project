#!/usr/bin/env python
# coding: utf-8

# # 上网业务——手机上网整体满意度

# In[1]:


# from sklearnex import patch_sklearn, config_context
# patch_sklearn()


# In[2]:


from lightgbm import LGBMClassifier
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier,RandomForestClassifier,StackingClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,accuracy_score
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import missingno as msno
from time import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['font.sans-serif']=['SimHei']


# ##  预处理数据导入

# In[3]:


train = pd.read_excel("./output/上网训练集.xlsx")


# In[4]:


train_data = pd.DataFrame.copy(train, deep=True)
# train_data


# In[5]:


train_data=train_data.drop(['用户', '网络覆盖与信号强度', '手机上网速度', '手机上网稳定性'],axis=1)
# train_data


# ## 相关性分析

# In[6]:


cor = pd.DataFrame(train_data.corr().abs()["手机上网整体满意度"].sort_values(ascending = False))
cor.columns = ["手机上网整体满意度"]
# cor[0:20]


# In[7]:


corr = train_data.corr().abs()
k = 9
col = corr.nlargest(k, '手机上网整体满意度')['手机上网整体满意度'].index   #Top10 index
corr = corr.loc[col, col]
corr = corr.round(2)

plt.subplots(figsize=(20, 20))
plt.subplots_adjust(left=0.25, bottom=0.25)
sns.heatmap(corr, annot=True, fmt="g", cmap='viridis')
plt.savefig('./output/手机上网整体满意度相关性.png', dpi=300)
plt.show()


# ## 数据划分

# In[8]:


x = train_data.loc[:, col].drop(['手机上网整体满意度'],axis=1)
# x


# In[9]:


y = train_data["手机上网整体满意度"]
# y


# In[10]:


x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)


# ## 模型训练

# In[11]:


rg = RidgeClassifier()
parameters = {
    "alpha":[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
    "normalize":[True,False]
}

rg_cv = GridSearchCV(rg, parameters, cv=5)
rg_cv.fit(x_train,y_train)
# rg_cv.best_estimator_


# In[12]:


dt = DecisionTreeClassifier()
parameters = {
    "criterion":['gini', 'entropy','log_loss'],
    "max_depth":[2,4,8,16],
    "min_samples_leaf":[2,4,8,16],
    "min_samples_split":[2,4,8,16,32]
}

dt_cv = GridSearchCV(dt, parameters, cv=5)
dt_cv.fit(x_train,y_train)
# dt_cv.best_estimator_


# In[13]:


rf = RandomForestClassifier()
parameters = {
    "max_depth":[2,4,8,16],
    "n_estimators":[5,50,250,500]
}

rf_cv = GridSearchCV(rf, parameters, cv=5)
rf_cv.fit(x_train,y_train)
# rf_cv.best_estimator_


# In[14]:


ada = AdaBoostClassifier()
parameters = {
    "learning_rate":[0.01,0.1,1.0],
    "n_estimators":[5,50,250,500]
}

ada_cv = GridSearchCV(ada, parameters, cv=5)
ada_cv.fit(x_train,y_train)
# ada_cv.best_estimator_


# In[15]:


gb = GradientBoostingClassifier()
parameters = {
    "learning_rate":[0.01,0.1,1.0],
    "max_depth":[2,4,8,16],
    "n_estimators":[5,25,50,250,500]
}

gb_cv = GridSearchCV(gb, parameters, cv=5)
gb_cv.fit(x_train,y_train)
# gb_cv.best_estimator_


# In[16]:


xgb = XGBClassifier(eval_metric='mlogloss')
parameters = {
    "n_estimators":[5,25,50,250],
    "max_depth":[2,4,8],
    "learning_rate":[0.01,0.1,1.0]
}

xgb_cv = GridSearchCV(xgb, parameters, cv=5)
xgb_cv.fit(x_train,y_train)
# xgb_cv.best_estimator_


# In[17]:


svr = SVC(kernel='poly')
parameters = {
    "C":[0.001,0.01],
}

svr_cv = GridSearchCV(svr, parameters, cv=5)
svr_cv.fit(x_train,y_train)
# svr_cv.best_estimator_


# In[18]:


mlp = MLPClassifier(activation='logistic')
parameters = {
    "hidden_layer_sizes":[(10,),(50,)],
    "learning_rate":["constant","invscaling","adaptive"],
    "solver":["lbfgs","sgd","adam"]
}

mlp_cv = GridSearchCV(mlp, parameters, cv=5)
mlp_cv.fit(x_train, y_train)
# mlp_cv.best_estimator_


# In[19]:


estimators = [("rg",rg_cv.best_estimator_),
              ("dt",dt_cv.best_estimator_),
              ("rf",rf_cv.best_estimator_),
              ("ada",ada_cv.best_estimator_),
              ("gb",gb_cv.best_estimator_),
              ("xgb",xgb_cv.best_estimator_),
              ("svr",svr_cv.best_estimator_),
              ("mlp",mlp_cv.best_estimator_)]

sr = StackingClassifier(estimators=estimators)
parameters = {
    "passthrough":[True,False]
}

sr_cv = GridSearchCV(sr, parameters, cv=5)
sr_cv.fit(x_train,y_train)
# sr_cv.best_estimator_


# In[20]:


models = [rg_cv.best_estimator_,
          dt_cv.best_estimator_,
          rf_cv.best_estimator_,
          ada_cv.best_estimator_,
          gb_cv.best_estimator_,
          xgb_cv.best_estimator_,
          svr_cv.best_estimator_,
          mlp_cv.best_estimator_,
          sr_cv.best_estimator_]


# In[21]:


val_set = pd.DataFrame()
    
for i in models:
        start = time()
        pred = i.predict(x_val)
        end = time()        
        temp = pd.DataFrame(
                {   
                    "Train Acc":("%0.3f" % (i.score(x_train,y_train))),
                    "Test Acc":("%0.3f" % (accuracy_score(y_val,pred))),
                    "MAE":("%0.3f" % (mean_absolute_error(y_val,pred))),
                    "MSE":("%0.3f" % (mean_squared_error(y_val,pred))),
                    "Latency":("%0.1fms" % ((end-start)*1000))
                }, index=[(str(i).split("(")[0])]
        )
        val_set = pd.concat([val_set,temp])
# val_set


# ## 预测（StackingClassifier）

# In[22]:


test = pd.read_excel("./output/上网测试集.xlsx")


# In[23]:


test_data = pd.DataFrame.copy(test, deep=True)
# test_data


# In[24]:


test_col = col.drop('手机上网整体满意度')


# In[25]:


test_data = test_data.loc[:, test_col]
# test_data


# In[26]:


y_pred_test = sr_cv.best_estimator_.predict(test_data)
output = pd.DataFrame({'Id': test['用户id'], '手机上网整体满意度': np.round(y_pred_test, 0)})
output.to_excel('./output//result-手机上网整体满意度.xlsx', index=False)

