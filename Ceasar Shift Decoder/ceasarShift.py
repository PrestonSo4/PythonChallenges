#https://www.101computing.net/caesar-shift-decoder/
def decrypt():
    cipher = input("Enter the text: ").upper()
    for i in range(25):
        print('Key', str(i), 'A =', str(65+i),'\n')
        text = ''
        for char in cipher:
            ascii = ord(char)
            if ascii >= 65 and ascii <= 90:
                ascii += i
                if ascii > 90:
                    ascii -= 26
            text += chr(ascii)
        print(text,'\n')

## Trying to make a ceasar shift encoder

def encrypt():
    text = input('Enter plain text: ')
    cipher = ''
    while True:
        try:
            key = int(input('Enter the key: '))
            if key >  26 or key < 1:
                print('That is to big or too small of a key.')
            else:
                break
        except:
            print('That is an invalid key, Try again!')
    for char in text:
        start = 97 if char.islower() else 65
        end = 122 if char.islower () else 90
        ascii = ord(char)
        ascii -= key
        if ascii < start:
            ascii += 26
        cipher += chr(ascii)
    print(cipher)

if __name__ == '__main__':
    
    while True:
        c = input('D/E/Q\n').upper()
        if c == 'D':
            decrypt()
        elif c == 'E':
            encrypt()
        else:
            break