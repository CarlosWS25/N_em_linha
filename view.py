from controller import *

#Variaveis
nome = []
jogos = []
vitorias = []
assuntos = PrettyTable(["Nome", "Jogos", "Vitórias"])
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
    time.sleep(3)
    os.system("cls")
    comando = input("Insira um comando: ").split(" ")
    while True:
        menu()
        if len(comando) != 2:
            os.system("cls")
            menu()
            comando = input("Insira um comando: ").split(" ")    
        else:
            while comando[0].lower() != "rj" and comando[0].lower() != "dj" and comando[0].lower() != "g" and comando[0].lower() != "l" :
                if comando[0].lower() == "ej":
                    os.system("cls")
                    print("Não pode eliminar jogadores sem antes os registar...")
                    time.sleep(2)
                    os.system("cls")
                    menu()
                    comando = input("Insira um comando: ").split(" ")   
                elif comando[0].lower() == "lj":
                    os.system("cls")
                    print("Não pode listar jogadores sem antes os registar...")
                    time.sleep(2)
                    os.system("cls")
                    menu()
                    comando = input("Insira um comando: ").split(" ")   
                elif comando[0].lower() == "ij":
                    os.system("cls")
                    print("Não pode iniciar jogadores enquanto não tiver jogadores registados...")
                    time.sleep(2)
                    os.system("cls")
                    menu()
                    comando = input("Insira um comando: ").split(" ")   
                elif comando[0].lower() == "dj":
                    os.system("cls")
                    print("Não pode listar jogadores sem antes os registar...")
                    time.sleep(2)
                    os.system("cls")
                    menu()
                    comando = input("Insira um comando: ").split(" ")   
                elif comando[0].lower() == "d":
                    os.system("cls")
                    print("Não pode desistir ter começado o jogo (não tem jogadores registados)")
                    time.sleep(2)
                    os.system("cls")
                    menu()
                    comando = input("Insira um comando: ").split(" ")   
                elif comando[0].lower() == "cp":
                    os.system("cls")
                    print("Não pode colocar peça sem ter começado o jogo (não tem jogadores registados)")
                    time.sleep(2)
                    os.system("cls")
                    menu()
                    comando = input("Insira um comando: ").split(" ")   
                elif comando[0].lower() == "v":
                    os.system("cls")
                    print("Não pode visualizar resultado sem ter jogadores registados...")
                    time.sleep(2)
                    os.system("cls")
                    menu()
                    comando = input("Insira um comando: ").split(" ")   
                else:
                    os.system("cls")
                    menu()
                    comando = input("Insira um comando: ").split(" ")
            if comando[0].lower() == "rj":
                registar_jogadores(comando, jogos, vitorias, nome)   
                print(lista_players)
                break
                
            



