from utils import tryGetFromString

#Função que pega as informações de "RESTRICOES DE VOLUME ARMAZENADO/VAZAO DEFLUENTE" com identificadores HV, LV e CV
def parseVolumeRest(content):
    HvFilename = 'volumeRestHV.csv'
    LvFilename = 'volumeRestLV.csv'
    CvFilename = 'volumeRestCV.csv'

    HvHeader = [
        'volumeRestId', 'inicialStage',
        'finalStage'
    ]

    LvHeader = [
        'volumeRestId', 'stageNum',
        'inferiorLimit', 'superiorLimit'
    ]

    CvHeader = [
        'volumeRestId', 'stageNum',
        'hidroId', 'coefficient',
        'variableType'
    ]
  
    HvResult = []
    LvResult = []
    CvResult = []
    lines = content.splitlines()[1:]

    for line in lines:

        if '&' in line or line.strip() == '':
            continue

        # HV

        if 'HV' in line:

            HvResult.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 16, int)
            ])

        # LV

        if 'LV' in line:

            LvResult.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 24, float),
                tryGetFromString(line, 25, 34, float)
            ])

        # CV

        if 'CV' in line:

            CvResult.append([
                tryGetFromString(line, 4, 7, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 17, int),
                tryGetFromString(line, 19, 29, float),
                tryGetFromString(line, 34, 38)
            ])

    return [(HvFilename, HvHeader, HvResult),
            (LvFilename, LvHeader, LvResult),
            (CvFilename, CvHeader, CvResult)]