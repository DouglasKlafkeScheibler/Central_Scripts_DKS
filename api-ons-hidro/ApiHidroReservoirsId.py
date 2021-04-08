import requests


#Essa função tem como objetivo consultar o id e o nome curto dos reservatórios
def api_reservoirs_id(token, pagina = 1):
    """
    :param token: codigo de autenticacao obtido na função de autenticaçoo da api
    :return: retorna dict com identificador e nome curto dos reservatórios disponíveis
    """
    # api-endpoint 
    URL = "https://apis.ons.org.br/hidrologia/v1/reservatorios"

    headers = {'accept': 'application/json',
               'Pagina': str(pagina),
               'Quantidade':'240',
               'Authorization': token,
              }

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, headers=headers) 

    # extracting data in json format 
    reservoirs = r.json()
    return reservoirs