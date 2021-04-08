from utils import tryGetFromString

#Função que pega as informações de "VOLUME DOS RESERVATORIOS" com identificador UH
def parseReservoirVolume(content):
    filename = 'reservoir.csv'
    header = ['hydroId', 'ree', 'initialVolume', 'minOutflow', 'hasEvaporation',
              'opStart', 'initialBaseVolume', 'superiorPouringLimit', 'hydroBalanceEachStage']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'UH' in line:
            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 24, float, 0.0),
                tryGetFromString(line, 24, 34, float),
                tryGetFromString(line, 39, 40, int, 0),
                tryGetFromString(line, 44, 46, int, 1),
                tryGetFromString(line, 49, 59, float, 0.0),
                tryGetFromString(line, 59, 69, float, 1e21),
                tryGetFromString(line, 69, 70, int, 0)

            ])
    return [(filename, header, result)]