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

if __name__ == '__main__':
    c = input('Y/N\n').upper()
    while c == 'Y':
        decrypt()
        c = input('Y/N\n').upper()