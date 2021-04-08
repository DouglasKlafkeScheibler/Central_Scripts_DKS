from utils import tryGetFromString


#Funções que compõem a tabela parametro
def parseTitle(content):
    result = {'title': ''}
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'TE' in line:
            result['title'] = (result['title'] + line).rstrip()

    return result

def parseDiscountRate(content):
    result = {}
    lines = content.splitlines()[1:]
    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'TX' in line:
            result['discountRate'] = tryGetFromString(line, 4, 9, float, 10.0)

    return result


def parseConvergenceTol(content):
    result = {}
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'GP' in line:
            result['convergenceTolerance'] = tryGetFromString(
                line, 4, 14, float, 0.001)

    return result


def parseTotalIteration(content):
    result = {}
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'NI' in line:
            result['totalIterations'] = tryGetFromString(
                line, 4, 7, float, 10.0)
            result['maximumIteration'] = tryGetFromString(line, 8, 9, int, 0) == 0

    return result


def parseRefDate(content):
    from datetime import date
    result = {}
    lines = content.splitlines()[1:]

    for line in lines:
        if '&' in line or line.strip() == '':
            continue

        if 'DT' in line:
            rawDate = list(filter(None, line.split(' ')[1:]))
            rawDate.reverse()
            result['referenceDate'] = '{}-{}-{}T00:00:00-0300'.format(*rawDate)

    return result

