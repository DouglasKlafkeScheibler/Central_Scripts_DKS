from utils import tryGetFromString
import datetime    
    
#Função que pega as informações de "CUSTO MARGINAL DE OPERACAO" do sumário
def marginalCost(content):
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
        if 'CUSTO MARGINAL DE OPERACAO' in line:
            validy = True

        if validy == True:
            if 'X-' in line:
                count = count + 1
            else:
                if count == 2:
                    sem1 = line[11:21].strip()
                    sem2 = line[22:32].strip()
                    sem3 = line[33:43].strip()
                    sem4 = line[44:54].strip()
                    sem5 = line[55:65].strip()
                    result.append([
                        tryGetFromString(line, 4, 10),
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

    #Logic for Pat with Region
    i = 3
    for trash in range(5):
        ssis = newResult[i][0][3:]
        for c in range(3):
            elementOne = newResult[i - c - 1][0] + ssis            
            newResult[i - c - 1][0] = elementOne
        i += 4
    
    return [(header, newResult)]