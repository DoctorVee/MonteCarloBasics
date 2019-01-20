# Now, just to test our dice, let's roll the dice 100 times.
import random

def rollDice():
    roll = random.randint(1,100)
    return roll

x = 0
win = 0
lose = 0
while x < 10000:
    result = rollDice()
#    print(result)
    if result==100:
        lose +=1
    elif result<51:
        lose +=1
    else:
        win +=1
    x+=1

print("Out of 10000 tries, ")
print(win, " wins")
print(lose, "losses")