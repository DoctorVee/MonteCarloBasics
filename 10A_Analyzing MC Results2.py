# This version lightly rewritten for more logical flow.
# Also added third option - profit, bust, and now loss (didn't make money but didn't bust either)

# So now that we've compared the life expectency of these strategies,
# we should also compare profits. First we can just compare profit vs loss,
# but also degree of profits is important.
# Both strategies stand to lose equal amounts, but this is not the case for gains.
# It is clear that our doublor bettor, despite having lower life expectancy,
# has far more upside compared to the simple bettor.

# Your results may vary slightly, but they should be something like:
#
# ('Simple Bettor Bust Chances:', 0.0)
# ('Doubler Bettor Bust Chances:', 31.269999999999996)
# ('Simple Bettor Profit Chances:', 38.32)
# ('Doubler Bettor Profit Chances:', 63.190000000000005)

import random
import matplotlib
import matplotlib.pyplot as plt
import time

sampleSize = 100
startingFunds = 10000
wagerSize = 100
wagerCount = 100


def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    else:                   # Was elif 100 > roll >= 50:
        return True


def doubler_bettor(funds, initial_wager, wager_count, color):
    global doubler_busts
    #####################
    global doubler_profits
    global doubler_losses
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
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                if value < 0:
                    currentWager += wager_count +1
#                    doubler_busts += 1
        elif previousWager == 'loss':
            wager = previousWagerAmount * 2     # Appeared in both parts of rollDice  if-else
            if (value - wager) < 0:             # Appeared in both parts of rollDice  if-else
                wager = value                   # Appeared in both parts of rollDice  if-else
            if rollDice():
                value += wager
                previousWager = 'win'
                wager = initial_wager
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager

                if value <= 0:
                    currentWager += wager_count +1
#                    doubler_busts += 1

        currentWager += 1
        wX.append(currentWager)         # This line used to appear 4 times.
        vY.append(value)                # This line used to appear 4 times.
    plt.plot(wX, vY, color)
    #####################
    if value > funds:
        doubler_profits += 1            # Ended up with more than we started.
    elif value == 0:
        doubler_busts += 1              # Ended up going broke.
    else:
        doubler_losses += 1               # Lost money but not all of it.

'''
Simple bettor, betting the same amount each time.
'''

def simple_bettor(funds, initial_wager, wager_count, color):
    global simple_busts
    #####################
    global simple_profits
    global simple_losses

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager
            if value <= 0:
                currentWager += wager_count +1
#                simple_busts += 1
        currentWager += 1
        wX.append(currentWager)
        vY.append(value)

    plt.plot(wX, vY, color)
    #####################
    if value > funds:
        simple_profits += 1
    elif value == 0:
        simple_busts += 1
    else:
        simple_losses += 1


x = 0

simple_busts = 0.0
simple_profits = 0.0
simple_losses = 0.0
#####################

doubler_profits = 0.0
doubler_busts = 0.0
doubler_losses = 0.0

while x < sampleSize:
    simple_bettor(startingFunds, wagerSize, wagerCount, 'c')
    # simple_bettor(startingFunds,wagerSize*2,wagerCount,'c')
    doubler_bettor(startingFunds, wagerSize, wagerCount, 'k')
    x += 1

print(('Simple Bettor Profit Chances:', (simple_profits / sampleSize) * 100.00))
print(('Simple Bettor Losses Chances:', (simple_losses / sampleSize) * 100.00))
print(('Simple Bettor Bust Chances:', (simple_busts / sampleSize) * 100.00))

print(('Doubler Bettor Profit Chances:', (doubler_profits / sampleSize) * 100.00))
print(('Doubler Bettor Losses Chances:', (doubler_losses / sampleSize) * 100.00))
print(('Doubler Bettor Bust Chances:', (doubler_busts / sampleSize) * 100.00))

plt.axhline(0, color='r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()