
def misterMind(ans):
    ans = str(ans)
    count = {}
    for num in ans:
        if num not in count:
            count[num] = 1
        else:
            count[num] +=1
    guess = input("Please guess!")
    result = checker(guess, ans, count)
    if result:
        print(result)
    else:
        misterMind(ans)
def checker(guess, ans, count):
    A = 0
    B = 0
    if guess == ans:
        return "Congrats you win!"
    else:
        for i in range(len(guess)):
            if guess[i] == ans[i]:
                A+=1
                count[guess[i]] -= 1
        for k in range(len(guess)):
            if guess[k] in ans:
                if count[guess[k]]>0:
                    B += 1
                    count[guess[k]] -= 1
        print(A)
        print(B)