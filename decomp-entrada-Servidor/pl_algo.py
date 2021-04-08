from utils import tryGetFromString

#Função que pega as informações de "ALGORITMO DA PL" com identificador PD
def parsePlAlgo(content):
    filename = 'plAlgo.csv'
    header = ['mnemonico']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'PD' in line:

            result.append([tryGetFromString(line, 4, 10)])

    return [(filename, header, result)]

