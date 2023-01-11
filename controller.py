import os
import time
from prettytable import PrettyTable

def tabela(assuntos : PrettyTable, nome : list, lista_players : list):
    for i in range(len(lista_players[0]["Nome"])): 
        assuntos.add_row([lista_players[0]["Nome"][i], lista_players[1]["Jogos"][i], lista_players[2]["Vitórias"][i]])
        return assuntos

def registar_jogadores(comando, jogos : list, vitorias : list, nome : list):
    if len(comando) != 2:
        os.system("cls")
        menu()
        comando = input("Insira um comando: ").split(" ")
    else:    
        nome.append(comando[1])
        jogos.append(0)
        vitorias.append(0)

def registar_jogadores(comando, jogos, vitorias, nome):
    nome.append(comando[1])
    jogos.append(0)
    vitorias.append(0)
    

def menu():
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
║   CP TamanhoPeça Posição Sentido] - Colocar Peça  ║
║            [V] - Visualizar Resultado             ║
║             [G NomeFicheiro] - Gravar             ║
║              [L NomeFicheiro] - Ler               ║                    
╚═══════════════════════════════════════════════════╝
""")
    
def apagar(i):
    time.sleep(i)
    os.system("cls")

def detetor_iguais(lista_players, comando):
    for i in range(len(lista_players[0]["Nome"])):
        if lista_players[0]["Nome"][i] == comando[1]:
            igual = True
        else:
            igual = False
    return igual
