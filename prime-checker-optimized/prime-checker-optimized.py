from math import sqrt
def findP(x):
    if x<=1: return False
    elif x == 2 or x == 3: return True
    elif x%2 == 0: return False
    elif x%3 == 0: return False
    else:
        i = 5
        while i<=int(sqrt(x)):
            if x%i == 0: return False
            i+=2
        return True
n = 2099
print(f"{n} is Prime") if findP(n) else print(f"{n} is Not Prime")