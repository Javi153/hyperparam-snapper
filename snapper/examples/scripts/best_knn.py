from snapper_ml import job

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import pickle
import os

SEED = 1234

def main(n_neighbors=21, weights = 'distance', algorithm = 'brute', p = 1):
    os.chdir('/run/media/javier/1TB/Universidad/Master_UGR/ServidoresWeb/hyperparam-snapper/snapper')
    np.random.seed(SEED)
    baseball = pd.read_csv('examples/scripts/baseball.dat', header = 0)
    baseball_target = baseball['Salary']
    baseball_data = baseball.drop(['Salary'], axis = 1)
    X_train, X_val, y_train, y_val = train_test_split(baseball_data, baseball_target, random_state=SEED)
    model = KNeighborsRegressor(n_neighbors = n_neighbors, weights=weights, algorithm=algorithm, p = p)
    model.fit(X_train, y_train)
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    # accuracy = model.score(X_val, y_val)
    # return {'val_accuracy': accuracy}


if __name__ == '__main__':
    print(main())
