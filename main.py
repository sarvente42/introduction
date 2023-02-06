try:
    begin = int(input())
    end = int(input())
    function = input()
    sum = 0
    counter = 0
    if function == 'even numbers':
        for i in range(begin, end+1):
            if i % 2 == 0:
                sum += i
                counter += 1
        print(sum)
        print(sum / counter)
    if function == 'buzz numbers':
        for i in range(begin, end+1):
            if i % 2 != 0:
                sum += i
                counter += 1
        print(sum)
        print(sum / counter)
    if function == 'multiple of 9':
        for i in range(begin, end+1):
            if i % 9 == 0:
                sum += i
                counter += 1
        print(sum)
        print(sum / counter)

except ArithmeticError as ar_vl:
    print(f'Error', ar_vl)
except ValueError as vl_er:
    print(vl_er)
