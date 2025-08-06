# import pandas
# from sklearn import linear_model

# df = pandas.read_csv("data.csv")

# X = df[['Weight', 'Volume']]
# y = df['CO2']

# regr = linear_model.LinearRegression()
# regr.fit(X, y)

# #predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
# predictedCO2 = regr.predict([[2300, 1300]])
# # print(X,y)
# print("The result is ", predictedCO2)


import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)