from utils import tryGetFromString

#Função que pega as informações de "RESTRICOES DE VAZAO DEFLUENTE" com identificadores HQ, LQ e CQ
def parseOutflowRest(content):
    HQFilename = 'outflowRestHQ.csv'
    LQFilename = 'outflowRestLQ.csv'
    CQFilename = 'outflowRestCQ.csv'

    HQHeader = [
        'restrictionFlowId', 'inicialStage',
        'finalStage'
    ]

    LQHeader = [
        'restrictionFlowId', 'stageNum',
        'inferiorLimit1', 'superiorLimit1',
        'inferiorLimit2', 'superiorLimit2',
        'inferiorLimit3', 'superiorLimit3',
        'inferiorLimit4', 'superiorLimit4',
        'inferiorLimit5', 'superiorLimit5',
    ]

    CQHeader = [
        'restrictionFlowId', 'stageNum',
        'hidroId', 'coefficient',
        'variableType'
    ]
  
    HQResult = []
    LQResult = []
    CQResult = []
    lines = content.splitlines()[1:]

    for line in lines:

        if '&' in line or line.strip() == '':
            continue

        # HQ

        if 'HQ' in line:

            HQResult.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 16, int)
            ])

        # LQ

        if 'LQ' in line:

            LQResult.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 24, float),
                tryGetFromString(line, 25, 34, float),
                tryGetFromString(line, 35, 44, float),
                tryGetFromString(line, 45, 54, float),
                tryGetFromString(line, 55, 64, float),
                tryGetFromString(line, 65, 74, float),
                tryGetFromString(line, 75, 84, float),
                tryGetFromString(line, 85, 94, float),
                tryGetFromString(line, 95, 104, float),
                tryGetFromString(line, 105, 114, float),
            ])

        # CQ

        if 'CQ' in line:

            CQResult.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 17, int),
                tryGetFromString(line, 19, 29, float),
                tryGetFromString(line, 34, 38)
            ])

    return [(HQFilename, HQHeader, HQResult),
            (LQFilename, LQHeader, LQResult),
            (CQFilename, CQHeader, CQResult)]