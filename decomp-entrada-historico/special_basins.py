from utils import tryGetFromString

#Função que pega as informações de "BACIAS ESPECIAIS/PEQUENAS USINAS" com identificador BE
def parseSpecialBasins(content):
    filename = 'specialBasins.csv'
    header = [
        'name', 'subsystem',
        'stage', 'generationPat1',
        'generationPat2', 'generationPat3',
        'gravityLost'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'BE' in line:
            patInfo = []

            
            result.append([
                tryGetFromString(line, 4, 14),
                tryGetFromString(line, 14, 16, int),
                tryGetFromString(line, 19, 21, int),
                tryGetFromString(line, 24, 29, float),
                tryGetFromString(line, 30, 34, float),
                tryGetFromString(line, 35, 39, float),
                tryGetFromString(line, 40, 44, float)
            ])

    return [(filename, header, result)]