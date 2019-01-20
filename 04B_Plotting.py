# This version stops betting when you hit zero.
# Rewritten with Classes
# How long does it take to hit zero?
# What is the biggest pile of money anyone wins?

import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


'''
Simple bettor, betting the same amount each time.
'''

class Bettor:

    def __init__(self,funds,initial_wager,wager_count):
        self.value = funds              # How much money we have available to bet
        self.wager = initial_wager      # How much money we bet on each roll
        self.wagercount = wager_count   # How many times we are willing to bet

    def bet(self):
        wX = []     # wager history - start with an empty array
        vY = []
        currentWager = 1
        keepbetting = True

        while keepbetting:
            if rollDice():
                self.value += self.wager
            else:
                self.value -= self.wager

            wX.append(currentWager)
            vY.append(self.value)

            if self.value == 0:   # stop betting when you get to zero
                keepbetting = False
            else:
                currentWager += 1
        self.EndPoint = currentWager
        self.MaxValue = np.max(vY)
        plt.plot(wX, vY)


x = 0
WagerArray = []
MaxArray = []

# start this off @ 1, then add, and increase 50 to 500, then 1000
while x < 100:
    A= Bettor(10000, 100, 50000) # funds, initial wager, wager count
    A.bet()
    WagerArray.append(A.EndPoint)
    MaxArray.append(A.MaxValue)
    x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
AvgWager = np.average(WagerArray)
print("The average bettor lasted ", AvgWager, " wagers before going broke.")
print("The fastest bettor lasted ", np.min(WagerArray), " wagers.")
print("The slowest bettor lasted ", np.max(WagerArray), " wagers.")
print("The highest pile of money was ", np.max(MaxArray))