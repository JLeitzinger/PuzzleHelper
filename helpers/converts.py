import csv 

def treatAsASCII(character):
    return chr(character)

def csvToDict(filename):
    with open(filename) as f:
        fileData = csv.reader(f)
        headers = next(fileData)
        return [dict(zip(headers, i)) for i in fileData]

def genPluDict():
    return csvToDict('./lookups/plu_codes.csv')



arr2 = "79 110 101 111 117 103 104 116 111 98 116 97 105 110 111 110 101 111 104"

arr2 = arr2.split(' ')