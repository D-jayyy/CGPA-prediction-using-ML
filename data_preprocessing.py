##preprocessing data in The_Grades_Dataset.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ##categorical data
dataset = pd.read_csv('1-2years.csv')
dataset.drop("Seat No.", axis=1, inplace=True)
print(dataset.head())

##filling missing values
dataset.apply(lambda x: np.nan if isinstance(x, str) and x.isspace() else x)
dataset.fillna("C+", inplace=True)




##categorical data to numeric data
dataset.replace("A+", 4, inplace=True)
dataset.replace("A", 4, inplace=True)
dataset.replace("A-", 3.7, inplace=True)
dataset.replace("B+", 3.4, inplace=True)
dataset.replace("B", 3.0, inplace=True)
dataset.replace("B-", 2.7, inplace=True)
dataset.replace("C+", 2.4, inplace=True)
dataset.replace("C", 2.0, inplace=True)
dataset.replace("C-", 1.7, inplace=True)
dataset.replace("D+", 1.4, inplace=True)
dataset.replace("D", 1.0, inplace=True)
dataset.replace("F", 0, inplace=True)
dataset.replace("WU", 0, inplace=True)
dataset.replace("W", 0, inplace=True)
dataset.replace("I",0,inplace=True)




print(dataset.head())

##checking for missing values
print(dataset.isnull().sum())


##saving changes to csv file
dataset.to_csv('1-2years.csv', index=False)









