try:
    number = 0
    while True:
        number = int(input('number->'))
        if number == 7:
            break
        elif number > 0:
            print('number is positive')
        elif number < 0:
            print('number is negative')
        elif number == 0:
            print('number is equal to zero')
except ValueError as vl_er:
    print(vl_er)
