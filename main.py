try:
    number = float(input('Your number->> '))

    if number > 0:
        print('Your number is positive')
    elif number < 0:
        print('Your number is negative')
    elif number == 0:
        print('Your number is equal to Zero')
except ValueError as vl_er:
    print('Error!Wrong type of function,', vl_er)

