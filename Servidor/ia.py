import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

class IAProcessor:

  def __init__(self):
    self.elements = list()

  def getEuclidianDistance(self, p, q):
    """
    Calcula a distancia euclidiana entre 2 elementos
    
    Args:
        p: Primeiro elemento
        q: Segundo elemento
        
    Returns:
        Float: Distancia euclidiana
    """
    return np.linalg.norm(np.array(p) - np.array(q))

  def knn(self, trainSet, trainSetClass, testSet, testSetClass, k):
    testPridictSetClass = []

    for testIndex in testSet.index:
      testElement = testSet.iloc[testIndex]
      distances = []

      for trainIndex in trainSet.index:
        trainElement = trainSet.iloc[trainIndex]
        distances.append(self.getEuclidianDistance(trainElement, testElement))
      
      distanceSetDF = pd.DataFrame(data=distances, index=trainSet.index, columns=['dist'])
      distanceSetDF.head()

      dfnn = distanceSetDF.sort_values(by=['dist'], axis=0)[:k]
      counter = Counter(trainSetClass[dfnn.index])
      testPridictSetClass.append(counter.most_common()[0][0])

    gotRight = 0
    for idx, x in enumerate(testPridictSetClass):
      if x == testSetClass.iloc[idx]:
        gotRight += 1

    print(str(gotRight) + "/" + str(len(testPridictSetClass)))

    confusion_matrix = metrics.confusion_matrix(testSetClass.to_numpy(), testPridictSetClass)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix)
    cm_display.plot()
    plt.show()

  def do(self):
    iris = datasets.load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df.head()

    trainData = df.drop('target', axis=1)
    trainClassification = df.target

    testElement = [4.8, 2.7, 2.5, 0.7]

    distances = []
    for i in trainData.index:
      trainElement = trainData.iloc[i]
      distances.append(self.getEuclidianDistance(trainElement, testElement))
    
    df_dists = pd.DataFrame(data=distances, index=trainData.index, columns=['dist'])
    df_dists.head()
    
    k = 5

    df_nn = df_dists.sort_values(by=['dist'], axis=0)[:k]
    counter = Counter(trainClassification[df_nn.index])
    testClassification = counter.most_common()[0][0]

    confusion_matrix = metrics.confusion_matrix([1], [testClassification])
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix)
    cm_display.plot()
    plt.show()
    # print(self.getEuclidianDistance(p, q))

ia = IAProcessor()
#ia.do()

iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['class'] = iris.target
df.head()

df_train, df_test = train_test_split(df, train_size=0.7)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

ia.knn(df_train.drop('class', axis=1), df_train.loc[:, 'class'], df_test.drop('class', axis=1), df_test.loc[:, 'class'], 15)