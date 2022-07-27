##2nd model 

##importing the model
import pickle  #to load a saved model

import pandas as pd
from sklearn.model_selection import train_test_split


##read the csv file
df = pd.read_csv('1-2years.csv')

import xgboost as xgb
from sklearn.model_selection import train_test_split

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

xtrain, xtest, ytrain, ytest=train_test_split(X, y, test_size=0.15)

xgbr = xgb.XGBRegressor(verbosity=0) # verbosity=0 means silent

##the given parameters are used to train the model, and can be adjusted to get better results.

# XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
#        colsample_bynode=1, colsample_bytree=1, gamma=0,
#        importance_type='gain', learning_rate=0.1, max_delta_step=0,
#        max_depth=3, min_child_weight=1, missing=None, n_estimators=100,
#        n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
#        reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
#        silent=None, subsample=1, verbosity=1)


xgbr.fit(xtrain, ytrain)


##dump the model to a file
pickle.dump(xgbr, open('2nd_model.pkl', 'wb'))


