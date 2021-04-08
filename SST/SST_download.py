import pathlib
import os
import shutil
import urllib.request as request
from contextlib import closing
import netCDF4
from pandas.tseries.offsets import DateOffset
from datetime import datetime

from InterpolaSST_V1 import parse_data_sst
from SST2DB import insert_into_CPC_SST
archive_name = 'sst.mnmean.nc'

def download_sst():
    try:
        #Criar um diretório temporario
        dir = os.path.join('./tempSST')
        os.mkdir(dir)

        # baixar o arquivo da SST
        with closing(request.urlopen('ftp://ftp.cdc.noaa.gov/Datasets/noaa.ersst.v5/sst.mnmean.nc')) as r:
            with open('./tempSST/' + archive_name, 'wb') as f:
                #Salva os arquivos
                shutil.copyfileobj(r, f)
    except e:
        print('Problema no download dos SST:')



# download_sst()


def sst_to_db():
    #LEITURA
    new_sst = netCDF4.Dataset('./tempSST/sst.mnmean.nc','r')
    old_sst = netCDF4.Dataset('./consolidatedSST/sst.mnmean.nc','r')

    new_sst_date = new_sst.data_modified
    old_sst_date = old_sst.data_modified

    print(new_sst_date,old_sst_date)
    #Verificar se tem alteração no arquivo
    if(new_sst_date != old_sst_date):
        #Logica para colocar ultimos arquivos
        
        #Monta os dados do sst a partir do arquivo baixado 
        # new_sst_month = new_sst_date[5:7]
        new_sst_month = "03"
        sst_data = parse_data_sst(new_sst,new_sst_month)
        print(sst_data)

        #Função de inserção dos dados, Inserir apenas o ultimo mes
        # insert_into_CPC_SST(sst_data)
        
        #Ao final substituir arquivo para o local de consolidado
        # shutil.copyfileobj(new_sst, old_sst)

        #Excluir SST temporario
        new_sst.close()
        # shutil.rmtree('./tempSST')

    else:
        print('Sem alterações no arquivo')

# download_sst()
sst_to_db()