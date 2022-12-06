try:
    a = int(input('begin->>'))
    b = int(input('end->>'))

    for item in range(a,  b):
        print(item, end='  ')
except ValueError as vl_er:
    print('Error!', vl_er)