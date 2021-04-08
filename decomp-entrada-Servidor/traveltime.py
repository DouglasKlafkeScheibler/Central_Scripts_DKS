from utils import tryGetFromString

#Função que pega as informações de "TEMPO DE VIAGEM DA AGUA" com identificador VI
def parseTravelTime(content):
    filename = 'traveltime.csv'
    header = ['hydroId', 'travelTime',
            'outflowPastStage1', 'outflowPastStage2',
            'outflowPastStage3', 'outflowPastStage4',
            'outflowPastStage5', 'outflowPastStage6']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'VI' in line[:2]:

            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 12),
                tryGetFromString(line, 14, 19, float),
                tryGetFromString(line, 20, 24, float),
                tryGetFromString(line, 25, 29, float),
                tryGetFromString(line, 30, 34, float),
                tryGetFromString(line, 35, 39, float),
                tryGetFromString(line, 40, 44, float)
            ])

    return [(filename, header, result)]
