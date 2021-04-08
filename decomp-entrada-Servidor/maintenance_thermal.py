from utils import tryGetFromString

#Função que pega as informações de "MANUTENCAO PROGRAMADA DE USINAS TERMICAS" com identificador MT
def parseMaintenanceThermal(content):
    filename = 'maintthermal.csv'
    header = ['thermalId', 'subsystem']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'MT' in line:

            patInfo = []
            stageId = 0
            lastInfo = 0

            while lastInfo != -1:
                lastInfo = tryGetFromString(
                    line, 14 + stageId*5, 19 + stageId*5, float, -1)

                if lastInfo == -1:
                    break

                patInfo.append(lastInfo)

                stageId = stageId + 1

            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                *patInfo
            ])

    if len(result) != 0:
        for i in range(len(result[0])-2):
            header.append('maintFactorStage{}'.format(i+1))

    return [(filename, header, result)]

