try:
    managerA = int(input('First manager sells->'))
    managerB = int(input('Second manager sells->'))
    managerC = int(input('Third manager sells->'))
    if managerA or managerB or managerC <= 500:
       a = int(managerA or managerB or managerC * 0.03)
    elif managerA or managerB or managerC >= 501 and managerA or managerB or managerC <= 1000:
       b = int(managerA or managerB or managerC * 0.05)
    elif managerA or managerB or managerC >= 1001:
       c = int(managerA or managerB or managerC * 0.08)
    salaryA = managerA + 200 + a or b or c
    salaryB = managerB + 200 + a or b or c
    salaryC = managerC + 200 + a or b or c
    print(f'First manager salary: {salaryA}')
    print(f'Second manager salary: {salaryB}')
    print(f'Third manager salary: {salaryC}')
    max_sum = max(salaryA, salaryB, salaryC)
    print(f'The best manager salary: {max_sum + 200}!!!')
except ValueError as vl_er:
    print(f'Error!, {vl_er}')

