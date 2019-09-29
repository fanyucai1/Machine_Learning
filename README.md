1.  偏度（Skewness） 

        对Sample构成的分布的对称性状况的描述。正态分布的 Skewness=0。
        如果 Skewness>0 代表波形有右侧长尾，如果 Skewness<0代表波形有左侧长尾。
        
2.  Kurtosis(峰度)

        对Sample构成的分布的峰值是否突兀或是平坦的描述。
        正态分布的Kurtosis为 k=3，为了描述的方便，使用exceess_k=k−3来标准化表示。
        如果exceess_k>0, 表示波形更平坦(flatness); 如果 exceess_k<0, 则表示波形更突兀消瘦(peakedness).

参考链接：
https://blog.csdn.net/baidu_28858149/article/details/50553414

3.  特征数据预处理（sklearn.preprocessing）

        Scale：MinMaxScaler,MaxAbsScaler(MaxAbsScaler 和 maxabs_scale这两个方法是专门为稀疏数据的规模化所设计的。如果你的数据有许多异常值可以使用robust_scale 和 RobustScaler这两个方法。它会根据中位数或者四分位数去中心化数据。)
        normalize：通过减去平均值，然后除以方差，使得到的分布具有单位方差，标注化受到异常值的影响很小，经常被使用在分类与聚类中。

参考链接：
https://scikit-learn.org/stable/modules/preprocessing.html


4. DataFrame与array之间的互相转化

        df = pd.dataframe()
        arr = df.values
 --- 

5.  机器学习框架

参考链接：https://docs.microsoft.com/en-us/azure/machine-learning/studio/algorithm-choice

| Algorithm                           | Accuracy | Training time | Linearity | Parameters | Notes                                           | 
|-------------------------------------|----------|---------------|-----------|------------|-------------------------------------------------| 
| **Two-class classification**        |          |               |           |            |                                                 | 
| logistic regression                 |          | ●             | ●         | 5          |                                                 | 
| decision forest                     | ●        | ○             |           | 6          |                                                 | 
| decision jungle                     | ●        | ○             |           | 6          | Low memory footprint                            | 
| boosted decision tree               | ●        | ○             |           | 6          | Large memory footprint                          | 
| neural network                      | ●        |               |           | 9          | Additional customization is possible            | 
| averaged perceptron                 | ○        | ○             | ●         | 4          |                                                 | 
| support vector machine              |          | ○             | ●         | 5          | Good for large feature sets                     | 
| locally deep support vector machine | ○        |               |           | 8          | Good for large feature sets                     | 
| Bayes’ point machine                |          | ○             | ●         | 3          |                                                 | 
| **Multi-class classification**      |          |               |           |            |                                                 | 
| logistic regression                 |          | ●             | ●         | 5          |                                                 | 
| decision forest                     | ●        | ○             |           | 6          |                                                 | 
| decision jungle                     | ●        | ○             |           | 6          | Low memory footprint                            | 
| neural network                      | ●        |               |           | 9          | Additional customization is possible            | 
| one-v-all                           | -        | -             | -         | -          | See properties of the two-class method selected | 
| **Regression**                      |          |               |           |            |                                                 | 
| linear                              |          | ●             | ●         | 4          |                                                 | 
| Bayesian linear                     |          | ○             | ●         | 2          |                                                 | 
| decision forest                     | ●        | ○             |           | 6          |                                                 | 
| boosted decision tree               | ●        | ○             |           | 5          | Large memory footprint                          | 
| fast forest quantile                | ●        | ○             |           | 9          | Distributions rather than point predictions     | 
| neural network                      | ●        |               |           | 9          | Additional customization is possible            | 
| Poisson                             |          |               | ●         | 5          | Technically log-linear. For predicting counts   | 
| ordinal                             |          |               |           | 0          | For predicting rank-ordering                    | 
| **Anomaly detection**               |          |               |           |            |                                                 | 
| support vector machine              | ○        | ○             |           | 2          | Especially good for large feature sets          | 
| PCA-based anomaly detection         |          | ○             | ●         | 3          |                                                 | 
| K-means                             |          | ○             | ●         | 4          | A clustering algorithm                          |

 --- 

