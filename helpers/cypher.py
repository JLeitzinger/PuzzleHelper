
def rot13(letter):
    numL = ord(letter.lower())
    if (letter==' '):
        return ' '
    elif (numL < 110):
        return chr(numL+13)
    else:
        return chr(numL-13)