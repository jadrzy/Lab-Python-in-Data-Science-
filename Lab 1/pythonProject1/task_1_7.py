import pandas as pd

def task():
    print("Running task_1_7: ")
    data = pd.read_csv('Data/winequality-red.csv', sep = ';') # When data separator needed

    print(data.head())
    print(data.describe())