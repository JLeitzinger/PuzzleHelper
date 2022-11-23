import string

def alphaArr(arr):
    return arr.sort()

def alphaMiss(arr):
    arrSet = set([x.lower() for x in arr])
    alpha = set([x for x in string.ascii_lowercase])
    return alpha - arrSet