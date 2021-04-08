from utils import tryGetFromString

#Função que pega as informações de "eletricas" com os identificadores RE, LU, FU, FT, FI e FE 
def parseElectricRest(content):
    reFilename = 'electricrest_re.csv'
    limitsFilename = 'electricrest_limits.csv'
    participHydroFilename = 'electricrest_hydro.csv'
    participThermalFilename = 'electricrest_therm.csv'
    participInterchangeFilename = 'electricrest_inter.csv'
    participExportImportFilename = 'electricrest_expimp.csv'

    reHeader = [
        'restrictionIndex', 'initialStage',
        'finalStage'
    ]

    limitsHeader = [
        'restrictionIndex', 'stageIndex',
        'infLimitPat1', 'supLimitPat1',
        'infLimitPat2', 'supLimitPat2',
        'infLimitPat3', 'supLimitPat3',
        'infLimitPat4', 'supLimitPat4',
        'infLimitPat5', 'supLimitPat5'
    ]

    participHydroHeader = [
        'restrictionIndex', 'stageIndex',
        'hydroId', 'participationFactor'
    ]

    participThermalHeader = [
        'restrictionIndex', 'stageIndex',
        'hydroId', 'subsystem', 'participationFactor'
    ]

    participInterchangeHeader = [
        'restrictionIndex', 'stageIndex',
        'fromSystem', 'toSystem',
        'participationFactor'
    ]

    participExportImportHeader = [
        'restrictionIndex', 'stageIndex',
        'contractIndex', 'subsystem',
        'participationFactor'
    ]

    reResult = []
    limitsResult = []
    participHydroResult = []
    participThermalResult = []
    participInterchangeResult = []
    participExportImportResult = []
    lines = content.splitlines()[1:]

    for line in lines:

        if '&' in line or line.strip() == '':
            continue

        # RESTRICTIONS

        if 'RE' in line:

            reResult.append([
                tryGetFromString(line, 4, 8, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 16, int)
            ])

        # LIMITS

        if 'LU' in line: 
            patInfo = []

            for i in range(5):
                patInfo.append(tryGetFromString(
                    line, 14 + i*20, 24 + i*20, float))
                patInfo.append(tryGetFromString(
                    line, 24 + i*20, 34 + i*20, float))

            limitsResult.append([
                tryGetFromString(line, 4, 8, int),
                tryGetFromString(line, 9, 11, int),
                *patInfo
            ])

        # PARTICIPATION HYDRO

        if 'FU' in line:
            patInfo = []

            participHydroResult.append([
                tryGetFromString(line, 4, 8, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 17, int),
                tryGetFromString(line, 19, 29, float)
            ])

        # PARTICIPATION THERMAL

        if 'FT' in line:
            patInfo = []

            participThermalResult.append([
                tryGetFromString(line, 4, 8, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 17, int),
                tryGetFromString(line, 19, 21, int),
                tryGetFromString(line, 24, 34, float)
            ])

        # PARTICIPATION INTERCONNECTIONS

        if 'FI' in line:
            patInfo = []

            participInterchangeResult.append([
                tryGetFromString(line, 4, 8, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 16),
                tryGetFromString(line, 19, 21),
                tryGetFromString(line, 24, 34, float)
            ])

        # PARTICIPATION CONTRACTS

        if 'FE' in line:
            patInfo = []

            participExportImportResult.append([
                tryGetFromString(line, 4, 8, int),
                tryGetFromString(line, 9, 11, int),
                tryGetFromString(line, 14, 17, int),
                tryGetFromString(line, 19, 21, int),
                tryGetFromString(line, 24, 34, float)
            ])

    return [(reFilename, reHeader, reResult),
            (limitsFilename, limitsHeader, limitsResult),
            (participHydroFilename, participHydroHeader,
             participHydroResult), (participThermalFilename,
                                    participThermalHeader, participThermalResult),
            (participInterchangeFilename, participInterchangeHeader,
             participInterchangeResult), (participExportImportFilename, participExportImportHeader, participExportImportResult)]
