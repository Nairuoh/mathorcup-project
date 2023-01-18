import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plotDistribution(x):
    config = x

    # 读入数据
    # Titanic = pd.read_excel(r'泰坦尼克号乘客年龄分布.xlsx')
    train_data = pd.read_excel("output/上网训练集.xlsx",index_col='用户')
    test_data = pd.read_excel("output/上网测试集.xlsx",index_col='用户id')


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

    # 取出数据
    Number_train = train_data[config]
    Number_test = test_data[config]

    # seaborn模块绘制分组的直方图和核密度图
    # 绘制男女乘客年龄的直方图
    sns.distplot(Number_train, bins=5, kde=False, hist_kws={'color':'steelblue'},
                 label=('train', '直方图'), norm_hist=True)
    # 绘制女性年龄的直方图
    sns.distplot(Number_test, bins=5, kde=False, hist_kws={'color':'purple'},
                 label=('test', '直方图'), norm_hist=True)
    # 绘制男女乘客年龄的核密度图
    sns.distplot(Number_train, hist=False, kde_kws={'color':'red', 'linestyle':'-'},
                 norm_hist=True, label=('train', '核密度图'))
    # 绘制女性年龄的核密度图
    sns.distplot(Number_test, hist=False, kde_kws={'color':'black', 'linestyle':'--'},
                 norm_hist=True, label=('test', '核密度图'))

    plt.title('上网业务'+config+'分布图')
    plt.xlabel(config)
    plt.ylabel('核密度值-频率')

    # 显示图例
    plt.legend()

    plt.savefig('output/上网数据分布/上网业务网络信号差_没有信号分布图.png', dpi=300)

    # 显示图形
    # plt.show()


# list = ['手机上网速度慢', '上网过程中网络时断时续或时快时慢', '打开网页或APP图片慢', '居民小区',
#         '显示有信号上不了网', '办公室','看视频卡顿', '打游戏延时大','下载速度慢', '地铁','全部网页或APP都慢','手机支付较慢',
#         '全部都卡顿','商业街','微信','高铁','淘宝','终端品牌_苹果','王者荣耀','腾讯视频','京东','农村','抖音']
# for x in list:
#     plotDistribution(x)

plotDistribution('网络信号差/没有信号')
