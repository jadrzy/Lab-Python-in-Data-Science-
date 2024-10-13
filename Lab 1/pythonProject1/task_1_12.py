import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task():
    print("Running task_1_12: ")
    data = pd.read_csv('Data/winequality-red.csv', sep = ';') # When data separator needed

    scatterplot = sns.scatterplot(data = data, x = 'pH', y = 'density', hue='quality')
    scatterplot.set_title('Simple scatterplot')
    plt.show()