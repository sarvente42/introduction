try:
    a = int(input('begin->>'))
    b = int(input('end->>'))

    for i in range(a, b):
        if i % 7 == 0:
            print(i, end='  ')

except ValueError as vl_er:
    print('Error!', vl_er)

