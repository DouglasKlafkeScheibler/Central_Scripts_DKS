from utils import tryGetFromString
import datetime    

#Função que pega as informações de "DEMANDA BRUTA POR SUBSISTEMA E POR PATAMAR" do sumário
def grossDemand(content):
    header = [
        'ssis', 'sem_01',
        'sem_02', 'sem_03',
        'sem_04', 'sem_05',
        'deck_date'
    ]
    result = []
    lines = content.splitlines()[1:]
    validy = False
    count = 0
    date = datetime.datetime.strptime(lines[3][98:109], "%d/%m/%Y").strftime("%Y-%m-%d")
    
    for line in lines:
        
        if 'DEMANDA BRUTA (MWmed) POR SUBSISTEMA E POR PATAMAR' in line:
            validy = True

        if validy == True:
            if 'X-' in line:
                count = count + 1
            else:
                if count == 2:
                    result.append([
                        tryGetFromString(line, 4, 10),
                        tryGetFromString(line, 11, 21, float),
                        tryGetFromString(line, 22, 32, float),
                        tryGetFromString(line, 33, 43, float),
                        tryGetFromString(line, 44, 54, float),
                        tryGetFromString(line, 55, 65, float),
                        date
                    ])
                elif count == 3:
                    break      

    newResult = []

    for data in result:
        newResult.append([x if x != '' else None for x in data])
    
    return [(header, newResult)]