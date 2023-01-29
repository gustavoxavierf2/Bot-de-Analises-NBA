from requests import get
import json
#GAMES_URL = "https://www.balldontlie.io/api/v1//games?per_page=100&seasons[]=2022&team_ids[]="

'''for time in range(1, 3):#31
    arq = open(f'requests/teste{time}.json', 'w')
    for partida in range(1, 10):#82 
        print(time, '|', partida)
        json = str(get(GAMES_URL + f"{time}").json())
        format = json.replace("'", '"')
        format = format.replace("False", 'false')
        format = format.replace("None", 'null')
        arq.write(format)'''
with open('teste1.json', 'r', encoding='utf-8') as arq:
    obj = json.load(arq)
    a = obj.keys()
'''for time in range(1, 31):#31
    cont = -1
    
    for partida in range(1, 82):#82 
        print(time, '|', partida)
        response = obj
        path =   response['data']
        cont += 1
        print(path[partida]['home_team']['name'])
        print(path[partida]['visitor_team']['name'])
        print(path[partida]['visitor_team']['name'])'''
