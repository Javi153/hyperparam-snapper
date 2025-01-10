from snapper_ml import job

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

SEED = 1234


@job  # ADD THIS DECORATOR
def main(C=1.0, kernel='rbf', degree=3, gamma='scale'):
    np.random.seed(SEED)
    iris = load_iris()
    X_train, X_val, y_train, y_val = train_test_split(iris.data, iris.target, random_state=SEED)
    model = SVC(C=C, gamma=gamma, kernel=kernel, degree=degree)
    model.fit(X_train, y_train)
    accuracy = model.score(X_val, y_val)
    return {'val_accuracy': accuracy}


if __name__ == '__main__':
    main()
