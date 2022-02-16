
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant): #this is a specialized x of plant- it inherits the attributes from Plant
    def __init__(self,color, petals):
        Plant.__init__(self,color)
        #you can call methods from the supeclass, not the actuall attribute ex. __color
        self.__petals = petals

    def get_petals(self):
        return self.__petals
