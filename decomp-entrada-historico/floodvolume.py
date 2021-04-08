from utils import tryGetFromString

#Função que pega as informações de "VOLUME DE ESPERA" com identificador VE
def parseFloodVolume(content):
    filename = 'floodvol.csv'
    header = ['hydroId', 'floodVolumeStage1', 
              'floodVolumeStage2', 'floodVolumeStage3',
              'floodVolumeStage4', 'floodVolumeStage5',
              'floodVolumeStage6', 'floodVolumeStage7',
              'floodVolumeStage8', 'floodVolumeStage9'
    ]
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue
        if 'VE' in line:

            patInfo = []
            stageId = 0
            lastInfo = 0

            while lastInfo != -1:
                lastInfo = tryGetFromString(
                    line, 9 + stageId*5, 14 + stageId*5, float)

                if stageId == 9:
                    break

                patInfo.append(lastInfo)

                stageId = stageId + 1

            result.append([
                tryGetFromString(line, 4, 7, int),
                *patInfo
            ])

    return [(filename, header, result)]
