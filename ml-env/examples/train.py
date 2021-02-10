import numpy as np

import joblib

from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split


filename_p = "model.joblib"


if __name__ == "__main__":

    digits = datasets.load_digits()
    X_train, X_test, y_train, y_test = train_test_split(
        digits.data, digits.target, random_state=0
    )

    clf = svm.SVC(gamma=0.001, C=100.0)
    clf.fit(X_train, y_train)

    joblib.dump(clf, filename_p)
