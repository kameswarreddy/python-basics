# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:27:27 2022

@author: Bharath kuamr reddy
"""
### machine learning project practice
### sales prediction 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("D:\ML practice\sales pridiction.csv")
df.head()
df.columns
df.info()
x = np.array(df.drop('Sales',1))
x
y = np.array(df['Sales'])
y
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)
model = LinearRegression()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
ypred.shape
plt.scatter(ytest, ypred)
plt.fit(ytest, ypred)
plt.ylabel('Predicted')
plt.xlabel('Y test')
import seaborn as sns
a = df['TV']
a
sns.jointplot(a,y,df)
sns.pairplot(df)
model.coef_
import sklearn.metrics as metrics
print('MAE: {}'.format(metrics.mean_absolute_error(ytest, ypred)))
print('MSE: {}'.format(metrics.mean_squared_error(ytest, ypred)))
print('RMSE: {}'.format(np.sqrt(metrics.mean_squared_error(ytest, ypred))))
metrics.r2_score(ytest, ypred)
df.close()



##### Tips prediction
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("D:\\ML practice\\tip prediction.csv")
df.info()
df.describe()
df["sex"] = df["sex"].map({"Female": 0, "Male": 1})
df["smoker"] = df["smoker"].map({"No": 0, "Yes": 1})
df["day"] = df["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
df["time"] = df["time"].map({"Lunch": 0, "Dinner": 1})
df.head()
x = df.drop('tip',1)
y = df['tip']
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)
model = LinearRegression()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
import sklearn.metrics as metrics
print('MAE: {}'.format(metrics.mean_absolute_error(ytest, ypred)))
print('MSE: {}'.format(metrics.mean_squared_error(ytest, ypred)))
print('RMSE: {}'.format(np.sqrt(metrics.mean_squared_error(ytest, ypred))))
metrics.r2_score(ytest, ypred)
features = np.array([[24.50, 1, 0, 0, 1, 4]])
model.predict(features)



### product demand predicyion
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df1 = pd.read_csv("D:\ML practice\demand prediction.csv")
df1.describe()
df1.info()
df1.isnull().sum()
df2 = df1.dropna()
df2.isnull().sum()
df2.info()
x = df2[['Total Price','Base Price']]
y = df2['Units Sold']
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)
model = LinearRegression()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
print('MAE: {}'.format(metrics.mean_absolute_error(ytest, ypred)))
print('MSE: {}'.format(metrics.mean_squared_error(ytest, ypred)))
print('RMSE: {}'.format(np.sqrt(metrics.mean_squared_error(ytest, ypred))))
metrics.r2_score(ytest, ypred)

## try with another alog for better accuracy
from sklearn.tree import DecisionTreeRegressor
correlations = df2.corr(method='pearson')
plt.figure(figsize=(8, 6))
sns.heatmap(correlations, cmap="coolwarm", annot=True)
plt.show()
model2 = DecisionTreeRegressor()
model2.fit(xtrain, ytrain)
ypred2 = model2.predict(xtest)
print(ypred2)
print('MAE: {}'.format(metrics.mean_absolute_error(ytest, ypred)))
print('MSE: {}'.format(metrics.mean_squared_error(ytest, ypred)))
print('RMSE: {}'.format(np.sqrt(metrics.mean_squared_error(ytest, ypred))))
metrics.r2_score(ytest, ypred2)
features = np.array([[133.00, 140.00]])
model2.predict(features)
df1.close()
