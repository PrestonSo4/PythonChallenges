def cipher():
    cipher = ''    
    text = input('Enter the text you want to cipher')
    key = int(input('Enter the key: '))
    if key > 26 or key < 1:
        print('The key is too big or small')
    for char in text:
        if char.isalpha():
            ascii = ord(char)
            if char.islower():
                start = 97
                end = 122
            if char.isupper():
                start = 65
                end = 90
            ascii -= key 
            if ascii < start:
                ascii += 26
            cipher += chr(ascii)
        else:
            cipher += char    
        
    return(cipher)
print(cipher())
def decipher():
    text = ''    
    cipher = input('Enter the text you want to decipher')
    key = int(input('Enter the key: '))
    if key > 26 or key < 1:
        print('The key is too big or small')
    for char in cipher:
        if char.isalpha():
            ascii = ord(char)
            if char.islower():
                start = 97
                end = 122
            if char.isupper():
                start = 65
                end = 90        
            ascii += key 
            if ascii > end:
                ascii -= 26
            text += chr(ascii)
        else:
            text += char
    return(text)
print(decipher())

