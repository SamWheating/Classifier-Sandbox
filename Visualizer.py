from tkinter import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.patches as mpatches
from sklearn import neighbors, datasets
from sklearn.decomposition import PCA
import pandas

# end imports

matplotlib.use('TkAgg')

# GLOBAL VARIABLES & CONTROLS

INPUT_DATA = "SpinalData.csv"

# Load and Triage Data:

inputData  = pandas.read_csv(INPUT_DATA)
labels = inputData['class']
inputData = inputData.drop(['class'], axis=1)
mapping = {'Hernia':0, 'Spondylolisthesis':1, 'Normal':2}
labels_ints = labels.map(mapping)

# Use PCA to reduce to 2 dimensional data

pca = PCA(n_components=2)
pca.fit(inputData)
PCAData = pca.transform(inputData)
PCAData = pandas.DataFrame(PCAData)

# Join integer class labels and PCA

PCAData = pandas.concat([PCAData, labels_ints], axis=1)
PCAData.columns = ['PCA1', 'PCA2', 'Class']

# remove outliers:

PCAData = PCAData.query('PCA1 < 150')

classes = PCAData['Class']
colours = PCAData['Class']

# Create color maps

def makeGraph(n_neighbors, h, patient, weighting):

    plt.close()

    print("Regenerating plot...\n")

    patient = np.array(patient)
    patient = patient.reshape(1, -1)
    patient = pca.transform(patient)

    print(patient)

    y = PCAData['Class']
    X = PCAData.drop(['Class'], axis=1)

#    y = y.reshape(-1,1)

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#FF00FF'])

    # Convert Dataframes to Numpy Arrays
    
    X = X.as_matrix()
    y = y.as_matrix()

    X = np.append(X, patient, axis=0)
    y = np.append(y, 3)

    X_all = X
    y_all = y

    X = X[:-1]
    y = y[:-1]

    # Generate KNN Plot (largely taken from SKLearn Documentation)

#   for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weighting)
    clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(12,9))
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X_all[:, 0], X_all[:, 1], c=y_all, cmap=cmap_bold, 
                edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weighting))

    red_patch = mpatches.Patch(color='red', label='Hernia')
    blue_patch = mpatches.Patch(color='blue', label='Normal')
    green_patch = mpatches.Patch(color='green', label='Spondylolisthesis')
    pink_patch = mpatches.Patch(color='#FF00FF', label='Patient')
    plt.legend(handles=[red_patch, blue_patch, green_patch, pink_patch], loc=4)


    if(clf.predict(X_all[-1].reshape(1, -1)) == 1):
        print("Patient likely has Spondylolisthesis")
    if(clf.predict(X_all[-1].reshape(1, -1)) == 0):
        print("Patient spine is possibly herniated")
    if(clf.predict(X_all[-1].reshape(1, -1)) == 2):
        print("Patient spine is normal")

    plt.show()