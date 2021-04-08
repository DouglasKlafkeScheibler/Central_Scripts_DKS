from utils import tryGetFromString
import datetime 

#Função que pega as informações de "ENERGIA ARMAZENADA NOS REEs" do sumário
def storedEnergyREE(content):
    header = [
        'REE', 'number',
        'sis', 'inic',
        'sem_01', 'sem_02',
        'sem_03', 'sem_04',
        'sem_05', 'deck_date'
    ]
    result = []
    lines = content.splitlines()[1:]
    validy = False
    count = 0
    date = datetime.datetime.strptime(lines[3][98:109], "%d/%m/%Y").strftime("%Y-%m-%d")

    for line in lines:

        if 'ENERGIA ARMAZENADA NOS REEs' in line:
            validy = True

        if validy == True:
            if 'X-' in line:
                count = count + 1
            else:
                if count == 2:
                    inic = line[28:35].strip()
                    sem1 = line[36:42].strip()
                    sem2 = line[43:49].strip()
                    sem3 = line[50:56].strip()
                    sem4 = line[57:63].strip()
                    sem5 = line[64:70].strip()
                    result.append([
                        tryGetFromString(line, 4, 17),
                        tryGetFromString(line, 18, 22, int),
                        tryGetFromString(line, 23, 27, int),
                        tryGetFromString(line, 28, 35),
                        sem1,
                        sem2,
                        sem3,
                        sem4,
                        sem5,
                        date
                    ])
                elif count == 3:
                    break 

    newResult = []
    newResult2 = []

    for data in result:
        newResult.append([x if x != '' else None for x in data])
   
    for data in newResult:
        newResult2.append([x if x != '-' else None for x in data])

    if len(newResult2) == 0:
        newResult2 = [[None, None, None, None, None, None, None, None, None, date]]

    return [(header, newResult2)]