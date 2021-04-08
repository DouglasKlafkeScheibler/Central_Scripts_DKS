from utils import tryGetFromString

#Função que pega as informações de "CARGA DOS SUBSISTEMAS" com identificador DP
def parseSystemLoad(content):
    filename = 'load.csv'
    header = [
        'stageIndex', 'subsystem',
        'loadPat1', 'durationPat1',
        'loadPat2', 'durationPat2',
        'loadPat3', 'durationPat3',
        'loadPat4', 'durationPat4',
        'loadPat5', 'durationPat5'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'DP' in line:
            patInfo = []

            for i in range(5):
                patInfo.append(tryGetFromString(
                    line, 19 + i*20, 29 + i*20, float))
                patInfo.append(tryGetFromString(
                    line, 29 + i*20, 39 + i*20, float))

            result.append([
                tryGetFromString(line, 4, 6, int),
                tryGetFromString(line, 9, 11, int),
                *patInfo
            ])

    return [(filename, header, result)]
