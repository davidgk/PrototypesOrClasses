
class Car(object):

    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

    def brand(self):
        return self.__brand

    def color(self):
        return self.__color



