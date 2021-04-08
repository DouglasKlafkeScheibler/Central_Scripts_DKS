from utils import tryGetFromString

#Função que pega as informações de "MANUTENCOES PROGRAMADAS HIDRAULICAS" com identificador MP
def parseMaintenanceHydro(content):
    filename = 'mainthydro.csv'
    header = [
        'hydroId', 'maintFactorStage1',
        'maintFactorStage2', 'maintFactorStage3',
        'maintFactorStage4', 'maintFactorStage5',
        'maintFactorStage6', 'maintFactorStage7',
        'maintFactorStage8', 'maintFactorStage9',
        'maintFactorStage10'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'MP' in line[:3]:

            result.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 14),
                tryGetFromString(line, 14, 19),
                tryGetFromString(line, 19, 24),
                tryGetFromString(line, 24, 29),
                tryGetFromString(line, 29, 34),
                tryGetFromString(line, 34, 39),
                tryGetFromString(line, 39, 44),
                tryGetFromString(line, 44, 49),
                tryGetFromString(line, 49, 54),
                tryGetFromString(line, 54, 59),
            ])


    return [(filename, header, result)]