try:
    hours = int(input('Hours->>'))

    if hours < 0:
        raise Exception('Hours are less than Zero')
    elif hours > 24:
        raise Exception('Hours are more than Twenty Four')
 #я не знаю чому тут не правильно працюють raise-и

    elif 0 <= hours < 6:
        print('Good Night')
    elif 6 <= hours < 13:
        print('Good Morning')
    elif 13 <= hours < 17:
        print('Good Day')
    elif 17 <= hours <= 23:
        print('Good Evening')

except ValueError as vl_er:
    print('Error! Wrong type of function,', vl_er)



