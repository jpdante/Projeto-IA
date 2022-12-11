class NewElement:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.position = [self.a, self.b, self.c]

    def get_a(self):
            return self.a

    def set_a(self, a):
            self.a = a

    def get_b(self):
            return self.b

    def set_b(self, b):
            self.b = b

    def get_c(self):
            return self.c

    def set_c(self, c):
            self.c = c

    def get_position(self):
            return self.position

    def set_position(self, position):
            self.position = position

    def get_distancy(self):
            return self.distancy

    def set_distancy(self, distancy):
            self.distancy = distancy