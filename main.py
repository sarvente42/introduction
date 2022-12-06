try:
    a = int(input('begin->>'))
    b = int(input('end->>'))

    for item in range(a, b):
       if item % 2 != 0:
          print(item, end='  ')
except ValueError as vl_er:
    print('Error!', vl_er)
