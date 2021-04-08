from utils import tryGetFromString

#Função que pega as informações de "LIMITES DE INTERC�MBIO ENTRE SUBSISTEMAS" com identificador IA
def parseExchangeLimits(content):
    filename = 'exchangelimit.csv'
    header = [
        'stageIndex', 'fromSubsystem', 'toSubsystem', 'usePenalty',
        'limitFromToPat1', 'limitToFromPat1',
        'limitFromToPat2', 'limitToFromPat2',
        'limitFromToPat3', 'limitToFromPat3',
        'limitFromToPat4', 'limitToFromPat4',
        'limitFromToPat5', 'limitToFromPat5',
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'IA' in line:
            patInfo = []

            for i in range(5):
                patInfo.append(tryGetFromString(
                    line, 19 + i*20, 29 + i*20, float))
                patInfo.append(tryGetFromString(
                    line, 29 + i*20, 39 + i*20, float))

            result.append([
                tryGetFromString(line, 4, 6, int),
                tryGetFromString(line, 9, 11),
                tryGetFromString(line, 14, 16),
                tryGetFromString(line, 17, 18, int, 0),
                *patInfo
            ])

    return [(filename, header, result)]