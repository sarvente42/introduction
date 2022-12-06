try:
    a = int(input('begin->>'))
    b = int(input('end->>'))
    counter = int(0)
    if a == 0 and b == 0:
        raise Exception('Both of numbers equals Zero')
    for i in reversed(range(a, b)):
        print(i, end='\t')
    for i in range(a, b):
        print(i, end='\t')
    for i in range(a, b):
        if i % 7 == 0:
            print(i, end='\t')
    for i in range(a, b):
        if i % 5 == 0:
            counter = counter + 1
    print(counter)

except ValueError as vl_er:
    print('Error!', vl_er)
except Exception as ex:
    print('Error!', ex)
    print(f'Name: {ex.__class__.__name__}')




