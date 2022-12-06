try:
    a = int(input('begin->>'))
    b = int(input('end->>'))
    for i in reversed(range(a+1, b)):
        print(i, end='  ')
except ValueError as vl_er:
    print('Error!', vl_er)

