a = int(input('begin->>'))
b = int(input('end->>'))

for item in range(a, b):
    if item % 2 != 0:
        print(item, end='  ')