try:
    a = int(input('begin->>'))
    b = int(input('end->>'))
    counter = int(0)
    if a and b == 0:
        raise Exception
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




