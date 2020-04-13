if __name__ == "__main__":
    sum
    min
    mnozh
    dil

def sum(*params):
    res = 0
    for item in params:
        res +=item
    return res

def min(*params):
    res = 0
    for item in params:
        res -=item
    return res

def mnozh(a, b):
    return a*b

def dil(a, b):
    return a/b