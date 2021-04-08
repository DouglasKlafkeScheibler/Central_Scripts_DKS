from utils import tryGetFromString

#Função que pega as informações de "FATOR DE DISPONIBILIDADE DE USINAS HIDRAULICAS" com identificador FD
def parseDisponibilityFactor(content):
    filename = 'dispfactor.csv'
    header = ['hydroId', 'dispFactorStage1',
              'dispFactorStage2', 'dispFactorStage3',
              'dispFactorStage4', 'dispFactorStage5',
              'dispFactorStage6', 'dispFactorStage7',
              'dispFactorStage8'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'FD' in line:

            patInfo = []
            stageId = 0
            lastInfo = 0

            while lastInfo != -1:
                lastInfo = tryGetFromString(
                    line, 9 + stageId*5, 14 + stageId*5, float)

                if stageId == 8:
                    break

                patInfo.append(lastInfo)

                stageId = stageId + 1

            result.append([
                tryGetFromString(line, 4, 7, int),
                *patInfo
            ])

    return [(filename, header, result)]
