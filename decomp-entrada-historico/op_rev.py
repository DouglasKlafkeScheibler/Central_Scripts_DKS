from utils import tryGetFromString

#Função que pega as informações de "REVISAO DA OPERACAO" com identificador RV
def parseOpRev(content):
    filename = 'opRev.csv'
    header = ['mnemonico', 'inicialStage', 'finalStage']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'RV' in line:

            result.append([
                tryGetFromString(line, 4, 11),
                tryGetFromString(line, 14, 15, int),
                tryGetFromString(line, 19, 20, int)
            ])

    return [(filename, header, result)]

