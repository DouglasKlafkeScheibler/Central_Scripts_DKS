from pathlib import Path
import os
from UsefulVolReservoirs import usefulVolReservoirs
from StoredEnergyREE import storedEnergyREE
from StoredEnergySubsystem import storedEnergySubsytem
from ExchangeFlow import exchangeFlow
from MarginalCost import marginalCost
from ThermalGenerationSubsystem import thermalGenerationSubsystem
from HydraulicGeneration import hydraulicGeneration
from ThermalGeneration import thermalGeneration
from SmallPlants import smallPlants
from GrossDemand import grossDemand
from HydraulicGenerationItaipu import hydraulicGenerationItaipu
from EnergyInterconnectedSubsystems import energyInterconnectedSubsystems

from MarginalCostM2 import marginalCostM2

import sys
sys.path.append('../config')
from sendDb import sendToDb

# Esse Script tem como função fazer a aquisição das informações de saida do Decomp e salvar no banco de dados.
# Nesse Script tem varias referencias a outros scripts que são especializadas para pegar as informações especificas de cada bloco


def readFile(path):
    retval = ''
    with open(path,'r',encoding='latin1') as f:
        retval = f.read()
    return retval


#Bloco de arquivos que serão coletados do sumário, e que tem suas funções de coleta
blocksSumario = [
        'usefulVolReservoirs',           #Volume util reservatorios
        'storedEnergyREE',               #Energia armazenada nos REEs
        'storedEnergySubsytem',          #Energia armazenada nos subsistemas
        'exchangeFlow',                  #Fluxo nos intercambios
        'hydraulicGenerationItaipu',     #Geracao hidraulica em itaipu
        'energyInterconnectedSubsystems',#Energia para os subsistemas interligados
        'marginalCost',                  #Custo marginal de operacao
        'thermalGenerationSubsystem',    #Geracao termica nos subsistemas
        'hydraulicGeneration',           #Gercao hidraulica
        'thermalGeneration',             #Geracao termica
        'smallPlants',                   #Pequenas usinas
        'grossDemand'                    #Demanda bruta
    ]


def upload_data_deckOut(path = '../decomp-entrada-Servidor/tempDecomp'):
        #Logica 1 mes de arquivos
        for root, directories, files in os.walk(path, topdown=False):
            for name in directories:
                relatory = path + '/' + name
                files = os.listdir(relatory)
                for f in files:

                    #Pega as informações dos arquivos de Sumário referentes ao bloco "blocoSumario"
                    if 'sumario' in f:
                        file = relatory + '/' + f
                        print(file)
                        lines = readFile(file)

                        functions = globals()

                        #Para cada script de coleta, executar sua função associada
                        for block in blocksSumario:
                            print('table:' + block)

                            #Joga as linhas para extração
                            result = functions[block](lines)

                            #Para cada dado colocar no banco
                            for info in result:
                                columns = info[0]
                                data = info[1]
                                table = 'dec_out_' + block
                                # print(data)

                                #Função para enviar para o banco
                                sendToDb(columns, data, table)
                   
                   #Pega as informações de Custo marginal de operação no arquivo de relato 2
                    elif 'relato2' in f:
                        file = relatory + '/' + f
                        print(file)
                        lines = readFile(file)

                        #Joga as linhas para extração
                        result = marginalCostM2(lines)

                        for info in result:
                            columns = info[0]
                            data = info[1]
                            table = 'dec_out_MarginalCost_m2'
                            # print(data)
                            sendToDb(columns, data, table)   