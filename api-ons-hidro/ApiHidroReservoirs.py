import requests


#Essa função tem como objetivo acessar diversos endPoints e conseguir setar as datas que desejam ser requisitadas
def api_reservoirs_data(token, identifier, variable, pagina, init = "1999-01-30 00:00:00", final = "2020-12-30 00:00:00", intervalo = "DI", origem = "TRL"):
    """
    :param token: codigo de autenticacao obtido na função de autenticaçoo da api
    :return: retorna dict com identificador e nome curto dos reservatórios disponíveis
    """
    # api-endpoint 
    URL = "https://apis.ons.org.br/hidrologia/v1/reservatorios/{}/{}".format(identifier, variable)

    query={
        'Inicio': init,
        'Fim': final,
        'Intervalo': intervalo,
        'Origem': origem
    }
    
    headers = {'accept': 'application/json',
               'Pagina': str(pagina),
               'Quantidade':'240',
               'Authorization': token,
              }


    # sending get request and saving the response as response object 
    r = requests.get(url = URL, headers = headers, params = query) 

    # extracting data in json format 
    data = r.json()
    return data

