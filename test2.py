import pandas as pd
import quandl 
import math
import numpy as numpy
from sklearn import preprocessing, cross_validation, svm
import csv

df = pd.read_csv('CS_2012.csv')
print(df[1:])

