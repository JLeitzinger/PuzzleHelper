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

