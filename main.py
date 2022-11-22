try:
    number = int(input('Your number->>'))
    if number < 0 or number > 100:
        raise Exception('Your number is less then 0 or more then 100')
    elif number % 3 == 0 and number / 5 != 3:
        print('Fizz')
    elif number % 5 == 0 and number / 3 != 5:
        print('Buzz')
    elif number % 3 == 0 and number % 5 == 0:
        print('Fizz Buzz')
    elif number % 5 != 0 and number % 3 != 0:

        print(number)
except ValueError as vl_er:
    print('Error,', vl_er)
except Exception as ex:
    print(f'Error:{ex}')
