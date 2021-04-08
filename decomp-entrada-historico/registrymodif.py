from utils import tryGetFromString

#Função que pega as informações de "MODIFICACAO DO CADASTRO" com identificador AC
def parseRegistryModif(content):
    filename = 'registrymodif.csv'
    header = ['hydroId', 'modifiedParameter', 'newValue1',
              'newValue2', 'newValue3', 'month', 'week', 'year']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'AC' in line:
            modifType = tryGetFromString(line, 9, 15).strip()
            modifValues = []

            if modifType == 'NOMEUH':
                modifValues.append(tryGetFromString(line, 19, 31).strip())
                modifValues.append(None)
                modifValues.append(None)
            elif modifType == 'NPOSNW' or modifType == 'NUMPOS' or modifType == 'NUMJUS' or modifType == 'NUMCON' or modifType == 'VERTJU' or modifType == 'VAZMIN' or modifType == 'NUMBAS' or modifType == 'TIPTUR' or modifType == 'TIPERH' or modifType == 'JUSENA':
                modifValues.append(tryGetFromString(line, 19, 24, int))
                modifValues.append(None)
                modifValues.append(None)
            elif modifType == 'DESVIO' or modifType == 'POTEFE' or modifType == 'ALTEFE' or modifType == 'NCHAVE':
                modifValues.append(tryGetFromString(line, 19, 24, int))
                modifValues.append(tryGetFromString(line, 24, 34, float))
                modifValues.append(None)
            elif modifType == 'VOLMIN' or modifType == 'VOLMAX' or modifType == 'PROESP' or modifType == 'PERHID' or modifType == 'JUSMED' or modifType == 'VSVERT' or modifType == 'VMDESV':
                modifValues.append(tryGetFromString(line, 19, 29, float))
                modifValues.append(None)
                modifValues.append(None)
            elif modifType == 'COFEVA' or modifType == 'NUMMAQ' or modifType == 'VAZEFE':
                modifValues.append(tryGetFromString(line, 19, 24, int))
                modifValues.append(tryGetFromString(line, 24, 29, int))
                modifValues.append(None)
            elif modifType == 'COTVOL'or modifType == 'COTARE':
                modifValues.append(tryGetFromString(line, 19, 24, int))
                modifValues.append(tryGetFromString(line, 24, 69, float))
                modifValues.append(None)
            elif modifType == 'COTVAZ':
                modifValues.append(tryGetFromString(line, 19, 24, int))
                modifValues.append(tryGetFromString(line, 24, 29, int))
                modifValues.append(tryGetFromString(line, 29, 69, float))
            elif modifType == 'VAZCCF':
                modifValues.append(tryGetFromString(line, 19, 29, float))
                modifValues.append(tryGetFromString(line, 29, 34, int))
                modifValues.append(tryGetFromString(line, 34, 44, float))
            elif modifType == 'TIPUSI':
                modifValues.append(tryGetFromString(line, 19, 20))
                modifValues.append(None)
                modifValues.append(None)
            else:
                print('UNKNOWN REGISTRY MODIFICATION', modifType)
                modifValues.append(None)
                modifValues.append(None)
                modifValues.append(None)

            result.append([
                tryGetFromString(line, 4, 7, int),
                modifType,
                *modifValues,
                tryGetFromString(line, 69, 72),
                tryGetFromString(line, 74, 75, int),
                tryGetFromString(line, 76, 80, int)


            ])
    return [(filename, header, result)]
