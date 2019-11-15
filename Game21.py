import random

class Game21:
    def __init__(self):
        self.__nLast = -1
    def takeTurn(self, sInput):
        if self.__nLast == -1:
            self.__nLast = 0
            return("Welcome to my game")
        else:
            aInput = sInput.split(",")
            self.__nLast = int(aInput[-1]) + 1
            if self.__nLast == 21:
                return "21.... You win this time!"
            nNumbers = random.randint(1,3)
            sReturn = ""
            for n in range(0, nNumbers):
                sReturn += str(self.__nLast) + ","
                if self.__nLast == 20:
                    return sReturn + " ... I win"
                self.__nLast += 1
            return sReturn
        
