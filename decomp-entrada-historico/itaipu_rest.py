from utils import tryGetFromString

#Função que pega as informações de "RESTRICAO ITAIPU" com identificador IT
def parseItaipuRest(content):
    filename = 'itaipuRest.csv'
    header = ['stage', 'INDICIDEUSINA',
            'subsystem', 'generationItaPat1',
            'loadAndePat1','generationItaPat2',
            'loadAndePat2', 'generationItaPat3',
            'loadAndePat3'  
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'IT' in line:

            result.append([
                tryGetFromString(line, 4, 6, int),
                tryGetFromString(line, 9, 12, int),
                tryGetFromString(line, 14, 16, int),
                tryGetFromString(line, 19, 24, float),
                tryGetFromString(line, 25, 29, float),
                tryGetFromString(line, 30, 34, float),
                tryGetFromString(line, 35, 39, float),
                tryGetFromString(line, 40, 44, float),
                tryGetFromString(line, 45, 49, float)
            ])

    return [(filename, header, result)]

