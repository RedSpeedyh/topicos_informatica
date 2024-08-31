import os
os.system('cls')

"""Funções"""

def limpar_tela():
    os.system('cls')

def ler_numero():
    return int(input("Informe um valor: "))

def soma(n1, n2):
    return n1+n2

def main():
    limpar_tela()
    n1 = ler_numero()
    n2 = ler_numero()
    print(soma(n1,n2))

main()

def exibir_intervalo(ini=0, fim=10, passo=1):
    for item in range(ini, fim, passo):
        print(item)

exibir_intervalo(1,6,2)
exibir_intervalo(fim = 5, passo = 2)

