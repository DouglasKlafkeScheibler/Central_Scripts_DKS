from utils import tryGetFromString

#Função que pega as informações de "TAXA DE ENCHIMENTO" com identificador VM
def parseFillRate(content):
    filename = 'fillRate.csv'
    header = ['hydroelectric', 'subsystem']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'VM' in line:

            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, float),
            ])

    return [(filename, header, result)]

