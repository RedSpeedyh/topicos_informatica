import os
os.system('cls')

"""Tratamento de Exceções"""

vet = "12X45"
for i in range (0,6):

    try:
        print("Quadrado: %d" %(int(vet[i])**2))
    except ValueError:
        print("Valor inválido na posição: %d" %i)
    except IndexError:
        print("índice %d maior que o tamanho do vetor" %i)