FileSize = float(input('The size of file in gigabytes->>'))
SpeedInBitForSec = float(input('The speed of the internet connection in bit/sec->>'))
SpeedInGbForSec = float(SpeedInBitForSec * 1.25 * 10 ** -10)
TimeInSec = (FileSize / SpeedInGbForSec)
action = input('action->>')

if action == 'hours':
