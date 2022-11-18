try:
    FileSize = float(input('The size of file in gigabytes->>'))
    SpeedInBitForSec = float(input('The speed of the internet connection in bit/sec->>'))
    SpeedInGbForSec = float(SpeedInBitForSec * 1.25 * 10 ** -10)
    TimeInSec = (FileSize / SpeedInGbForSec)
    action = input('action->>')

    if action == 'hours':
        print(f'Remain {int(TimeInSec / 3600)} hours till download')
    elif action == 'minutes':
        print(f'Remain {int(TimeInSec / 60)} minutes till download')
    elif action == 'seconds':
        print(f'Remain {int(TimeInSec)} seconds till download')
    else:
        h = int(TimeInSec / 3600)
        m = int((TimeInSec % 3600) / 60)
        s = int((TimeInSec % 3600) % 60)
        print(f'Remain {h}:{m}:{s} till download')

except ValueError as vl_er:
    print('Error! Wrong type of function,', vl_er)

