#https://www.101computing.net/blackbeards-treasure-map/
answer = 1889121
for rows in range(2440, 2470):
    for columns in range(750, 770):
        product = rows * columns
        if product == answer:
            print('x:', rows, 'y:', columns)
            break
