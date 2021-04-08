from utils import tryGetFromString
import datetime    
    
#Função que pega as informações de "GERACAO TERMICA" do sumário
def thermalGeneration(content):
    header = [
        'number', 'bb',
        'sem_01', 'sem_02',
        'sem_03', 'sem_04', 
        'sem_05', 'pat',
        'deck_date'
    ]
    lines = content.splitlines()[1:]
    validy = False
    count = 0
    date = datetime.datetime.strptime(lines[3][98:109], "%d/%m/%Y").strftime("%Y-%m-%d")
    result = []

    for line in lines:

        if 'GERACAO TERMICA (MWmed) PARA O PATAMAR 1' in line:
            validy = True

        if validy == True:
            if 'X-' in line:
                count = count + 1
            else:
                if count == 2:
                    result.append([
                        tryGetFromString(line, 4, 8, int),
                        tryGetFromString(line, 9, 21),
                        tryGetFromString(line, 22, 29, float),
                        tryGetFromString(line, 30, 37, float),
                        tryGetFromString(line, 38, 45, float),
                        tryGetFromString(line, 46, 53, float),
                        tryGetFromString(line, 54, 61, float),
                        1,
                        date
                    ])

                elif count == 5:
                    result.append([
                        tryGetFromString(line, 4, 8, int),
                        tryGetFromString(line, 9, 21),
                        tryGetFromString(line, 22, 29, float),
                        tryGetFromString(line, 30, 37, float),
                        tryGetFromString(line, 38, 45, float),
                        tryGetFromString(line, 46, 53, float),
                        tryGetFromString(line, 54, 61, float),
                        2,
                    date
                ]) 

                elif count == 8:
                    result.append([
                        tryGetFromString(line, 4, 8, int),
                        tryGetFromString(line, 9, 21),
                        tryGetFromString(line, 22, 29, float),
                        tryGetFromString(line, 30, 37, float),
                        tryGetFromString(line, 38, 45, float),
                        tryGetFromString(line, 46, 53, float),
                        tryGetFromString(line, 54, 61, float),
                        3,
                    date
                ])

                elif count == 9:
                    break

    newResult = []

    for data in result:
        newResult.append([x if x != '' else None for x in data])
    
    return [(header, newResult)]



def getInfo(line, pat, date):
    result.append([
                tryGetFromString(line, 4, 8, int),
                tryGetFromString(line, 9, 21),
                tryGetFromString(line, 22, 29, float),
                tryGetFromString(line, 30, 37, float),
                tryGetFromString(line, 38, 45, float),
                tryGetFromString(line, 46, 53, float),
                tryGetFromString(line, 54, 61, float),
                pat,
                date
                ])
    return result