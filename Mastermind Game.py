#Rules: 
#1) Guess 4 numbers correctly to win, individul number ranges from 0 to 9 inclusive
#2) Numbers in the four position could have duplicates as they are generated randomly
#3) The first hint tells you the amount of correct numbers in CORRECT POSITIONS but the exact numbers are not known
#4) The Second hint tells you the amount of correct numbers in WRONG POSITIONS
#5) Note, numbers in first and second hint does not overlap
#6) There are unlimited tries

import random

ans = ""
for i in range(4):
    ans += str(random.randint(0,9))
def misterMind():
    count = {}
    original_count = []
    reset = 0
    for ch in ans:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] += 1
    for num in count:
        original_count.append(count[num])
    guess = input("Please guess a four digit number!")
    result = checker(guess, ans, count)
    while not result:
        for num in count:
            count[num] = original_count[reset]
            reset += 1
        reset = 0
        guess = input("Please guess a four digit number!")
        result = checker(guess, ans, count)
    print(result)

def checker(guess, ans, count):
    A = 0
    B = 0
    if guess == ans:
        return "Congrats you win!"
    else:
        for i in range(len(guess)):
            if guess[i] == ans[i]:
                A += 1
                count[guess[i]] -= 1
        for k in range(len(guess)):
            if guess[k] in ans:
                if count[guess[k]] > 0:
                    B += 1
                    count[guess[k]] -= 1

        print("Correct Numbers in correct position " + str(A))
        print("Correct Numbers in wrong position " + str(B))

misterMind()
