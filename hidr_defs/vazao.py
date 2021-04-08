import sys
from functools import partial
from datetime import datetime

FORMAT_VAZEDIT = 0

def main():

    file = 'VAZOES.DAT'
    outfile = 'vazoes.csv'
    
    yearStart = 1931
    stations = 320

    if len(sys.argv) > 1:
        yearStart = int(sys.argv[1])
        if len(sys.argv) > 2:
            stations = int(sys.argv[2])
            if len(sys.argv) > 3:
                file = sys.argv[3]
                if len(sys.argv) > 4:
                    outfile = sys.argv[4]
    
    try:
        data = readFile(file, stations)
        
        writeResults(data,outfile, yearStart)
    except FileNotFoundError:
        print('The supplied file: ' + file + " was not found.")

def verifyStation(stationData):
    
    for i in range(0,len(stationData)):
        if stationData[i] != 0:
            return True
            
    return False
    

def readFile(file, stations):

    data = []
    
    for i in range(0,stations):
        data.append([])
    
    year = 0
    currentStation = 0
    currentMonth = 0
    
    with open(file,'rb') as f:
        for measurement in iter(partial(f.read, 4), b''):
            
            data[currentStation].append(int.from_bytes(measurement, byteorder='little'))
            
            currentStation = currentStation + 1
            if currentStation == stations:
                currentStation = 0
                

    return data
    
def writeResultsVazedit(data, outfile, yearStart):
    fileData = ''

    a = datetime.now()
    for i in range(len(data)):
        if verifyStation(data[i]):
            stationdata = ''
            for year in range(0,len(data[i])//12):
                
                stationdata = stationdata + str(i+1).rjust(3) + str(year + yearStart).rjust(5) + ''.join((f'{x:02d}').rjust(6) for x in data[i][year*12:(year+1)*12]) + '\n'
                
            fileData = fileData + stationdata
                
    b = datetime.now()
    print(b-a)
    with open(outfile, 'w') as f:
        f.write(fileData)

def writeResults(data, outfile, yearStart, format = FORMAT_VAZEDIT):
    if format == FORMAT_VAZEDIT:
        writeResultsVazedit(data, outfile, yearStart)
        
main()
