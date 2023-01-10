import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plotDistribution(x):
    config = x

    # 读入数据
    # Titanic = pd.read_excel(r'泰坦尼克号乘客年龄分布.xlsx')
    train_data = pd.read_excel("output/语音训练集.xlsx",index_col='用户id')
    test_data = pd.read_excel("output/语音测试集.xlsx",index_col='用户id')


    # 检查年龄是否有缺失
    # any(Titanic.Age.isnull())
    # 不妨删除含有缺失年龄的观察
    # Titanic.dropna(subset=['Age'], inplace=True)

    #设置绘图风格
    # plt.style.use('ggplot')

    #处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    #坐标轴负号的处理
    plt.rcParams['axes.unicode_minus']=False

    plt.cla()

    # 取出男性年龄
    # Age_Male = Titanic.Age[Titanic.Sex == 'male']
    # 取出女性年龄
    # Age_Female = Titanic.Age[Titanic.Sex == 'female']

    # 取出脱网次数
    offlineNumber_train = train_data[config]
    offlineNumber_test = test_data[config]

    # seaborn模块绘制分组的直方图和核密度图
    # 绘制男女乘客年龄的直方图
    sns.distplot(offlineNumber_train, bins=20, kde = False, hist_kws={'color':'steelblue'},
                 label=('train', '直方图'), norm_hist=True)

    # 绘制女性年龄的直方图
    sns.distplot(offlineNumber_test, bins=20, kde = False, hist_kws={'color':'purple'},
                 label=('test', '直方图'), norm_hist=True)

    # 绘制男女乘客年龄的核密度图
    sns.distplot(offlineNumber_train, hist=False, kde_kws={'color':'red', 'linestyle':'-'},
                 norm_hist=True, label=('train', '核密度图'))
    # sns.kdeplot(offlineNumber_train, color='red', linestyle='-', label=('train', '核密度图'))

    # 绘制女性年龄的核密度图
    sns.distplot(offlineNumber_test, hist=False, kde_kws={'color':'black', 'linestyle':'--'},
                 norm_hist=True, label=('test', '核密度图'))
    # sns.kdeplot(offlineNumber_test, color='black', linestyle='--', label=('test', '核密度图'))

    plt.title('语音业务'+config+'分布图')
    plt.xlabel(config)
    plt.ylabel('核密度值-频率')

    # 显示图例
    plt.legend()

    plt.savefig('output/数据分布图/语音业务'+config+'分布图.png', dpi=300)

    # 显示图形
    # plt.show()


list = ['是否遇到过网络问题', '居民小区', '手机没有信号', '有信号无法拨通', '通话过程中突然中断', '办公室', '通话过程中一方听不见',
        '通话中有杂音、听不清、断断续续', '商业街']
for x in list:
    plotDistribution(x)

