1.  偏度（Skewness） 

        对Sample构成的分布的对称性状况的描述。正态分布的 Skewness=0。
        如果 Skewness>0 代表波形有右侧长尾，如果 Skewness<0代表波形有左侧长尾。
        
2.  Kurtosis(峰度)

        对Sample构成的分布的峰值是否突兀或是平坦的描述。
        正态分布的Kurtosis为 k=3，为了描述的方便，使用exceess_k=k−3来标准化表示。
        如果exceess_k>0, 表示波形更平坦(flatness); 如果 exceess_k<0, 则表示波形更突兀消瘦(peakedness).

参考链接：
https://blog.csdn.net/baidu_28858149/article/details/50553414

3.  特征数据的归一化和标注化

        归一化：通过减去最小值，然后除以（Max-min）使数据归一化,Scikit-learn通过MinMaxScaler来实现（比如神经网络就需要输入值得范围使0到1）
        标准化：通过减去平均值，然后除以方差，使得到的分布具有单位方差，标注化受到异常值的影响很小，Scikit-learn通过StandardScaler


参考链接：
https://scikit-learn.org/stable/modules/preprocessing.html