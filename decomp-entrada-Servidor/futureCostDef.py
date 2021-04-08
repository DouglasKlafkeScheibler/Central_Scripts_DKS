from utils import tryGetFromString

#Função que pega as informações de "RELATORIOS DE SAIDA" com identificador IR
def parseFutureCostDef(content):
    filename = 'futureCostDef.csv'
    header = [
        'mnemonico', 'mnemonicoOption',
        'scenarioPrinted'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'IR' in line:
            patInfo = []

            
            result.append([
                tryGetFromString(line, 4, 11),
                tryGetFromString(line, 14, 16, int),
                tryGetFromString(line, 19, 21, int)
            ])

    return [(filename, header, result)]