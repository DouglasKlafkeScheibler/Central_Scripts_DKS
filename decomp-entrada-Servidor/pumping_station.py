from utils import tryGetFromString

#Função que pega as informações de "ESTACOES DE BOMBEAMENTO" com identificador UE
def parsePumpingStation(content):
    filename = 'pumpingStation.csv'
    header = [
        'station', 'subsystem',
        'stationName', 'hydroUpstream',
        'hydroDownstream', 'minFlow',
        'maxFlow', 'consumptionRate'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'UE' in line:
            patInfo = []

            
            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 26),
                tryGetFromString(line, 29, 32, int),
                tryGetFromString(line, 34, 37, int),
                tryGetFromString(line, 39, 49, float),
                tryGetFromString(line, 50, 59, float),
                tryGetFromString(line, 60, 69, float)
            ])

    return [(filename, header, result)]