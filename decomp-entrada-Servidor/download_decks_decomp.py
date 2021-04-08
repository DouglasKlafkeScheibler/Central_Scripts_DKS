import pathlib
from datetime import datetime
import zipfile
from zipfile import ZipFile
import requests
import os
import shutil

# Exemple:DC202001
# archive_name = 'DC202102'
archive_name = 'DC' + datetime.now().strftime("%Y%m")

def download_decomp():
    try:
        #Criar um diretório temporario
        dir = os.path.join('./tempDecomp')
        os.mkdir(dir)

        # baixar o arquivo da CCEE
        url_origem = 'https://www.ccee.org.br/ccee/documentos/'+archive_name
        # url_origem = 'http://200.135.184.209/'+archive_name # para testes
        decomp_arq = requests.get(url_origem)

        # grava o arquivo no diretotio temporario
        with open('./tempDecomp/' + archive_name+'.zip','wb') as arq:
            for chunk in decomp_arq.iter_content(chunk_size=1024):
                arq.write(chunk)

        #Chama a função para descompactar os arquivos
        unzip_decomp_files()
    except:
        print('Problema no download dos decks')

def unzip_decomp_files():
    unzip_decomp = './tempDecomp/' + archive_name+'.zip'

    with ZipFile(unzip_decomp, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall('tempDecomp')

    for root, directories, files in os.walk('tempDecomp', topdown=False):
        for name in files:

            unzip_decomp_data = './tempDecomp/' + name

            #Extrai os arquivos
            with ZipFile(unzip_decomp_data) as zf:
                zf.extractall(name[:-3])
            
            #Move para a pasta tempDecomp
            shutil.move('./'+ name[:-3],'./tempDecomp')


if __name__ == "__main__":
    download_decomp()