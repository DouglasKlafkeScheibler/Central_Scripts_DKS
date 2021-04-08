from utils import tryGetFromString
import datetime 

#Função que pega as informações de "PEQUENAS USINAS" do sumário
def smallPlants(content):
    header = [
        'usina', 'sem_01', 
        'sem_02', 'sem_03',
        'sem_04', 'sem_05', 
        'pat', 'deck_date'
    ]
    lines = content.splitlines()[1:]
    validy = False
    count = 0
    date = datetime.datetime.strptime(lines[3][98:109], "%d/%m/%Y").strftime("%Y-%m-%d")    
    result = []

    for line in lines:

        if 'PEQUENAS USINAS : DESPACHO NO PATAMAR 1 (MWmed)' in line:
            validy = True

        if validy == True:
            if 'X-' in line:
                count = count + 1
            else:
                if count == 2:
                    result.append([
                        tryGetFromString(line, 4, 16),
                        tryGetFromString(line, 17, 24, float),
                        tryGetFromString(line, 25, 32, float),
                        tryGetFromString(line, 33, 40, float),
                        tryGetFromString(line, 41, 48, float),
                        tryGetFromString(line, 49, 56, float),
                        1,
                        date
                    ])

                elif count == 5:
                    result.append([
                        tryGetFromString(line, 4, 16),
                        tryGetFromString(line, 17, 24, float),
                        tryGetFromString(line, 25, 32, float),
                        tryGetFromString(line, 33, 40, float),
                        tryGetFromString(line, 41, 48, float),
                        tryGetFromString(line, 49, 56, float),
                        2,
                        date
                    ])    

                elif count == 8:
                    result.append([
                        tryGetFromString(line, 4, 16),
                        tryGetFromString(line, 17, 24, float),
                        tryGetFromString(line, 25, 32, float),
                        tryGetFromString(line, 33, 40, float),
                        tryGetFromString(line, 41, 48, float),
                        tryGetFromString(line, 49, 56, float),
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
                tryGetFromString(line, 4, 16),
                tryGetFromString(line, 17, 24, float),
                tryGetFromString(line, 25, 32, float),
                tryGetFromString(line, 33, 40, float),
                tryGetFromString(line, 41, 48, float),
                tryGetFromString(line, 49, 56, float),
                pat,
                date
                ])
    return result