import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
from sklearn import metrics
from sklearn.model_selection import train_test_split
import io

class IAProcessor:

  def __init__(self):
    self.train_data = pd.read_csv("train_data.csv")
    self.train_data.head()
    self.k = 10

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

  def process(self, df):
    """
    Realiza o processamento dos dados de teste
    
    Args:
        df: DataFrame dos dados de test
        
    Returns:
        Object: resposta com items e plot
    """
    trainData = self.train_data.drop('class', axis=1)
    trainClass = self.train_data.loc[:, 'class']
    testData = df.drop('class', axis=1)
    testClass = df.loc[:, 'class']

    return self.knn(trainData, trainClass, testData, testClass, self.k)

  def knn(self, trainSet, trainSetClass, testSet, testSetClass, k):
    """
    Processamento knn
    
    Args:
        trainData: DataFrame dos dados de treinamento
        trainClass: DataFrame da classificação dos dados de treinamento
        testData: DataFrame dos dados de teste
        testClass: DataFrame da classificação dos dados de teste
        k: Quantidade de elementos proximos
        
    Returns:
        Object: resposta com items e plot
    """
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

    confusion_matrix = metrics.confusion_matrix(testSetClass.to_numpy(), testPridictSetClass)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix)
    cm_display.plot()
    image = None
    with io.BytesIO() as buffer:
      plt.savefig(buffer, format='png')
      buffer.seek(0)
      image = buffer.getvalue()

    accuracy = metrics.accuracy_score(testSetClass.to_numpy(), testPridictSetClass)

    items = []
    for testIndex in testSet.index:
      items.append({ 'id': str(testIndex), 'predict': str(testPridictSetClass[testIndex]), 'trueResult': str(testSetClass[testIndex]) })

    return {'items': items, 'image': base64.b64encode(image).decode(), 'accuracy': str(accuracy)}