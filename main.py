try:
    number = int(input('number->>'))
    st = int(input('st->>'))
    if st < 0 or st > 7:
        raise Exception('St is less then 0 or more then 7')
    else:
        print(number ** st)

except ValueError as vl_er:
    print('Error,', vl_er)
except Exception as ex:
    print(f'Error:{ex}')
