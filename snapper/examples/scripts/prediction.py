from snapper_ml import job

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import pickle
import os


def main(X):
    os.chdir('/run/media/javier/1TB/Universidad/Master_UGR/ServidoresWeb/hyperparam-snapper/snapper')
    model = pickle.load(open('finalized_model.sav', 'rb'))
    result = model.predict(X)
    return result

if __name__ == '__main__':
    print(main(np.array(eval(input()), ndmin = 2)))
