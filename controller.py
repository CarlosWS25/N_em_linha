import os
import time
import json
import numpy as np
from prettytable import PrettyTable



def tabela(assuntos : PrettyTable, nome: list , jogos: list, vitorias: list):
    assuntos.clear_rows()
    for i in range(len(nome)): 
        assuntos.add_row([nome[i], jogos[i], vitorias[i]])
    return assuntos             

def registar_jogadores(comando: list, jogos: list, vitorias: list, nome: list):
    nome.append(comando[1])
    jogos.append(0)
    vitorias.append(0)
        
def apagar(i):
    time.sleep(i)
    os.system("cls")

def detetor_iguais(nome: list, comando: list):
    if comando[1] in nome:
        return True
    else:
        return False

def detetor_players(nome: list, comando: list):
    if comando[1] and comando[2] in nome:
        return True
    else:
        return False

def eliminar_jogador(nome: list, comando: list):
    if comando[1] in nome:
        nome.remove(comando[1])
        return True
    else:
        return False

def carregar_jogo(save):
    with open(save) as s:
        info = json.load(s)
    return info

def gravar_jogo(save, l):
    json_string = json.dumps(l)
    json_file = open(save, "w")
    json_file.write(json_string)
    json_file.close()

def mesa_jogo(comando_int : list):
    return np.full((comando_int[0], comando_int[1]), "_")

def bubblesort(nome):
    n = len(nome)
    for i in range(n):
        for j in range(0, n-i-1):
            if nome[j] > nome[j+1]:
                nome[j], nome[j+1] = nome[j+1], nome[j]
    return nome

def criar_lista_ingame(lista_in_game: list, bubblesort, comando: list):
    lista_in_game.clear()
    lista_in_game.append(comando[1])
    lista_in_game.append(comando[2])
    bubblesort(lista_in_game)

def cair_peca(tabuleiro, comando_int : list):
    for k in range(comando_int[1]-1, -1, -1):
        if tabuleiro([comando_int[0],k]) == "_":
            tabuleiro[comando_int[0],k] = "X"


