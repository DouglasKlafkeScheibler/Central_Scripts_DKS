from utils import tryGetFromString

#Função que pega as informações de "PATAMARES DE CARGA EM ORDEM CRESCENTE" com identificador RC
def parseStairRestrictions(content):
    filename = 'stairRestrictions.csv'
    header = ['mnemonico']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'RC' in line:
            patInfo = []

            result.append([tryGetFromString(line, 4, 10)])

    return [(filename, header, result)]