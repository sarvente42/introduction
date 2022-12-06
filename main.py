try:
    a = int(input('begin->>'))
    b = int(input('end->>'))
    if a > b:
        a, b = b, a

    for i in range(a, b):
        if i % 2 != 0:
            print(i, end='  ')
except ValueError as vl_er:
    print('Error!', vl_er)