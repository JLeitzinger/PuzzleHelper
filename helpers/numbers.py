
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 73, 79, 83, 89, 97, 101]



def diffArray(arr):

    diffArray = []

    for i in range(0, len(arr)-1):
        diffArray.append(arr[i+1]-arr[i])

    return diffArray

def numToLetters(arr):

    return [chr(ord('@')+x) for x in arr]

