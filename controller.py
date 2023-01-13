import os
import time
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

def eliminar_jogador(nome: list, comando: list):
    if comando[1] in nome:
        nome.remove(comando[1])
        return True
    else:
        return False




