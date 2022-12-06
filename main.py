a = int(input('begin->>'))
b = int(input('end->>'))

for i in range(a+1, b):
    if i % 3 == 0:
        print('fizz', end=' ')
    if i % 5 == 0:
        print('buzz', end='')
    print()

