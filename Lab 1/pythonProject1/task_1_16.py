import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task():
    print("Running task_1_12: ")
    print("Quality would be a perfect target if we wanted to: "
          "\n - maximize the quality of the produced wine" 
          "\n - gather information about the best proportion of components" 
          "\n - and enhance the production process")

    print("\nBased on data's heatmap features that could be excluded are:"
          "\n - citric acid"
          "\n - density"
          "\n - pH"
          "\n - free sulfur dioxide")

    data = pd.read_csv('Data/winequality-red.csv', sep = ';') # When data separator needed
    corr = data.corr()
    plt.figure(figsize=(15, 8))
    heatmap = sns.heatmap(corr, cmap='crest', annot=True)
    heatmap.set_title('Heatmap')
    plt.show()