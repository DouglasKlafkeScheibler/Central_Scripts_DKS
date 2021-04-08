from utils import tryGetFromString

#Função que pega as informações de "CUSTO DE DEFICIT" com identificador CD
def parseDeficit(content):
    filename = 'deficit.csv'
    header = [
        'curveIndex', 'subsystem',
        'curveName', 'stageIndex',
        'loadPctPat1', 'deficitCostPat1',
        'loadPctPat2', 'deficitCostPat2',
        'loadPctPat3', 'deficitCostPat3',
        'loadPctPat4', 'deficitCostPat4',
        'loadPctPat5', 'deficitCostPat5'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'CD' in line:
            patInfo = []

            for i in range(5):
                patInfo.append(tryGetFromString(
                    line, 29 + i*15, 34 + i*15, float))
                patInfo.append(tryGetFromString(
                    line, 34 + i*15, 44 + i*15, float))

            result.append([
                tryGetFromString(line, 4, 6, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 24),
                tryGetFromString(line, 24, 26, int),
                *patInfo
            ])

    return [(filename, header, result)]
