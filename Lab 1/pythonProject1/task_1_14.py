import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task():
    print("Running task_1_12: ")
    data = pd.read_csv('Data/winequality-red.csv', sep = ';') # When data separator needed

    corr = data.corr()
    plt.figure(figsize=(15,8))
    heatmap = sns.heatmap(corr, cmap='crest', annot=True)
    heatmap.set_title('Heatmap')
    plt.show()