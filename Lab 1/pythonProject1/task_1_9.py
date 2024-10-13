import pandas as pd
import matplotlib   .pyplot as plt

def task():
    print("Running task_1_9: ")
    data = pd.read_csv('Data/winequality-red.csv', sep = ';') # When data separator needed

    # Quality
    quality = data['quality']
    plt.hist(quality)
    plt.title('1. Quality distribution')
    plt.xlabel('Quality')
    plt.ylabel('Count')
    plt.grid()
    plt.show()

    #Scatterplot
    citric_acid = data['citric acid']
    fixed_acidity = data['fixed acidity']

    plt.scatter(citric_acid, fixed_acidity)
    plt.title('2. Scatterplot citric acid and fixed acidity')
    plt.xlabel('Citric acid')
    plt.ylabel('Fixed acidity')
    plt.grid()
    plt.show()

    chlorides = data['chlorides']
    plt.boxplot(chlorides)
    plt.title('3. Boxplot of chlorides')
    plt.ylabel('Chlorides')
    plt.grid()
    plt.show()
