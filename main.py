from Game21 import Game21

oGame = Game21()

while True:
    sInput = input("> ")
    sReturn = oGame.takeTurn(sInput)
    print(sReturn)
