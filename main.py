try:
    diameter = float(input('Diameter of the circle->>'))
    action = input('action->>')
    r = float(diameter / 2)

    if action == 'square':
        print(float(3.14 * (r ** 2)))
    elif action == 'perimeter':
        print(float(3.14 * diameter))
    else:
        print('Error!')
except ValueError:
    print('Error! Wrong type of function')


