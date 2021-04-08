from utils import tryGetFromString

#Função que pega as informações de "OS SUBSISTEMAS" com identificador SB
def parseSubsystem(content):
    filename = 'subsystem.csv'
    header = ['subsystem', 'mnemonic']
    result = []
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'SB' in line:
            result.append([int(line[4:6]), line[9:11].strip()])

    return [(filename, header, result)]