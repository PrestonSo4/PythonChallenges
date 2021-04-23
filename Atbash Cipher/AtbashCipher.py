def encrypt(text):
    text=text.upper()
    cText = ''
    for char in text:
        ascii = ord(char)
        if ascii >= 65 and ascii <= 90:
            position = ascii - 65
            position = 25 - position
            ascii = position + 65
            char = chr(ascii)
            cText += char
        else: 
            cText += char
    return cText

print(encrypt('This is a test'))
print(encrypt(''))
