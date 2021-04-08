from utils import tryGetFromString

#Função que pega as informações de "NUMERO DE SEMANAS" com identificador GS
def parseIntervalMonth(content):
    filename = 'intervalMonth.csv'
    header = [
        'month', 'week'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'GS' in line:
            patInfo = []

            
            result.append([
                tryGetFromString(line, 4, 6, int),
                tryGetFromString(line, 9, 10, int)
            ])

    return [(filename, header, result)]