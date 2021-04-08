from utils import tryGetFromString
import datetime

#Função que pega as informações de "ENERGIA ARMAZENADA NOS SUBSISTEMAS" do sumário
def storedEnergySubsytem(content):
    header = [
        'subsystem', 'number',
        'inic', 'sem_01',
        'sem_02', 'sem_03',
        'sem_04', 'sem_05',
        'sem_06', 'deck_date'
    ]
    result = []
    lines = content.splitlines()[1:]
    validy = False
    count = 0
    date = datetime.datetime.strptime(lines[3][98:109], "%d/%m/%Y").strftime("%Y-%m-%d")

    for line in lines:

        if 'ENERGIA ARMAZENADA NOS SUBSISTEMAS' in line:
            validy = True

        if validy == True:
            if 'X-' in line:
                count = count + 1
            else:
                if count == 2:
                    sem1 = line[30:36].strip()
                    sem2 = line[37:43].strip()
                    sem3 = line[44:50].strip()
                    sem4 = line[51:57].strip()
                    sem5 = line[58:64].strip()
                    sem6 = line[65:71].strip()
                    result.append([
                        tryGetFromString(line, 4, 16),
                        tryGetFromString(line, 17, 21),
                        tryGetFromString(line, 22, 29),
                        sem1,
                        sem2,
                        sem3,
                        sem4,
                        sem5,
                        sem6,
                        date
                    ])
                elif count == 3:
                    break      

    newResult = []

    for data in result:
        newResult.append([x if x != '' else None for x in data])

    if len(newResult) == 0:
        newResult = [[None, None, None, None, None, None, None, None, None, date]]
        
    return [(header, newResult)]