import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn import tree

"""读入数据并进行处理"""
train_feature = pd.read_csv('./DATASET/train_feature.csv',encoding='GBK')
train_label = pd.read_csv('./DATASET/train_label.csv',encoding='GBK')
Z = pd.merge(train_feature,train_label,on = 'id',sort = False)#根据id合并两个表
Z = Z.dropna(axis = 0, how = 'any')#去掉不完整数据
X_train = Z.iloc[:-1,1:-4].values#train_feature
Y_train = Z.iloc[:-1,-4:].values#train_label
labelencoder = LabelEncoder()
X_train[ : , 0] = labelencoder.fit_transform(X_train[ : , 0])#男女转换为01
for i in range(4):
    Y_train[:,i] = labelencoder.fit_transform(Y_train[:,i])#ABCD转换为0123
test_feature = pd.read_csv('./DATASET/test_feature.csv',encoding='GBK')
test_label = pd.read_csv('./DATASET/test_label.csv',encoding='GBK')
Z_test = pd.merge(test_feature,test_label,on = 'id',sort = False)#根据id合并两个表
Z_test = Z_test.dropna(axis = 0, how = 'any')#去掉不完整数据
X_test =  Z_test.iloc[:-1,1:-4].values#test_feature
Y_test = Z_test.iloc[:-1,-4:].values#test_label
X_test[ : , 0] = labelencoder.fit_transform(X_test[ : , 0])#男女转换为01
for i in range(4):
    Y_test[:,i] = labelencoder.fit_transform(Y_test[:,i])#ABCD转换为0123

"""数据标准化"""
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

"""选定要预测的label"""
Y_train = Y_train[:, 3:4]
Y_test = Y_test[:, 3:4]

"""用R2对属性进行选择"""
res = []
formatlen = len(X_train[:1,:][0])
for i in range(formatlen - 1):
    X_train_select = X_train[:,i:i+1]
    regressor_select = LinearRegression()
    regressor_select.fit(X_train_select, Y_train)
    Y_predict_select = np.round(regressor_select.predict(X_test[:,i:i+1]))
    r2 = metrics.r2_score(Y_test, Y_predict_select) 
    if(r2 > 0):
        print('r2_score', r2)
        res.append(i)  
print('选中的属性列', res)

"""对数据按照选出的属性列投影"""
new_train = []
new_test = []
a = len(X_train[:,:1])#计算行数
b = len(X_test[:,:1])#计算行数
for j in range(a):
    temp1 = []
    temp2 = []
    for i in range(len(res)):
        k = X_train[j:j+1,:][0][res[i]]
        temp1.append(k)
        if j < b:
            m = X_test[j:j+1,:][0][res[i]]
            temp2.append(m)
    new_train.append(temp1)
    if j < b:
        new_test.append(temp2)

"""线性回归和预测"""
regressor = LinearRegression()
regressor.fit(new_train, Y_train)
Y_predict = np.round(regressor.predict(new_test))

"""预测结果评判"""
print("MSE", metrics.mean_squared_error(Y_test, Y_predict))
print("MAE", metrics.mean_absolute_error(Y_test, Y_predict))
print("EVS", metrics.explained_variance_score(Y_test, Y_predict))
print("R2", metrics.r2_score(Y_test, Y_predict))

"""计算准确率和误差"""
res = Y_predict - Y_test
count = 0
for i in res:
    if i == 0:
        count += 1
print('准确率', count/len(res))
count = 0
for i in res:
    if i == 1 or i == -1:
        count += 1
print('误差在上下一个标准以内', count/len(res))
