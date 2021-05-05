# What is the point of this repo?

This is a pickeled model that will return probability predictions of whether or not a given creditcard transaction is fraudulent from a dataset on openML available here: https://www.openml.org/d/1597

In order to successfully run this project first clone it and navigate to the directory then
```pip install -r requirements.txt```
After installing the requirements, the notebook is an easy way to visualize the project. clf.pickle is a fit pipeline that will return predictions once loaded from memory and passed with .predict_proba(). newdata.json is data from the credit card dataset saved as JSON. 
test_pickle.py can be inspected to view the benefit to a pickled model. As long as it is loaded from memory properly any user can pass it new data that it would qualify as fit to and get returned a prediction.
