from NewElement import NewElement

class Element(NewElement):
    def __init__(self, a, b, c, itsClass):
        super().__init__(a, b, c)
        self.itsClass = itsClass

    def get_itsClass(Element):
            return Element.itsClass

    def set_itsClass(Element, itsClass):
            Element.itsClass = itsClass