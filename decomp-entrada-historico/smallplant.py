from utils import tryGetFromString

#Função que pega as informações de "GERACAO EM PEQUENAS USINAS" com identificador PQ
def parseSmallPlant(content):
    filename = 'smallplant.csv'
    header = [
        'plantName', 'subsystem', 'stageIndex',
        'genPat1', 'genPat2', 'genPat3',
        'gravityCenterLoss',
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'PQ' in line:
            patInfo = []

            for i in range(3):
                patInfo.append(tryGetFromString(
                    line, 24 + i*5, 29 + i*5, float))

            result.append([
                tryGetFromString(line, 4, 14),
                tryGetFromString(line, 14, 16, int),
                tryGetFromString(line, 19, 21, int),
                *patInfo,
                tryGetFromString(line, 39, 44, float),
            ])

    return [(filename, header, result)]
