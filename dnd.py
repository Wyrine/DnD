#!/usr/bin/env python3

import random as rand

def rolldice(upperPlusOne):
    rand.seed()
    return rand.randrange(1, upperPlusOne)



if __name__ == '__main__':
    print(rolldice(21))
