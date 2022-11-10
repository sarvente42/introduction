a = int(input('number 1->>'))
b = int(input('number 2->>'))
c = int(input('number 3->>'))
action = input('action->>')
if action == 'max':
    if a > b and a > c:
        print(f'{a} is max')
    elif b > a and b > c:
        print(f'{b} is max')
    elif c > a and c > b:
        print(f'{c} is max')

elif action == 'min':
    if a < b and a < c:
        print(f'{a} is min')
    elif b < a and b < c:
        print(f'{b} is min')
    elif c < a and c < b:
        print(f'{c} is min')

elif action == 'avg':
    print((a + b + c)/3)
elif a == b == c:
    print('All numbers are equal')
else:
    print('The action is not found')