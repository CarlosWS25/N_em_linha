from controller import *

#Variaveis
nome = []
jogos = []
vitorias = []
assuntos = PrettyTable()
assuntos.field_names = ["Nome", "Jogos", "Vitórias"]
lista_players = [{"Nome" : nome} , {"Jogos" : jogos} , {"Vitórias" : vitorias}]
#main
def main():
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
║  [CP TamanhoPeça Posição Sentido] - Colocar Peça  ║
║            [V] - Visualizar Resultado             ║
║             [G NomeFicheiro] - Gravar             ║
║              [L NomeFicheiro] - Ler               ║                    
╚═══════════════════════════════════════════════════╝
""")
        comando = input("Insira um comando: ").split(" ")
        if lista_players[0]["Nome"] == []: 
            while comando[0].lower() != "rj"  and comando[0].lower() != "l" :
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
                                






