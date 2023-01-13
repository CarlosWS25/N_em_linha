from controller import *
def main():
    
    #Variaveis
    nome = []
    jogos = []
    vitorias = []
    assuntos = PrettyTable()
    assuntos.field_names = ["Nome", "Jogos", "Vitórias"]
    lista_players = [{"Nome" : nome} , {"Jogos" : jogos} , {"Vitórias" : vitorias}]
    lista_in_game = []  
    game_start = False

    #main
    os.system("cls")
    print(
"""
███╗   ██╗    ███████╗███╗   ███╗    ██╗     ██╗███╗   ██╗██╗  ██╗ █████╗ 
████╗  ██║    ██╔════╝████╗ ████║    ██║     ██║████╗  ██║██║  ██║██╔══██╗
██╔██╗ ██║    █████╗  ██╔████╔██║    ██║     ██║██╔██╗ ██║███████║███████║
██║╚██╗██║    ██╔══╝  ██║╚██╔╝██║    ██║     ██║██║╚██╗██║██╔══██║██╔══██║
██║ ╚████║    ███████╗██║ ╚═╝ ██║    ███████╗██║██║ ╚████║██║  ██║██║  ██║
╚═╝  ╚═══╝    ╚══════╝╚═╝     ╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                          
                           Jogo realizado por:                                                        
                            Carlos Rodrigues
                             Duarte Eusébio
                           João Pedro Andrade
""")
    apagar(3)
    while True:
        print(
"""
╔═══════════════════════════════════════════════════╗
║         Insira um dos seguintes comandos:         ║
╠═══════════════════════════════════════════════════╣
║            [RJ Nome] - Registar Jogador           ║
║            [EJ Nome] - Eliminar Jogador           ║ 
║              [LJ] - Listar Jogadores              ║
║                [IJ] - Iniciar Jogo                ║
║              [DJ] - Detalhes do Jogo              ║
║                [D Nome]- Desistir                 ║
║          [CP Nome Posição] - Colocar Peça         ║
║            [V] - Visualizar Resultado             ║
║             [G NomeFicheiro] - Gravar             ║
║              [L NomeFicheiro] - Ler               ║
╚═══════════════════════════════════════════════════╝
""")
        comando = input("Insira um comando: ").split(" ")
        if lista_players[0]["Nome"] == []: 
            while comando[0].lower() != "rj" and comando[0].lower() != "l" :
                if comando[0].lower() == "ej":
                    os.system("cls")
                    print("Não pode eliminar jogadores sem antes os registar...")
                    apagar(2)
                    break
                elif comando[0].lower() == "lj":
                    os.system("cls")
                    print("Não pode listar jogadores sem antes os registar...")
                    apagar(2)
                    break
                elif comando[0].lower() == "ij":
                    os.system("cls")
                    print("Não pode iniciar jogadores enquanto não tiver jogadores registados...")
                    apagar(2)  
                    break
                elif comando[0].lower() == "dj":
                    os.system("cls")
                    print("Não pode ver os detalhes do jogo sem antes o iniciar")
                    apagar(2)
                    break 
                elif comando[0].lower() == "d":
                    os.system("cls")
                    print("Não pode desistir ter começado o jogo (não tem jogadores registados)")
                    apagar(2)
                    break   
                elif comando[0].lower() == "cp":
                    os.system("cls")
                    print("Não pode colocar peça sem ter começado o jogo (não tem jogadores registados)")
                    apagar(2)
                    break  
                elif comando[0].lower() == "v":
                    os.system("cls")
                    print("Não pode visualizar resultado sem ter jogadores registados...")
                    apagar(2)
                    break
                elif comando[0].lower() == "g":
                    os.system("cls")
                    print("Não existe progresso para ser guardado...")
                    apagar(2)
                    break    
                else:
                    os.system("cls")
                    print("Instrução inválida.")
                    apagar(2)     
                    break  
            if comando[0].lower() == "rj":
                if len(comando) != 2:
                    os.system("cls")
                else:
                    verif = detetor_iguais(nome, comando)
                    if verif == True:
                        os.system("cls")
                        print("Já existe um jogador com esse nome...")                            
                        apagar(2)
                    else:
                        os.system("cls")
                        registar_jogadores(comando, jogos, vitorias, nome)
                        print("Jogador registado com sucesso.")
                        apagar(2)
            elif comando[0].lower() == "l":
                #carregar ficheiro load (Ainda não aprendemos)
                pass
        else:
            if game_start == True:
                while True:
                    if comando[0].lower() == "rj":
                        if len(comando) != 2:
                            os.system("cls")
                            break
                        else:
                            verif = detetor_iguais(nome, comando)
                        if verif == True:
                            os.system("cls")
                            print("Já existe um jogador com esse nome...")                            
                            apagar(2)
                            break
                        else:
                            os.system("cls")
                            registar_jogadores(comando, jogos, vitorias, nome)
                            print("Jogador registado com sucesso.")
                            apagar(2)
                            break
                    elif comando[0].lower() == "ej":
                        if len(comando) != 2:
                            os.system("cls")
                            break
                        else:
                            apagar_player = eliminar_jogador(nome, comando)
                            if apagar_player == True:
                                os.system("cls")
                                print("Jogador eliminado com sucesso!")
                                apagar(2)
                                break
                            else:
                                os.system("cls")
                                print("Jogador não existe!")
                                apagar(2)
                                break
                    elif comando[0].lower() == "lj":
                        os.system("cls")
                        table = tabela(assuntos, nome, jogos, vitorias)
                        print(table)
                        apagar(2)
                        break        
                    elif comando[0].lower() == "ij":
                        os.system("cls")
                        print("Já existe um jogo a decorrer!")
                        apagar(2)
                        break
                    elif comando[0].lower() == "dj":
                        print(
f"""
Nome dos jogadores: {lista_in_game[0]} e {lista_in_game[1]}
Comprimento: {comando_int[0]}
Altura: {comando_int[1]}
Quantidade de peças necessárias para vencer: {comando_int[2]}                      
""")
                        break
                    elif comando[0].lower() == "cp":
                        if len(comando) != 3:
                            os.system("cls")
                            print("Número de parametros inválido!")
                            apagar(2)
                        elif comando[1] not in lista_in_game:
                            os.system("cls")
                            print("Esse jogador não está a em jogo neste momento")
                            apagar(2)
                        elif comando[1] not in nome:
                            os.system("cls")
                            print("Esse jogador não existe...")
                            apagar(2)
                        elif not 0 < comando_int[2] <= comando_int[0]:
                            os.system("cls")
                            print(f"A jogada deve ser feita dentro dos limites do comprimento do tabuleiro (0-{comando_int[0]}.")
                            apagar(2)
                        else:
                            cair_peca(tabuleiro, comando_int)
                            print(tabuleiro)

                    elif comando[0].lower() == "v":
                        os.system("cls")
                        print(tabuleiro)
                        apagar(2)                        
                        break    
            else:                       
                while comando[0].lower() != "ij":
                    if comando[0].lower() == "rj":
                        if len(comando) != 2:
                            os.system("cls")
                            break
                        else:
                            verif = detetor_iguais(nome, comando)
                            if verif == True:
                                os.system("cls")
                                print("Já existe um jogador com esse nome...")                           
                                apagar(2)
                                break
                            else:
                                os.system("cls")
                                registar_jogadores(comando, jogos, vitorias, nome)
                                print("Jogador registado com sucesso.")
                                apagar(2)
                                break
                    elif comando[0].lower() == "lj":
                        os.system("cls")
                        table = tabela(assuntos, nome, jogos, vitorias)
                        print(table)
                        apagar(2)
                        break
                    elif comando[0].lower() == "ej":
                        if len(comando) != 2:
                            os.system("cls")
                            break
                        else:
                            apagar_player = eliminar_jogador(nome, comando)
                            if apagar_player == True:
                                os.system("cls")
                                print("Jogador eliminado com sucesso!")
                                apagar(2)
                                break
                            else:
                                os.system("cls")
                                print("Jogador não existe!")
                                apagar(2)
                                break
                    elif comando[0].lower() == "dj":
                        os.system("cls")
                        print("Não pode ver os detalhes do jogo sem antes o iniciar")
                        apagar(2)
                        break 
                    elif comando[0].lower() == "d":
                        os.system("cls")
                        print("Não pode desistir ter começado o jogo.")
                        apagar(2)
                        break                   
                    elif comando[0].lower() == "cp":
                        os.system("cls")
                        print("Não pode colocar peça sem ter começado o jogo.")
                        apagar(2)
                        break          
                    elif comando[0].lower() == "v":
                        os.system("cls")
                        print("Não existe jogo em curso.")
                        apagar(2)
                        break        
                    elif comando[0].lower() == "g":
                        pass
                        #fazer no fim
                    elif comando[0].lower() == "l":
                        pass
                        #carregar ficheiro load (Ainda não aprendemos)
                if comando[0].lower() == "ij":
                    if game_start == True:
                        os.system("cls")
                        print("Já existe um jogo a decorrer!")
                        apagar(2)
                    elif len(comando) != 3:
                        os.system("cls")
                        print("Apenas podem jogar 2 jogadores!")
                        apagar(2)
                    else:
                        verif_players = detetor_players(nome, comando)
                        if verif_players == True:
                            os.system("cls")
                            criar_lista_ingame(lista_in_game, bubblesort, comando)
                            while True:
                                comando = input(
    """
    ╔═══════════════════════════════════════════════════════╗
    ║   Insira os seguintes dados pela ordem apresentada:   ║
    ╠═══════════════════════════════════════════════════════╣
    ║ Comprimento (espaço) Altura (espaço) TamanhoSequência ║                        
    ╚═══════════════════════════════════════════════════════╝
    Comando: """).split(" ")
                                comando_int = list(map(int, comando))
                                if len(comando_int) != 3:
                                    os.system("cls")
                                    print("Número de parametros inválido!")
                                    apagar(2)
                                elif comando_int[0] < 0:
                                    os.system("cls")
                                    print("Comprimento da grelha tem de ser maior do que 0!")
                                    apagar(2)
                                elif not (comando_int[0] / 2) <= comando_int[1] <= comando_int[0]:
                                    os.system("cls")
                                    print(f"A altura da grelha deve estar compreendida entre {round(comando_int[0]/2)} e {comando_int[0]}.")
                                    apagar(2)
                                elif not 0 < comando_int[2] <= comando_int[0]:
                                    os.system("cls")
                                    print(f"O número de peças em linha para determinar a vitória tem de estar compreendido entre 0 e {comando_int[0]}.")
                                    apagar(2)
                                else:
                                    game_start = True
                                    bubblesort(nome)
                                    os.system("cls")                                
                                    tabuleiro = mesa_jogo(comando_int)
                                    print(f"Jogo iniciado entre {lista_in_game[0]} e {lista_in_game[1]}.")
                                    apagar(3)
                                    break           
                        else:
                            os.system("cls")
                            print("Os jogadores em questão não se encontram registados. (Sistema sensivel a maisculas)")
                            print(f"Lista de jogadores registados: {nome}")
                            apagar(3)
                    
                    



