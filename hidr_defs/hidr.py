import sys
from datetime import datetime
import hidr_defs as hd
import os

from collections import namedtuple

import sys
sys.path.append('../config')
from sendDb import sendToDb


#Esse script tem como função Utilizar as funções para extração das informações do HIDR e então preparar esses dados para exportar para 
#o banco de dados

FORMAT_HIDROEDIT = 0

TI = 0
TF = 1
TS  = 2

#Colocar no banco o histórico de 5 anos
def main():
    for y in range(6):
        year = str(y + 2015)

        for m in range(12):
            month = m + 1

            #Lembrando que estou usando o caminho absoluto dos dados. 
            if month < 9:
                pathdeck = '/Users/dougl/Desktop/Decomp-dataRaw/Decomp/' + year + '/DC' + year + '0' + str(month)
            
            else:
                pathdeck = '/Users/dougl/Desktop/Decomp-dataRaw/Decomp/' + year + '/DC' + year + str(month)

            #Logica para passear entre os arquivos
            for root, directories, files in os.walk(pathdeck, topdown=False):
                    for name in directories:
                        relatory = pathdeck + '/' + name
                        files = os.listdir(relatory)
                        for f in files:
                            if 'HIDR' in f:
                                file = relatory + '/' + f
                                print(file)
                                
                                if len(sys.argv) > 1:
                                    file = sys.argv[1]
                                    if len(sys.argv) > 2:
                                        out = sys.argv[2]
                                
                                #Try para leitura do arquivo e jogar para o banco
                                try:
                                    data = hd.readFile(file)
                                    
                                    sendToDataBase(data)
                                    # writeResults(data,out)
                                except FileNotFoundError:
                                    print('The supplied file: ' + file + " was not found.")
    
def tryGetPlant(data, plant):
    if plant in data:
        return data[plant]
    return None

#Não está sendo usado no histórico    
def writeResultsHidroEdit(data, outputName):
    fileData = ';'.join(hd.hidroHeader()) + ';\n'

    a = datetime.now()
    for plant in data.values():
        if plant != None:
                
            fileData = fileData + hd.getHydroEditString(plant,tryGetPlant(data,plant.downstream),tryGetPlant(data,plant.detour)) + '\n'
                
    b = datetime.now()
    print(b-a)
    with open(outputName, 'w') as f:
        f.write(fileData)

def writeResults(data, outputName, format = FORMAT_HIDROEDIT):
    if format == FORMAT_HIDROEDIT:
        writeResultsHidroEdit(data, outputName)


#Logica para utilizar a função sendToDb
#Foram utilizados diversas regras de negócio para deixar em um formato adequado para o Banco, então talvez não fique tão claro a primeira vista.
def sendToDataBase(data):
    fileData = ';'.join(hd.hidroHeader()) + ';\n'

    #Le todas as informações do HIDR e gera um csv a partir disso
    for plant in data.values():
        if plant != None:              
            fileData = fileData + hd.getHydroEditString(plant,tryGetPlant(data,plant.downstream),tryGetPlant(data,plant.detour)) + '\n'

    allData = []

    lines = fileData.split('\n')

    #Nessa etapa eu arrumo o csv para formatar em formato de banco para upar.
    for line in lines:
        lineData = []
        data = line.split(';')
        for row in data:
            temp = row.strip()

            if temp == '':
                temp = None

            lineData.append(temp)
        allData.append(lineData)

    allData.pop()

    allDataRight = []

    for d in allData:
        d.pop()
        allDataRight.append(d)

    table = 'dados_brutos.dec_in_hidr'
    columns = allDataRight[0]
    dataDb = allDataRight[1:]

    # print(dataDb)

    #Manda para o banco
    sendToDb(columns, dataDb, table)               

#Roda a aplicação  
main()
