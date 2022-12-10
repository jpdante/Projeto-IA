from Element import Element
from NewElement import NewElement
from Knn import Knn

if __name__ == '__main__':

    knn = Knn()

    element1 = Element(1, 1, 1, 'a')
    element2 = Element(2, 2, 2, 'b')
    element3 = Element(3, 3, 3, 'c')
    element4 = Element(4, 4, 4, 'd')
    element5 = NewElement(1.9, 1.9, 1.9)

    knn.append(element1)
    knn.append(element2)
    knn.append(element3)
    knn.append(element4)
    knn.append(element5)

    knn.classify(element5, 3)
    print(element5.get_itsClass())
    #resultado esperado = b


