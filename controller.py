import os
import time
from prettytable import PrettyTable

def tabela(assuntos : PrettyTable, nome , jogos, vitorias : list):
    for i in range(len(nome)): 
        assuntos.add_row(nome[i], jogos[i], vitorias[i])
        return assuntos


def registar_jogadores(comando: list, jogos: list, vitorias: list, nome: list):
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

def detetor_iguais(nome: list, comando: list):
    for i in range(len(nome)):
        if nome[i] == comando[1]:
            igual = True
        else:
            igual = False

def eliminar_jogador(i, nome: list, comando: list):
    for i in range (len(nome[i])):
        if nome[i] == comando[1]:
            del nome[i]




