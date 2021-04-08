from utils import tryGetFromString
import datetime    

#Função que pega as informações de "FLUXO NOS INTERCAMBIOS" do sumário
def exchangeFlow(content):
    header = [
        'interc', 'pat',
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

        if 'FLUXO NOS INTERCAMBIOS' in line:
            validy = True

        if validy == True:
            if 'X-' in line:
                count = count + 1
            else:
                if count == 2:
                    sem1 = line[18:28].strip()
                    sem2 = line[29:39].strip()
                    sem3 = line[40:50].strip()
                    sem4 = line[51:61].strip()
                    sem5 = line[62:73].strip()
                    result.append([
                        tryGetFromString(line, 4, 10),
                        tryGetFromString(line, 11, 17),
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

    for data in result:
        newResult.append([x if x != '' else None for x in data])
    
    return [(header, newResult)]