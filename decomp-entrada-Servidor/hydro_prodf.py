from utils import tryGetFromString

#Função que pega as informações de "FUNCOES DE PRODUCAO DAS UHEs" com identificador FP
def parseHydroProdf(content):
    filename = 'hydroProdf.csv'
    header = ['hydroelectric', 'stage',
            'turbineFlag', 'turbinePoints', 
            'turbinelowerLimit', 'turbineUpperLimit', 
            'volumeFlag', 'volumePoints',
            'volumeLowerLimit', 'volumeUpperLimit', 
            'hydraulicGenerationLowerLimit', 'hydraulicGenerationUpperLimit', 
            'desviationTolerance', 'dynamicModelingFlag', 
            'typeInputFlag', 'inicialFPHADPoints', 
            'additionalFPHADPoints', 'maxIteractionsFPHAD'
        ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'FP' in line:

            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 12, int),
                tryGetFromString(line, 14, 15, int),
                tryGetFromString(line, 16, 20, int),
                tryGetFromString(line, 21, 26, float),
                tryGetFromString(line, 27, 32, float),
                tryGetFromString(line, 34, 35, int),
                tryGetFromString(line, 36, 40, int),
                tryGetFromString(line, 41, 46, float),
                tryGetFromString(line, 47, 52, float),
                tryGetFromString(line, 54, 59, float),
                tryGetFromString(line, 60, 65, float),
                tryGetFromString(line, 66, 69, float),
                tryGetFromString(line, 71, 72, int),
                tryGetFromString(line, 76, 77, int),
                tryGetFromString(line, 78, 83, int),
                tryGetFromString(line, 84, 89, int),
                tryGetFromString(line, 90, 91, int)
            ])

    return [(filename, header, result)]

