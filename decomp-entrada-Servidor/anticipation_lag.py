from utils import tryGetFromString

#Função que pega as informações de "LAG DE ANTECIPACAO DE DESPACHO" com identificador NL do arquivo "DADGNL"
def parseAnticipationLag(content):
    filename = 'anticipationLag.csv'
    header = [
        'thermalId', 'subsystem',
        'dispatchAnticipationLag'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'NL' in line:
            patInfo = []

            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 15, int)
            ])

    return [(filename, header, result)]