a = int(input('number->>'))
action = input('action->>')
if action == 'mi':
    print(a * 0.000621371196)
elif action == 'in':
    print(a * 39.37)
elif action == 'yd':
    print(a * 1.0936)
else:
    print("Action is not found")