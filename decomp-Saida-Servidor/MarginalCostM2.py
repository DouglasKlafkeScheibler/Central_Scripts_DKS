from utils import tryGetFromString
import datetime    

#Função que pega as informações de "PROB ACUMUL", "Valor  esperado  do  custo  futuro", "Custo marginal de operacao do subsistema SE, S, NE, N, FC"
#do relato 2
def marginalCostM2(content):
    header = [
        'prob_acu', 'cmo_SE', 'cmo_S', 
        'cmo_NE', 'cmo_N', 'cmo_FC', 
        'VECF', 'cenario', 'deck_date'
    ]
    result = []
    lines = content.splitlines()[1:]

    #Regra de negócio para achar a data do planejamento
    for line in lines[:8]:
        if 'PLANEJAMENTO' in line:
            dateRelato = datetime.datetime.strptime(line[98:109], "%d/%m/%Y").strftime("%Y-%m-%d")

    validy = False
    cenario = 0
    probAcu = ''
    cmoSe = ''
    cmoS = ''
    cmoNe = ''
    cmoN = ''
    cmoFc = ''
    VECF = ''

    for line in lines: 
        if 'PROB ACUMUL' in line:
            probAcu = tryGetFromString(line, 67, 75)

        elif 'Valor  esperado  do  custo  futuro' in line:
            VECF = tryGetFromString(line, 52, 68)
            cenario = cenario + 1

        elif 'Custo marginal de operacao do subsistema SE' in line:
            cmoSe = tryGetFromString(line, 60, 68)

        elif 'Custo marginal de operacao do subsistema S' in line:
            cmoS = tryGetFromString(line, 60, 68)

        elif 'Custo marginal de operacao do subsistema NE'in line:
            cmoNe = tryGetFromString(line, 60, 68)

        elif 'Custo marginal de operacao do subsistema N' in line:
            cmoN = tryGetFromString(line, 60, 68)    
        
        elif 'Custo marginal de operacao do subsistema FC' in line:
            cmoFc = tryGetFromString(line, 60, 68)
            result.append([
                probAcu,
                cmoSe,
                cmoS,
                cmoNe,
                cmoN,
                cmoFc,
                VECF,
                cenario,
                dateRelato
            ])

    newResult = []

    for data in result:
        newResult.append([x if x != '' else None for x in data])

    if len(newResult) == 0:
        newResult = [[None, None, None, None, None, None, None, None, dateRelato]]
    
    return [(header, newResult)]