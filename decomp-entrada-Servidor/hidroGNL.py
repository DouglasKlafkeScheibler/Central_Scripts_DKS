from utils import tryGetFromString

#Função que pega as informações de "TERMICAS A GNL" com identificador TG do arquivo "DADGNL"
def parseHidroGNL(content):
    filename = 'hidroGNL.csv'
    header = [
        'hidroId', 'subsystem',
        'name', 'stage',
        'minGeneration1', 'generationCapacity1',
        'generationCost1', 'minGeneration2', 
        'generationCapacity2', 'generationCost2',
        'minGeneration3', 'generationCapacity3',
        'generationCost3', 'minGeneration4', 
        'generationCapacity4', 'generationCost4',
        'minGeneration5', 'generationCapacity5',
        'generationCost5'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'TG' in line:
            patInfo = []

            
            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 24),
                tryGetFromString(line, 25, 26, int),
                tryGetFromString(line, 29, 33, float),
                tryGetFromString(line, 34, 39, float),
                tryGetFromString(line, 40, 49, float),
                tryGetFromString(line, 50, 53, float),
                tryGetFromString(line, 54, 59, float),
                tryGetFromString(line, 60, 69, float),
                tryGetFromString(line, 70, 73, float),
                tryGetFromString(line, 74, 79, float),
                tryGetFromString(line, 80, 89, float),
                tryGetFromString(line, 90, 93, float),
                tryGetFromString(line, 94, 99, float),
                tryGetFromString(line, 100, 109, float),
                tryGetFromString(line, 110, 113, float),
                tryGetFromString(line, 114, 119, float),
                tryGetFromString(line, 120, 129, float)
            ])

    return [(filename, header, result)]