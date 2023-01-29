import API_nba as API


def get_abreviacoes():
    retorno = []
    for abreviacao in API.get_times():
        retorno.append(abreviacao['abbreviation'])
    return retorno
        
def get_cidades():
    retorno = []
    for cidade in API.get_times():
        retorno.append(cidade['city'])
    return retorno
             
def get_conferencia():
    retorno = []
    for conferencia in API.get_times():
        retorno.append(conferencia['conference'])
    return retorno
        
def get_divicao():
    retorno = []
    for divisao in API.get_times():
        retorno.append(divisao['division'])
    return retorno
        
def get_nomeCompleto():
    retorno = []
    for nomeCompleto in API.get_times():
        retorno.append(nomeCompleto['full_name'])
    return retorno
    
def get_nome():
    retorno = []
    for nome in API.get_times():
        retorno.append(nome['name'])
    return retorno

def informacaoTime(indice):
    info = API.get_times()
    info_nomeCompleto = info[indice]['full_name']
    info_nome = info[indice]['name']
    info_abreviacao = info[indice]['abbreviation']
    info_cidade = info[indice]['city']
    info_conferencia = info[indice]['conference']
    info_divisao = info[indice]['division']
    query = (f"NOME COMPLETO: {info_nomeCompleto}\nNOME: {info_nome}\nABREVIAÇAO: {info_abreviacao}\nCIDADE: {info_cidade}\nCONFERENCIA: {info_conferencia}\nDIVISAO:{ info_divisao}")
    return query

#print(get_abreviacoes(), '|\n\n', get_cidades(), '|\n\n', get_conferencia(), '|\n\n', get_divicao(), '|\n\n', get_nomeCompleto(), '|\n\n', get_nome())

