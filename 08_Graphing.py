# Of the survivors, who is the winner, also,
# is there a point at which a bettor should stop
# as their odds significantly decrease after a certain point?

# MGV - this version compares simple bettor - with standard initial wager (plots in black),
# and with an initial wager twice the size (plots in cyan).
# It does not use double bettor.
# The big thing this module introduces is changing the colors of the curves on the graph.
# plt.plot(xarray, yarray, color)
# plt.axhline(0, color='r')
# plt.xlabel('Label (units)')
# plt.ylabel('Label (units)')

import random
import matplotlib
import matplotlib.pyplot as plt
import time

# Since we will be comparing bettors, and eventually maybe have a handful,
# it would be wise to just set the starting funds, wager size, and
# wager count ahead of time globally.

sampleSize = 10

startingFunds = 10000
wagerSize = 100
wagerCount = 1000


def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


def doubler_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    currentWager += 10000000000000000
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * 2
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    currentWager += 10000000000000000

        currentWager += 1
    # this guy goes cyan #
    plt.plot(wX, vY, 'c')


#####                                           color#
def simple_bettor(funds, initial_wager, wager_count, color):
    ####

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

            ###add me
            if value < 0:
                currentWager += 10000000000000000
        currentWager += 1

    # this guy goes green #
    plt.plot(wX, vY, color)


x = 0

while x < sampleSize:
    simple_bettor(startingFunds, wagerSize, wagerCount, 'k')
    simple_bettor(startingFunds, wagerSize * 2, wagerCount, 'c')
    # doubler_bettor(startingFunds,wagerSize,wagerCount)
    x += 1

plt.axhline(0, color='r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()