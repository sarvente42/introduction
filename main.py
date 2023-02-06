try:
    begin = int(input())
    end = int(input())
    function = input()
    sum = 0
    counter = 0
    for i in range(begin, end+1):
        if function == 'even numbers':
            if i % 2 == 0:
                sum += i
                counter += 1
                print(sum)
                avg = sum / counter
                print(avg)
        elif function == 'buzz numbers':
            if i % 2 != 0:
                sum += i
                print(sum)
                counter += 1
                print(sum)
                avg = sum / counter
        elif function == 'multiple of 9':
            if i % 9 == 0:
                sum += i
                print(sum)
                counter += 1
                print(sum)
                avg = sum / counter


except ArithmeticError as ar_vl:
    print(f'Error', ar_vl)