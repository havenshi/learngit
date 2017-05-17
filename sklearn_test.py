# -*- coding:utf8 -*-
from sklearn.datasets import load_iris

#导入IRIS数据集
iris = load_iris()
# [[ 4.9  3.   1.4  0.2]...]
#特征矩阵
iris.data

#目标向量
iris.target


#一、数据预处理
#1.无量纲化，转换到同一规格

from sklearn.preprocessing import StandardScaler
#1.1标准化，返回值为标准化后的数据。依照特征矩阵的列处理数据
StandardScaler().fit_transform(iris.data)

from sklearn.preprocessing import MinMaxScaler
#1.2区间缩放，返回值为缩放到[0, 1]区间的数据
MinMaxScaler().fit_transform(iris.data)

from sklearn.preprocessing import Normalizer
#1.3归一化，返回值为归一化后的数据。依照特征矩阵的行处理数据
Normalizer().fit_transform(iris.data)

#2.对定量特征二值化，1或0

from sklearn.preprocessing import Binarizer
#二值化，阈值设置为3，返回值为二值化后的数据
Binarizer(threshold=3).fit_transform(iris.data)

#3.对定性特征哑编码，定性特征转换为定量特征

from sklearn.preprocessing import OneHotEncoder
#哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
OneHotEncoder().fit_transform(iris.target.reshape((-1,1)))

#4.缺失值计算

from numpy import vstack, array, nan
from sklearn.preprocessing import Imputer
#缺失值计算，返回值为计算缺失值后的数据
#参数missing_value为缺失值的表示形式，默认为NaN
#参数strategy为缺失值填充方式，默认为mean（均值）
Imputer().fit_transform(vstack((array([nan, nan, nan, nan]), iris.data)))

#5.数据变换

from sklearn.preprocessing import PolynomialFeatures
#多项式转换，数据矩阵增加列和行
#参数degree为度，默认值为2
PolynomialFeatures().fit_transform(iris.data)

from numpy import log1p
from sklearn.preprocessing import FunctionTransformer
#自定义转换函数为对数函数的数据变换
#第一个参数是单变元函数，使用单变元的函数来转换数据
FunctionTransformer(log1p).fit_transform(iris.data)


#二、特征选择
#1.Filter：过滤法，按照发散性或者相关性对各个特征进行评分，设定阈值或者待选择阈值的个数，选择特征。

#1.1 方差选择法，选择某一列
from sklearn.feature_selection import VarianceThreshold
#方差选择法，返回值为特征选择后的数据
#参数threshold为方差的阈值
VarianceThreshold(threshold=3).fit_transform(iris.data)

#1.2 相关系数法

from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr

#选择K个最好的特征，返回选择特征后的数据
#第一个参数为计算评估特征是否好的函数，该函数输入特征矩阵和目标向量，输出二元组（评分，P值）的数组，数组第i项为第i个特征的评分和P值。在此定义为计算相关系数
#参数k为选择的特征个数
#SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)

#1.3 卡方检验，选择某几列
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#选择K个最好的特征，返回选择特征后的数据
SelectKBest(chi2, k=2).fit_transform(iris.data, iris.target)

#1.4 互信息法
from sklearn.feature_selection import SelectKBest
from minepy import MINE

#由于MINE的设计不是函数式的，定义mic方法将其为函数式的，返回一个二元组，二元组的第2项设置成固定的P值0.5
# def mic(x, y):
#     m = MINE()
#     m.compute_score(x, y)
#     return (m.mic(), 0.5)
#
# #选择K个最好的特征，返回特征选择后的数据
# SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)

#2.Wrapper：包装法，根据目标函数（通常是预测效果评分），每次选择若干特征，或者排除若干特征。将权值系数较小的特征从特征集合中消除。
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
#递归特征消除法，返回特征选择后的数据
#参数estimator为基模型
#参数n_features_to_select为选择的特征个数
RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(iris.data, iris.target)

#3.Embedded：嵌入法，先使用某些机器学习的算法和模型进行训练，得到各个特征的权值系数，根据系数从大到小选择特征。选择权值系数较高的特征。

#3.1 基于惩罚项的特征选择法
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
#带L1惩罚项的逻辑回归作为基模型的特征选择
SelectFromModel(LogisticRegression(penalty="l1", C=0.1)).fit_transform(iris.data, iris.target)

#3.2 基于树模型的特征选择法
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
#GBDT作为基模型的特征选择
SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)


#三、降维

#1.主成分分析法（PCA）
from sklearn.decomposition import PCA
#主成分分析法，返回降维后的数据
#参数n_components为主成分数目
PCA(n_components=2).fit_transform(iris.data)

#2.线性判别分析法（LDA）
# from sklearn.lda import LDA
# #线性判别分析法，返回降维后的数据
# #参数n_components为降维后的维数
# LDA(n_components=2).fit_transform(iris.data, iris.target)