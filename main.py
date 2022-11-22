try:
    TimeOfConvHours = int(input('All time of conversations h->>'))
    TimeOfConvMin = int(input('All time of conversations m->>'))
    TimeOfConvSec = int(input('All time of conversations s->>'))
    if TimeOfConvMin > 60:
        raise Exception('All time of conversations in Minutes is more then 60')
    elif TimeOfConvSec > 60:
        raise Exception('All time of conversations in Seconds is more then 60')
    a = TimeOfConvHours * 3600
    b = TimeOfConvMin * 60
    TimeOfConvInSec = a + b + TimeOfConvSec
    Kyivstar = 1.5
    LifeCell = 2.8
    Vodafone = 3.6
    action = input('Cell operators->>')
    if action == 'Kyivstar':
        print(TimeOfConvInSec * (Kyivstar / 60))
    elif action == 'LifeCell':
        print(TimeOfConvInSec * (LifeCell / 60))
    elif action == 'Vodafone':
        print(TimeOfConvInSec * (Vodafone / 60))

except ValueError as vl_er:
    print('Error,', vl_er)
except Exception as ex:
    print('Error,', ex)
