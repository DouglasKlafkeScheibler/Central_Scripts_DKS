from utils import tryGetFromString

#Função que pega as informações de "CADASTRO UTE" com identificador CT
def parseThermalData(content):
    filename = 'thermal.csv'
    header = [
        'thermalId', 'subsystem', 'name', 'stageIndex',
        'minGenPat1', 'genCapPat1', 'costGenPat1',
        'minGenPat2', 'genCapPat2', 'costGenPat2',
        'minGenPat3', 'genCapPat3', 'costGenPat3',
        'minGenPat4', 'genCapPat4', 'costGenPat4',
        'minGenPat5', 'genCapPat5', 'costGenPat5'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'CT' in line:

            patInfo = []

            for i in range(5):
                patInfo.append(tryGetFromString(
                    line, 29 + i*20, 34 + i*20, float))
                patInfo.append(tryGetFromString(
                    line, 34 + i*20, 39 + i*20, float))
                patInfo.append(tryGetFromString(
                    line, 39 + i*20, 49 + i*20, float))

            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 24),
                tryGetFromString(line, 24, 26, int),
                *patInfo
            ])

    return [(filename, header, result)]
