import pandas as pd
from sklearn.model_selection import train_test_split

def task():
    print("Running task_1_15: ")
    data = pd.read_csv('Data/winequality-red.csv', sep = ';') # When data separator needed

    X_tr_data = []
    y_tr_data = []
    X_va_data = []
    y_va_data = []
    X_te_data = []
    y_te_data = []

    _data_parser(data, X_tr_data, y_tr_data, X_va_data, y_va_data, X_te_data, y_te_data)

    print(X_tr_data)
    print(X_va_data)
    print(X_te_data)

def _data_parser(data, X_training_data, y_training_data, X_validation_data, y_validation_data, X_test_data, y_test_data):
    X = data.drop('quality', axis=1)
    y = data['quality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=0.25, random_state=1)

    print(X_train)
    print(X_test)
    print(X_validation)

    X_training_data = X_train
    X_validation_data = X_validation
    X_test_data = X_test
