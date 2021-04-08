from utils import tryGetFromString

#Função que pega as informações de "GERACOES DE TERMICAS GNL JA COMANDADAS" com identificador GL do arquivo "DADGNL"
def parseThermalGenerationGNL(content):
    filename = 'thermalGenerationGNL.csv'
    header = [
        'thermalId', 'subsystem',
        'week', 'generation1',
        'duration1', 'generation2',
        'duration2', 'generation3',
        'duration3', 'inicialWeek',
        'inicialMonth'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'GL' in line:
            patInfo = []

            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 16, int),
                tryGetFromString(line, 19, 29, float),
                tryGetFromString(line, 30, 34, float),
                tryGetFromString(line, 35, 44, float),
                tryGetFromString(line, 45, 49, float),
                tryGetFromString(line, 50, 59, float),
                tryGetFromString(line, 60, 64, float),
                tryGetFromString(line, 65, 67, int),
                tryGetFromString(line, 68, 69, int)
            ])

    return [(filename, header, result)]