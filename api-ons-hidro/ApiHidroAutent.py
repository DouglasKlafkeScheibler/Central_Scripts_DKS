import requests
import json
import sys

#Esse script tem como função fazer uma requisição na API da ons de hidrologia e retornar um token para podermos fazer outras operações

#Lembrando que os dados para o login e senha estão no arquivo "login.json"


login = '/Users/dougl/Desktop/Scripts-DouglasKS/config/loginApiOnsHidro.json'

#Acha a pasta que contem as informações de login
def parseLogin(path):

    result = None
    with open(path,'r') as f:
        result = json.loads(f.read())

    return result['username'], result['password']


#Faz a requisição e retorna o token
def autent():

    username, password = parseLogin(login)

    """
    :param username: Login sintegre (ons)
    :param password: Senha sintegre (ons)
    :return: retorna token de autenticação API
    """
    token ={}
    
    #AUTENTICACAO HIDROLOGIA
    url = "https://apis.ons.org.br/hidrologia/v1/autenticar"
    payload = {
        "usuario": username, "senha": password
    }
    headers = {
        'content-type': 'application/json',
        'accept':'application/json'
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()

    return data


#Renova o token
def autentRefresh(token):
    
    url = "https://apis.ons.org.br/hidrologia/v1/renovar"
    payload = {
        "refresh_token": token
    }
    
    headers = {
        'content-type': 'application/json',
        'accept':'application/json'
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()

    return data
