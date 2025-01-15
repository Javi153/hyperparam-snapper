import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import pickle



def model_prediction(X):
    model = pickle.load(open('finalized_model.sav', 'rb'))
    result = model.predict(X)
    return result

