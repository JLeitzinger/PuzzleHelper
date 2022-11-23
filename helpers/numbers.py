from math import sqrt
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 73, 79, 83, 89, 97, 101]



def diffArray(arr):

    diffArray = []

    for i in range(0, len(arr)-1):
        diffArray.append(arr[i+1]-arr[i])

    return diffArray

def numToLetters(number):

    return chr(ord('@')+number)

def checkPrime(number):
    
    primeFlag = 0

    if(number > 1):
        for i in range(2, int(sqrt(number)) + 1):
            if (number % i == 0):
                primeFlag = 1
                break
        if (primeFlag == 0):
            return True
        else:
            return False
    else:
        return False

def checkArray(arr, check):
    if (check=='letters'):
        return [numToLetters(x) for x in arr]
    elif (check=='prime'):
        return [checkPrime(x) for x in arr]
    elif (check=='difference'):
        return diffArray(arr)
    else:
        print('No Valid Selection')
