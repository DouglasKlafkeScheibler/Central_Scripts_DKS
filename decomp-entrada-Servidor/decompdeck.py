from collections import namedtuple
import argparse

# [PARSING]

from utils import tryGetFromString
import os
from deficit import parseDeficit
from dispfactor import parseDisponibilityFactor
from electric_rest import parseElectricRest
from exchangelimit import parseExchangeLimits
from floodvolume import parseFloodVolume
from load import parseSystemLoad
from maintenance_hydro import parseMaintenanceHydro
from maintenance_thermal import parseMaintenanceThermal
from parameter import (parseConvergenceTol, parseDiscountRate, parseRefDate,
                       parseTitle, parseTotalIteration)
from registrymodif import parseRegistryModif
from res_volume import parseReservoirVolume
from smallplant import parseSmallPlant
from subsystem import parseSubsystem
from thermal import parseThermalData
from traveltime import parseTravelTime
from pumping_station import parsePumpingStation
from special_basins import parseSpecialBasins
from stair_restrictions import parseStairRestrictions
from itaipu_rest import parseItaipuRest
from pl_algo import parsePlAlgo
from fill_rate import parseFillRate
from op_rev import parseOpRev
from hydro_prodf import parseHydroProdf
from output_report import parseOutputReport
from irrig_rate import parseIrrigRate
from historic_outflow import parseHistoricOutflow
from stored_energy import parseStoredEnergy
from volume_rest import parseVolumeRest
from outflow_rest import parseOutflowRest
from impexp_contract import parseImpexpContract
# from parameters_elements import parseParametersElements

from hidroGNL import parseHidroGNL
from interval_month import parseIntervalMonth
from anticipation_lag import parseAnticipationLag
from thermal_generationGNL import parseThermalGenerationGNL

import sys
sys.path.append('../config')
from sendDb import sendToDb

sys.path.append('../decomp-Saida-Servidor')
from DecompDeckOut import upload_data_deckOut


from download_decks_decomp import download_decomp
import shutil 


#Esse Script tem como função chamar todas as funções de coleta que são relacionadas a Decomp de entrada 
#e enviar as informações para o banco de dados "CENTRAL".


# [PARSING]

Block = namedtuple("Block", ['argname', 'parseFunc', 'isParam', 'isDger'])

REF_DATE = 17

#Todos os blocos que serão upados e algumas variaveis auxiliares
def setupBlocks():
    return {
        1: Block('-', parseTitle, True, True), # DGER
        2: Block('-subsystem', parseSubsystem, False, True),
        3: Block('-reservoir', parseReservoirVolume, False, True),
        4: None,#Block('-thermal', parseThermalData, False, True),
        5: Block('-pumpStation', parsePumpingStation, False, True),
        6: Block('-load', parseSystemLoad, False, True),
        7: Block('-deficit', parseDeficit, False, True),
        8: Block('-specialBasins', parseSpecialBasins, False, True),
        9: Block('-smallplant', parseSmallPlant, False, True),
        10: Block('-itaipuRest', parseItaipuRest, False, True),
        11: Block('-exchangelimit', parseExchangeLimits, False, True),
        12: Block('-stairRestrictions', parseStairRestrictions, False, True),
        13: Block('-', parseDiscountRate, True, True),
        14: Block('-', parseConvergenceTol, True, True),
        15: Block('-', parseTotalIteration, True, True),
        16: Block('-plAlgo', parsePlAlgo, False, True),
        17: None, # Special case
        18: Block('-mainthydro', parseMaintenanceHydro, False, True), # --> Esse bloco foi alterado em 2019
        19: Block('-maintthermal', parseMaintenanceThermal, False, True),
        20: Block('-dispfactor', parseDisponibilityFactor, False, True),
        21: Block('-floodvol', parseFloodVolume, False, True),
        22: Block('-fillRate', parseFillRate, False, True),
        23: Block('-electricrest', parseElectricRest, False, True),
        24: Block('-traveltime', parseTravelTime, False, True),
        25: Block('-registrymodif', parseRegistryModif, False, True),
        26: Block('-opRev', parseOpRev, False, True),
        27: Block('-hydroProdf', parseHydroProdf, False, True),
        28: Block('-outputReport', parseOutputReport, False, True),
        29: Block('-impexpContract', parseImpexpContract, False, True),
        30: None,
        31: None,
        32: Block('-irrigRate', parseIrrigRate, False, True),
        33: Block('-historicOutflow', parseHistoricOutflow, False, True),
        34: Block('-storedEnergy', parseStoredEnergy, False, True),
        35: Block('-volumeRest', parseVolumeRest, False, True),
        36: Block('-outflowRest', parseOutflowRest, False, True), # DGER
        37: Block('-hidroGNL', parseHidroGNL, False, False), # DGNL 
        38: Block('-intervalMonth', parseIntervalMonth, False, False),
        39: Block('-anticipationLag', parseAnticipationLag, False, False),
        40: Block('-thermalGenationGNL', parseThermalGenerationGNL, False, False),  #? # DGNL 
    }

# TITLE = 1
# SUBSYSTEM = 2
# RESERVOIR = 3
# THERMAL = 4
# PUMP_STATIONS = 5 # NOT USED
# LOAD = 6
# DEFICIT = 7
# SPECIAL_BASINS = 8 # NOT USED
# SMALL_PLANT = 9
# ITAIPU_REST = 10  # MANUAL IS DIFFERENT FROM DECK FILE
# EXCHANGE_LIMIT = 11
# STAIR_RESTRICTIONS = 12 # NOT USED
# DISCOUNT_RATE = 13
# CONVERGENCE_TOL = 14
# TOTAL_ITER = 15
# PL_ALGO = 16 # NOT USED
# REF_DATE = 17
# HYDRO_MAINT = 18
# THERMAL_MAINT = 19
# DISPONIBILITY_FACTOR = 20
# FLOOD_VOLUME = 21
# FILL_RATE = 22 # NOT USED
# ELECTRIC_REST = 23
# TRAVEL_TIME = 24
# REGISTRY_MODIF = 25

# OP_REV = 26 # NOT USED
# HYDRO_PRODF = 27 # NOT USED
# OUTPUT_REPORT = 28
# IMPEXP_CONTRACT = 29
# STUDY_CONT = 30 # NOT USED
# FUTURE_COSTDEF = 31
# IRRIG_RATE = 32
# HISTORIC_OUTFLOW = 33
# STORED_ENERGY = 34
# VOLUME_REST = 35
# OUTFLOW_REST = 36


def parseArgs(blocks):

    parseable = []
    parameters = []
    toParse = []

    parser = argparse.ArgumentParser(
        description='Extract information from DECOMP decks.')

    for block in blocks:
        if blocks[block] != None:
            parseable.append(block)
            if blocks[block].isParam == False:
                parser.add_argument(blocks[block].argname, dest='toParse', action='append_const',
                                    const=[block])
            else:
                parameters.append(block)

    parser.add_argument('-parameters', dest='toParse', action='append_const',
                        const=parameters)
            
    parser.add_argument('-dger', '-dr', metavar='F', type=str, nargs=1,
                        help='The deck\'s DGER file.', required = False)

    parser.add_argument('-dgnl', '-dl', metavar='F', type=str, nargs=1,
                        help='The deck\'s DGNL file.', required = False)

    args = parser.parse_args()

    #Deixar ativo caso queira os args
    # args.dger = args.dger[0]
    # args.dgnl = args.dgnl[0]


    if args.toParse == None:
        args.toParse = parseable
    else:
        for argslist in args.toParse:
            toParse.extend(argslist)

        args.toParse = toParse


    selectedParameters = True

    for val in parameters:
        if not val in args.toParse:
            selectedParameters = False
            break

    args.parameters = selectedParameters

    return args


def getRangeFromList(content, ranges, var):
    return content[ranges[var][0]:ranges[var][1]]


def findRanges(allContent, length, offset):
    ranges = {}
    for i in range(1, 1+length):
        start = allContent.find('BLOCO {}'.format(i))
        end = allContent.find('BLOCO {}'.format(i+1))

        if end == -1:
            end = len(allContent)
        ranges[offset + i] = [start, end]

    if 20 in ranges and ranges[20][0] == -1:
        ranges[20][0] = allContent.find('REGISTRO FD')+11

    if 32 in ranges and ranges[32][0] == -1:
        ranges[32][0] = allContent.find('TAXA DE IRRIGACAO')+17

    return ranges

#Não esta sendo utilizado, pois não esta sendo gerado um csv
# def writeFile(prefix, filename, header, data ):
#     if len(data) == 0:
#         print('Empty', filename)
#         return

#     with open(prefix + '_' + filename, 'w') as f:
#         f.write(';'.join(header) + '\n')

#         for row in data:
#             f.write(';'.join(map(str, row)) + '\n')

def readFile(path):
    retval = ''
    with open(path,'r',encoding='latin1') as f:
        retval = f.read()
    return retval

#Main da aplicação, onde irá rodar as funções
if __name__ == "__main__":

    #Baixa os arquivos de decomp do mes atual do sistema e salva na pasta temporaria tempDecomp
    download_decomp()

    blocks = setupBlocks()

    args = parseArgs(blocks)
 
    #Indica onde está os arquivos baixados do mes
    pathdeck = '../decomp-entrada-Servidor/tempDecomp'

    #Faz a operação de upload dos dados de saida do decomp do mes atual
    upload_data_deckOut()

    #Procura pelos arquivos por essa lógica e faz a mesma operação da funcao "upload_data_deckout" mas para arquivos de entrada
    for root, directories, files in os.walk(pathdeck, topdown=False):
            for name in directories:
                if 'sem' in name:
                    relatory = pathdeck + '/' + name
                    files = os.listdir(relatory)
                    for f in files:
                        if 'DADGNL' in f:
                            print(relatory + '/' + f[7:])

                            contentDger = readFile(relatory + '/DADGER.' + f[7:])
                            contentDgnl = readFile(relatory + '/DADGNL.' + f[7:])
                            
                            dgerRanges = findRanges(contentDger,36,0)
                            dgnlRanges = findRanges(contentDgnl,4,36)

                            params = {}

                            params.update(parseRefDate(getRangeFromList(contentDger,dgerRanges,REF_DATE)))

                            #Data do estudo
                            refDate = str(parseRefDate(contentDger).get('referenceDate'))[:10]

                            for block in args.toParse:

                                if blocks[block] == None:
                                    continue

                                result = None
                                if blocks[block].isDger:
                                    #Pega as informações do decomp na parte do DADGER
                                    result = blocks[block].parseFunc(getRangeFromList(contentDger,dgerRanges,block))
                                else:
                                    #Pega as informações do decomp na parte do DADGNL
                                    result = blocks[block].parseFunc(getRangeFromList(contentDgnl,dgnlRanges,block))

                                if result == None:
                                    continue
                                
                                if blocks[block].isParam:
                                    params.update( result )
                                else:
                                    for info in result:
                                        #Tratar essas variaveis para inputar na função sendToDb
                                        table = 'dec_in_' + info[0][:-4]
                                        columns = info[1]
                                        columns.append('deck_date')
                                        data = info[2]

                                        new_data = []
                                        none_data = []

                                        #Tratar valores vazios para None
                                        for row in data:
                                            tempDecomp = [x if x != '' else None for x in row]
                                            tempDecomp.append(refDate)
                                            new_data.append(tempDecomp)

                                        #Se tiver tamanho upar normal no banco
                                        if len(new_data) != 0:
                                            # print(columns)
                                            # print(new_data)
                                            sendToDb(columns, new_data, table)
                                            print("Tabela ok:" + table)
                                            
                                        #Upar Vazio caso não venha nada
                                        else:
                                            algs = []
                                            for row in range(len(columns) - 1):
                                                algs.append(None)
                                            algs.append(refDate)
                                            none_data.append(algs)

                                            sendToDb(columns, none_data, table)
                                            print("Tabela vazia:" + table)
                            
                            # Parte para pegar os parametros do DADGER e upar no banco
                            paramToWrite = []
                            paramColumns = ['te', 'tx', 'gp', 'ni', 'deck_date']
                            paramTable = 'dec_parameters'
                            for info in params:
                                paramToWrite.append(params[info])

                            # del paramToWrite[0], paramToWrite[-1]
                            paramToWrite.append(refDate)
                            # print(paramToWrite)
                            # sendToDb(paramColumns, [paramToWrite], paramTable)
    
    #Apaga a pasta tempDecomp
    shutil.rmtree('./tempDecomp')