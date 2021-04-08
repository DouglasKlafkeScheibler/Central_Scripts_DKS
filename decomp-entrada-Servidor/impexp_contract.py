from utils import tryGetFromString

#Função que pega as informações de "CONTRATOS DE IMPORTACAO E EXPORTACAO" com identificadores CI e CE
def parseImpexpContract(content):
    CIFilename = 'impexpContractCI.csv'
    CEFilename = 'impexpContractCE.csv'

    CIHeader = [
        'contractId', 'subsystem',
        'name', 'stageId',
        'inferiorLimit1', 'superiorLimit1',
        'energyCost1', 'inferiorLimit2', 
        'superiorLimit2', 'energyCost2',
        'inferiorLimit3', 'superiorLimit3',
        'energyCost3', 'inferiorLimit4', 
        'superiorLimit4', 'energyCost4', 
        'inferiorLimit5', 'superiorLimit5',
        'energyCost5', 'lossFactorGravityCenter'
    ]

    CEHeader = [
        'contractId', 'subsystem',
        'name', 'stageId',
        'inferiorLimit1', 'superiorLimit1',
        'energyCost1', 'inferiorLimit2', 
        'superiorLimit2', 'energyCost2',
        'inferiorLimit3', 'superiorLimit3',
        'energyCost3', 'inferiorLimit4', 
        'superiorLimit4', 'energyCost4', 
        'inferiorLimit5', 'superiorLimit5',
        'energyCost5', 'lossFactorGravityCenter'
    ]
  
    CIResult = []
    CEResult = []
    lines = content.splitlines()[1:]

    for line in lines:

        if '&' in line or line.strip() == '':
            continue

        # CI

        if 'CI' in line:

            CIResult.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 8, 10, int),
                tryGetFromString(line, 11, 21),
                tryGetFromString(line, 24, 26, int),
                tryGetFromString(line, 29, 34, float),
                tryGetFromString(line, 35, 39, float),
                tryGetFromString(line, 40, 49, float),
                tryGetFromString(line, 50, 54, float),
                tryGetFromString(line, 55, 59, float),
                tryGetFromString(line, 60, 69, float),
                tryGetFromString(line, 70, 74, float),
                tryGetFromString(line, 75, 79, float),
                tryGetFromString(line, 80, 89, float),
                tryGetFromString(line, 90, 94, float),
                tryGetFromString(line, 95, 99, float),
                tryGetFromString(line, 100, 109, float),
                tryGetFromString(line, 110, 114, float),
                tryGetFromString(line, 115, 119, float),
                tryGetFromString(line, 120, 129, float),
                tryGetFromString(line, 130, 134, float)
            ])

        # CE

        if 'CE' in line:

            CEResult.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 8, 10, int),
                tryGetFromString(line, 11, 21),
                tryGetFromString(line, 24, 26, int),
                tryGetFromString(line, 29, 34, float),
                tryGetFromString(line, 35, 39, float),
                tryGetFromString(line, 40, 49, float),
                tryGetFromString(line, 50, 54, float),
                tryGetFromString(line, 55, 59, float),
                tryGetFromString(line, 60, 69, float),
                tryGetFromString(line, 70, 74, float),
                tryGetFromString(line, 75, 79, float),
                tryGetFromString(line, 80, 89, float),
                tryGetFromString(line, 90, 94, float),
                tryGetFromString(line, 95, 99, float),
                tryGetFromString(line, 100, 109, float),
                tryGetFromString(line, 110, 114, float),
                tryGetFromString(line, 115, 119, float),
                tryGetFromString(line, 120, 129, float),
                tryGetFromString(line, 130, 134, float)
            ])

    return [(CIFilename, CIHeader, CIResult),
            (CEFilename, CEHeader, CEResult)]