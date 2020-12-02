import random

class Game21:
    def __init__(self):
        self.__nLast = -1
    def takeTurn(self, sInput):
        if self.__nLast == -1:
            self.__nLast = 1
            return("""
Welcome to my game!
In this game the object is to make your opponent the computer
count the number 21 You type a series of up to 3 numbers for your turn.
The computer does the same.
""")
        else:
            aInput = sInput.split(",")
            # test aInput
            try:
                print(self.__nLast, "is nLast")
                print(aInput[0], "is aInput[0]")
                if int(aInput[0]) != self.__nLast:
                    return "Start counting at " + str(self.__nLast)
                nLast = self.__nLast
                for sNumber in aInput:
                    if int(sNumber) != nLast:
                        return "Please make sure your numbers are in order"
                    nLast += 1
                self.__nLast = nLast
            except:
                return "Enter numbers please"
            if self.__nLast == 21:
                return "21.... You win this time!"
            # see if 20 is in range
            if self.__nLast > 17:
                nNumbers = 21 - self.__nLast
            else:
                nNumbers = random.randint(1,3)
            sReturn = ""
            for n in range(0, nNumbers):
                sReturn += str(self.__nLast) + ","
                if self.__nLast == 20:
                    return sReturn + " ... I win"
                self.__nLast += 1
            return sReturn
        
