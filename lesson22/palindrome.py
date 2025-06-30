
def palindrome(r):
    e = len(r)-1

    s = 0
    while s<e:
        if r[s] != r[e]:
            return False
        s+=1
        e-=1

    return True

r = (7,8,8,8,7,9)

if (palindrome(r)):
    print("the tuple is a flip flop")

else:
    print("the tuple is not a flip flop")
