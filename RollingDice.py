import random,time
from random import randint
def roll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    print("Die 1:", die1)
    print("Die 2:", die2)
    print("Die 3:", die3)
    if die1 == die2 and die2 == die3:
        print('You got a three of a kind!')
    elif die1 == die2 or die2 == die3 or die1 == die3:
        print("There was one pair!")
    else:
        print('Better luck next time!')
    time.sleep(.5)
roll()