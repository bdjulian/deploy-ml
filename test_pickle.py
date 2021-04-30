import pandas as pd
import sklearn
from sklearn.datasets import fetch_openml
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import json

with open('newdata.json') as f:
    data = json.load(f)
    
pickle_off = open("clf.pickle","rb")
model = pickle.load(pickle_off)
print(model)

preds = model.predict_proba([data])
print(preds)