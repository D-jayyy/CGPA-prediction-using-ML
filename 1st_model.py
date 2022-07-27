##1st_model

#You are required to develop a machine learning system to predict final CGPA of a student using csv file.
 

import pickle  #to load a saved model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


##read the csv file
df = pd.read_csv('1-3years.csv')


#implementing regression model

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


regressor = LinearRegression()
regressor.fit(X_train, y_train)

##dumping the model,so it doesn't have to be trained again

pickle.dump(regressor, open('1st_model.pkl', 'wb'))


