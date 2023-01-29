from requests import get
import Info_times as info

GAMES_URL = "https://www.balldontlie.io/api/v1//games?per_page=100&seasons[]=2022&team_ids[]="
'''
for i in range(30):
    a = (GAMES_URL+f'{i+1}')
    print(a)
    response = get(a).json()
    for i in range(25):
        print(response['data'][i]['home_team']['name'],'|', response['data'][i]['home_team']['id'] )'''


def get_resultadosJogos(nome):
    teste = []
    for time in range(1, 8):#31
        #print(time,': ****************************************************************************************************************')
        timesH = []
        timesV = []
        winrateH = []
        empate = []
        winrateV = []
        cont = -1
        print(time)
     
        for partida in range(1, 2):#82 
            print(time, '|', partida)
            response = get(GAMES_URL + f"{time}").json()   
            path =   response['data']
            cont += 1
            timesH.append(path[partida]['home_team']['name'])
            timesV.append(path[partida]['visitor_team']['name'])
            teste.append(path[partida]['visitor_team']['name'])
            winrateH.append(0)
            empate.append(0)
            winrateV.append(0)

            if timesH[cont] == nome:
                    '''print("\nCASA: ", timesH[cont], '||',
                        "VISITANTE: ", timesV[cont], )
                    print("SCORE CASA: ",  path[partida]['home_team_score'],
                        " X SCORE VISITANTES: ", path[partida]['visitor_team_score'])'''
                    if path[partida]['home_team_score'] > path[partida]['visitor_team_score']:
                        #print('Vencedor: ', timesH[cont])
                        if  timesV[cont] == teste[time] :
                            winrateH[time] += 1
                            print('winrate do time', timesH[cont], 'ganhou do',timesV[cont],'=', winrateH[time])

                        '''elif partida['home_team_score'] == i['visitor_team_score']:
                        print('EMPATE: ', timesH[cont], 'X', timesV[cont])
                        if  timesV[cont] == teste[time] :
                            print(len(timesV))
                            empate[time] += 1
                            print('winrate do time', timesH[cont], 'empatou com',timesV[cont],'=', empate[time])

                    else:
                        print('Vencedor: ', timesV[cont])
                        if  timesV[cont] == teste[time] :
                            print(len(timesV))
                            winrateV[time] += 1
                            print('winrate do time', timesH[cont], 'perdeu do',timesV[cont],'=', winrateV[time])'''

            elif timesV[cont] == nome:
                    '''print("\nVISITANTE: ", timesV[cont],
                        '||', "CASA: ", timesH[cont], )
                    print("SCORE VISITANTE: ",
                        path[partida]['visitor_team_score'], " X SCORE CASA: ", path[partida]['home_team_score'])'''
                    if path[partida]['visitor_team_score'] > path[partida]['home_team_score']:
                        #print('Vencedor: ', timesV[cont])
                        if  timesH[cont] == teste[time] :
                            winrateH[time] += 1
                            print('winrate do time', timesV[cont], 'ganhou do',timesH[cont],'=', winrateH[time])

                    '''elif i['home_team_score'] == i['visitor_team_score']:
                        print('EMPATE: ', timesH[cont], 'x', timesV[cont])
                        empate[time] += 1
                        print('winrate do time', timesH[cont], 'empatou do',timesV[cont],'=', empate[time])

                    else:
                        print('Vencedor: ', timesH[cont])
                        winrateV[time] += 1
                        print('winrate do time', timesH[cont], 'ganhou do',timesV[cont],'=', winrateV[time])'''
            
            
            
