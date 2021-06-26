class BMI:
    __phight = 0
    __pweight = 0
    def __gethight(self):
        return self.__phight
    def __sethight(self, inValue):
        self.__phight = inValue

    def __getweight(self):
        return self.__pweight
    def __setweight(self, inValue):
        self.__pweight = inValue

    hight = property(__gethight,__sethight)
    weight = property(__getweight,__setweight)


    def BMI_Value(self):
        return self.__phight / self.__pweight ** 2