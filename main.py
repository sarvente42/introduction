try:
    number = 0
    sum_ = 0
    min_ = 0
    max_ = 0
    trigger = True
    while True:
        number = int(input('number->'))
        if number == 7:
            break
        else:
            sum_ += number
            if trigger:
                min_ = max_ = number
                trigger = False
            else:
                if max_ < number:
                    max_ = number
                if min_ > number:
                    min_ = number
    print(f'Sum = {sum_}')
    print(f'Min = {min_}')
    print(f'Max = {max_}')
except ValueError as vl_er:
    print(vl_er)
