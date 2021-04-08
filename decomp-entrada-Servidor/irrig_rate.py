from utils import tryGetFromString

#Função que pega as informações de "TAXA DE IRRIGACAO" com identificador TI
def parseIrrigRate(content):
    filename = 'irrigRate.csv'
    header = [
        'hidroId', 'divertedFlow1',
        'divertedFlow2', 'divertedFlow3',
        'divertedFlow4', 'divertedFlow5',
        'divertedFlow6'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'TI' in line:
            patInfo = []

            
            result.append([
                tryGetFromString(line, 5, 7, int),
                tryGetFromString(line, 8, 14, float),
                tryGetFromString(line, 15, 19, float),
                tryGetFromString(line, 20, 24, float),
                tryGetFromString(line, 25, 29, float),
                tryGetFromString(line, 30, 34, float),
                tryGetFromString(line, 35, 39, float)
            ])

    return [(filename, header, result)]