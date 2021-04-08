from utils import tryGetFromString

#Função que pega as informações de "FUNCAO DE ENERGIA ARMAZENADA" com identificador EZ
def parseStoredEnergy(content):
    filename = 'storedEnergy.csv'
    header = ['hidroId', 'usefulVolume']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'EZ' in line:
            patInfo = []

            
            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 14, float)
            ])

    return [(filename, header, result)]