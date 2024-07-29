import math

def divide(first, second):
    if second == 0:
        res = math.inf
    else:
        res = first//second

    return res

