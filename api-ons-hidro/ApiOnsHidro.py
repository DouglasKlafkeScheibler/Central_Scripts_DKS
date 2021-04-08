import requests, json, math
import datetime
from ApiHidroAutent import autent, autentRefresh
from ApiHidroReservoirs import api_reservoirs_data
from ApiHidroReservoirsId import api_reservoirs_id

import sys
sys.path.append('../config')
from sendDb import sendToDb

#Esse Script tem como função Adquirir as informações da API de hidrologia sendo elas todas as informações de Reservatórios e exportar todos esses
#dados coletados para a base de dados da Central.


#Os end-points que serão coletados na parte de reservatórios
variables = [
    'afluencia',
    'defluencia',
    'energiaTurbinavel',
    'nivelJusante',
    'nivelMontante',
    'vazaoOutrasEstruturas',
    'vazaoTurbinada',
    'vazaoVertida',
    'volumeUtil'
]

columns = [
    'identifier',
    'Value',
    'Instant'
]

if __name__ == "__main__":

    # pega o token da api
    token = autent()

    # Pega reservoirs_id da api, porem se não trocar os reservatórios usar as estáticas que estão abaixo
    #Reservátorios estáticos
    reservoirs_id = [
        'IGSSAN', 'PPUHMU', 'GRAGVL', 'PNUCB4', 'DCAIMO', 'IGSEG1', 'JIUHMC', 'JIUHQJ', 'PBILH1', 'PBILHP', 'GRECUN', 'GRLIMO', 'PNCPB2', 
        'PRITAI', 'PRJUPI', 'PRPPRI', 'PNST', 'PNSV', 'PNUFRC', 'PPPJU'
    ]    

    #Para cada Reservatório ele irá fazer uma consuta na api
    for identifier in reservoirs_id:
        print('************************')
        print('Identificador: ' + identifier)

        for var in variables:

            table = 'dados_brutos.api_hidro_' + var
            print(table)
            reservoirs_search = api_reservoirs_data(token["access_token"], identifier, var, 1)
            numDados = reservoirs_search['QuantidadeTotalItens']

            #Como o máximo de paginas é 240, essa operação faz com que passemos por todos os dados em lotes de 240
            itera = math.ceil(numDados / 240)
        
            #Verifica cada página e upa até terminar todas as paginas, lembrando que o range max de uma página é 240 itens. 
            for pag in range(itera):
                reservoirs_data = api_reservoirs_data(token["access_token"], identifier, var, pag + 1)
                data_all = reservoirs_data['Resultados']

                data = []
                #Pega o valor que vem da api
                for data_moment in data_all:
                    date = datetime.datetime.strptime(data_moment['Instante'], "%d/%m/%Y %H:%M:%S").strftime("%Y-%m-%d")
                    data.append([identifier, data_moment['Valor'], date]) 

                #Manda pro banco com a função sendToDb
                sendToDb(columns, data, table)
                print("PAGINA:{} UPADA".format(pag + 1))