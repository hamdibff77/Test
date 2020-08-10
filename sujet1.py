def Majus(data):
    result = ''
    for char in data:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    return result