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
        menu()
        comando = input("Insira um comando: ").split(" ")
        if lista_players[0]["Nome"] == []: 
            while comando[0].lower() != "rj"  and comando[0].lower() != "l" :
                if comando[0].lower() == "ej":
                    os.system("cls")
                    print("Não pode eliminar jogadores sem antes os registar...")
                    apagar(2) 
                elif comando[0].lower() == "lj":
                    os.system("cls")
                    print("Não pode listar jogadores sem antes os registar...")
                    apagar(2) 
                elif comando[0].lower() == "ij":
                    os.system("cls")
                    print("Não pode iniciar jogadores enquanto não tiver jogadores registados...")
                    apagar(2)  
                elif comando[0].lower() == "dj":
                    os.system("cls")
                    print("Não pode listar jogadores sem antes os registar...")
                    apagar(2)   
                elif comando[0].lower() == "d":
                    os.system("cls")
                    print("Não pode desistir ter começado o jogo (não tem jogadores registados)")
                    apagar(2)   
                elif comando[0].lower() == "cp":
                    os.system("cls")
                    print("Não pode colocar peça sem ter começado o jogo (não tem jogadores registados)")
                    apagar(2)  
                elif comando[0].lower() == "v":
                    os.system("cls")
                    print("Não pode visualizar resultado sem ter jogadores registados...")
                    apagar(2)
                elif comando[0].lower() == "dj":
                    os.system("cls")
                    print("Não pode ver detalhes de jogo sem antes ter iniciado jogo...")
                    apagar(2)
                elif comando[0].lower() == "dj":
                    os.system("cls")
                    print("Não existe progresso para ser guardado...")
                    apagar(2)    
                else:
                    os.system("cls")       
            if comando[0].lower() == "rj":
                if len(comando) != 2:
                        os.system("cls")
                else:
                    os.system("cls")
                    registar_jogadores(comando, jogos, vitorias, nome)
                    print("Jogador registado com sucesso.")
                    apagar(2)
            elif comando[0].lower() == "l":
                #carregar ficheiro load (Ainda não aprendemos)
                pass
        else:
            if comando[0].lower() == "rj":
                if len(comando) != 2:
                        os.system("cls")
                else:
                    verif = detetor_iguais(lista_players, comando)
                    if verif == True:
                       os.system("cls")
                       print("Já existe um jogador com esse nome...")
                       apagar(2)
                    else:
                        os.system("cls")
                        registar_jogadores(comando, jogos, vitorias, nome)
                        print("Jogador registado com sucesso.")
                        apagar(2)
            elif comando[0].lower() == "lj":
                table = tabela(assuntos, nome, lista_players)
                print(table)
        






