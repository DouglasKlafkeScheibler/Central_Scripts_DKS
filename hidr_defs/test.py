import sys
from functools import partial
from datetime import datetime

file = 'MLT.DAT'

with open(file,'rb') as f:

    for measurement in iter(partial(f.read, 4), b''):
        print(int.from_bytes(measurement, byteorder='little'))


        # for measurement in iter(partial(f.read, 4), b''):
            
        #     data[currentStation].append(int.from_bytes(measurement, byteorder='little'))
            
        #     currentStation = currentStation + 1
        #     if currentStation == stations:
        #         currentStation = 0