try:
    a = int(input('seconds->>'))
    b = 24 *3600
    if b < a:
        raise Exception('All seconds per day is less then user seconds')
    c = b - a

    action = input('action->>')
    if action == 'hours':
        print(f'Hours to midnight = {int(c/3600)} h')
    elif action == 'minutes':
        print(f'Minutes to midnight = {int(c/60)} m')
    elif action == 'seconds':
        print(f'Seconds to midnight = {c} s')
    else:
        h = int(c / 3600)
        m = int((c % 3600) / 60)
        s = int((c % 3600) % 60)
        print(f'{h}:{m:}{s} to midnight')

except ValueError as vl_ex:
    print(f'Value error:{vl_ex}')
except Exception as ex:
    print(f'Error:{ex}')
    print(f'Name:{ex.__class__.__name__}')

