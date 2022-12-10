from Element import Element
import numpy as np
from typing import List

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
        distance = np.linalg.norm(elementPosition - x.get_position())

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

