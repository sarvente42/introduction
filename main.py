try:
    a = int(input('length->>'))
    b = input('sign->>')
    if a == 0 and b == 0:
        raise Exception("Both numbers equals Zero")
    for i in range(0, a):
        print(b, end='\n')

except ValueError as vl_er:
    print('Error!', vl_er)
except Exception as ex:
    print('Error!', ex)
