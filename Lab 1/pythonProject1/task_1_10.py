import pandas as pd
import matplotlib   .pyplot as plt

def task():
    print("Running task_1_10: ")
    data = pd.read_csv('Data/winequality-red.csv', sep = ';') # When data separator needed

    #print(data.head())
    #print(data.describe())

    # Quality
    quality = data['quality']
    plt.hist(quality)
    plt.title('1. Quality distribution')
    plt.xlabel('Quality')
    plt.ylabel('Count')
    plt.grid()
    plt.savefig('Plots/plot.png', dpi=600)
    plt.show()
