import Info_times as TM
import Info_estatisticas as IE

import API_nba as API

while True:
    menu =int(input('[1] Times | [2] Estatisticas dos Jogos | [3] jogos ao vivo = '))
    
    if(menu == 1):
        print('\n { Voce esta na seçao de times::') 
        menu =int(input('[1] buscar infos por times especificos | [2] Todos os detalhes } = '))
        
        if(menu == 1):
            print('ID DOS TIME:')
            for lista in API.get_times():
                print(f"[{lista['id']-1} {lista['name']}], ", end="")
            
            print('\n')
            
            ID_TIME = int(input('Digite o ID do time a buscar: '))
            print('========================================================================')
            print(TM.informacaoTime(ID_TIME))
            print('========================================================================')
         
        elif(menu == 2):
            menu =int(input('[1] TODOS os nome completos  | [2] TODAS as abreviaçoes } = '))
            
            if(menu == 1):
                print('\n========================================================================')
                print(TM.get_nomeCompleto())
                print('========================================================================')  
                 
            elif(menu == 2):
                print('\n========================================================================')
                print(TM.get_abreviacoes())
                print('========================================================================')
                
    elif(menu == 2):
        NOME_TIME = str(input('Digite o NOME do time a buscar: '))
        print('========================================================================')
        print(IE.get_resultadosJogos(NOME_TIME))
        print('========================================================================')
    print('end...')
        
