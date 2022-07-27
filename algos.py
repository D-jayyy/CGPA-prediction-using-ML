##You are required to develop a machine learning system to predict final CGPA of a student using csv file.

                                    #made by CS-19076, CS-19100, CS-19121

'''
            PLEASE NOTE:
                        RUN ONLY ONE ALGORITHM AT A TIME'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


##reading the csv files
df = pd.read_csv('1-2years.csv')

# ## for reading the 2nd_model i.e 1-3 years csv file

# # df = pd.read_csv('1_3years.csv')

# ##using XGBoost to predict the CGPA.

import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, KFold

X = df.drop(['CGPA'], axis=1)
y = df['CGPA']

xtrain, xtest, ytrain, ytest=train_test_split(X, y, test_size=0.15)

xgbr = xgb.XGBRegressor(verbosity=0) 
# print(xgbr)

##the given parameters are used to train the model, and can be adjusted to get better results.

# XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
#        colsample_bynode=1, colsample_bytree=1, gamma=0,
#        importance_type='gain', learning_rate=0.1, max_delta_step=0,
#        max_depth=3, min_child_weight=1, missing=None, n_estimators=100,
#        n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
#        reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
#        silent=None, subsample=1, verbosity=1)


xgbr.fit(xtrain, ytrain)
print(xgbr.predict(xtest))

score = xgbr.score(xtrain, ytrain)  
print("Training score of XGBoost algo: ", score)

#using k-fold cross validation to get the accuracy of the model.
kfold = KFold(n_splits=10, shuffle=True)
kf_cv_scores = cross_val_score(xgbr, xtrain, ytrain, cv=kfold )
print("K-fold CV average score: %.2f" % kf_cv_scores.mean())





##using svm regression model

# ##importing libraries
# from sklearn.svm import SVR

# X = df.drop(['CGPA'], axis=1)
# y = df['CGPA']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

# ##implementing svm regression model

# svr_regressor = SVR(kernel = 'linear')
# svr_regressor.fit(X_train, y_train)

# y_pred = svr_regressor.predict(X_test)
# # print(y_pred)
# print("SVM score: ",svr_regressor.score(X_test, y_test))
# #calculating the rms

# print("Mean squared error: ",mean_squared_error(y_test, y_pred))


##using lasso regression model


# from sklearn.linear_model import Lasso

# ##split the data into training and testing data
# X = df.drop(['CGPA'], axis=1)
# y = df['CGPA']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# ##create the model
# lasso = Lasso(alpha=0.1)
# lasso.fit(X_train, y_train)
# y_pred = lasso.predict(X_test)
# print('Lasso score: ', lasso.score(X_test, y_test))
# print('Mean squared error: ', mean_squared_error(y_test, y_pred))




# ##using linear regression model

# from sklearn.linear_model import LinearRegression

# X = df.iloc[:, :-1].values
# y = df.iloc[:, -1].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


# regressor = LinearRegression()
# regressor.fit(X_train, y_train)
# y_pred=regressor.predict(X_test)
# print('regression score: ',regressor.score(X_test, y_test))
# print('Mean squared error: ', mean_squared_error(y_test, y_pred))


