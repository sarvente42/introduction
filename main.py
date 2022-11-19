try:
    number1 = float(input('First number->> '))
    number2 = float(input('Second number->>'))

    if number1 > number2:
        print(number2, number1)
    elif number2 > number1:
        print(number1, number2)
    else:
        print('First and second numbers are equal')
except ValueError as vl_er:
    print('Error! Wrong type of function,', vl_er)
