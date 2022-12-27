import os
import time
from prettytable import PrettyTable

def tabela(assuntos, nome, jogos, vitorias, lista_players):
    for i in range(len(nome)): 
        assuntos.add_row([lista_players[i]["Nome"], jogos[i], vitorias[i]])
    return assuntos

def registar_jogadores(comando, jogos, vitorias, nome):
    nome.append(comando[1])
    jogos.append(0)
    vitorias.append(0)

def retirar_jogadores:
    
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
    



