try:
    number = int(input('The number of the week->>'))

    if number == 1:
        print('Monday')
    elif number == 2:
        print('Tuesday')
    elif number == 3:
        print('Wednesday')
    elif number == 4:
        print('Thursday')
    elif number == 5:
        print('Friday')
    elif number == 6:
        print('Saturday')
    elif number == 7:
        print('Sunday')
    elif number > 7:
        raise Exception('There is no higher number than Seven in number of week')

except ValueError as vl_er:
    print('Error! Wrong Type of function,', vl_er)
except Exception as ex:
    print('Error!', ex)