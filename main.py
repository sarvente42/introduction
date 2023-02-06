managerA = int(input('First manager sells->'))
managerB = int(input('Second manager sells->'))
managerC = int(input('Third manager sells->'))
if managerA or managerB or managerC <= 500:
    a = managerA or managerB or managerC * 0.03
elif managerA or managerB or managerC >=501 and managerA or managerB or managerC <= 1000:
    b = managerA or managerB or managerC * 0.05
elif managerA or managerB or managerC >= 1001:
    c = managerA or managerB or managerC * 0.08