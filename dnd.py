#!/usr/local/bin python3

import random as rand

def rolldice(diceRoll):
    print("d%d roll: " % (diceRoll), end="")
    return rand.randint(1, diceRoll)



if __name__ == '__main__':
    rand.seed()
    rollNum = 0
    while True:
        rollNum = int(input("What kind of dice would you like to roll? -1 to exit: "))
        if rollNum == -1: break
        print(rolldice(rollNum))
    print("Thanks for playing. Hope you didn't die!")
