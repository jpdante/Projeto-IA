from Element import Element
import numpy as np
from typing import List
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

class Knn:

    def __init__(self):
        self.elements = list()

    def classify(self, element, k):
        for x in self.elements:
            distancy = self.euclideanDistance(element, x)
            x.set_distancy(distancy)
        sorted: List[Element] = sorted(self.elements, key=element.get_position())
        nearstNeighbors = sorted[:self.k]
        element.itsClass = self.moreFrequent(nearstNeighbors)
        self.append(element)

    def euclideanDistance(self, element1, element2):
        distance = np.linalg.norm(element1.get_position() - element2.get_position())

    def moreFrequent(self, nearstNeighbors: List[Element]):
        mostFrequent = 0
        mostFrequentElement
        for x in nearstNeighbors:
            current_frequency = List.count(x)
            if (current_frequency > mostFrequent):
                mostFrequent = current_frequency
                mostFrequentElement = x
        return mostFrequentElement

    def getElements(self):
        return self.elements

    def append(self, element):
        self.elements.append(element)
    def confusionMatrix(self, correctList):
        correctListClasses = List[string]
        elementsClasses = List[string]
        for x in correctList:
            correctListClasses.append(x.get_itsClass)
        for x in self.elements:
            elementsClasses.append(x.get_itsClass)
        confusion_matrix = metrics.confusion_matrix(elementsClasses, correctListClasses)
        cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[False, True])
        cm_display.plot()
        plt.show()
        plt.savefig(sys.stdout.buffer)
        sys.stdout.flush()

