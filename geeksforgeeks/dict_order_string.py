from collections import OrderedDict

def checkOrder(input, pattern):
    dict = OrderedDict.fromkeys(input)

    ptrlen = 0
    for key,value in dict.items():
        if (key == pattern[ptrlen]):
            ptrlen += 1
        if (ptrlen == (len(pattern))):
            return True
    return False

input = 'engineers rock'
pattern = 'er'
print(checkOrder(input, pattern))