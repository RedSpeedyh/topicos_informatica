import os
os.system('cls')

def exibir(lista = None):
    for item in lista:
        print(item)
        
    print("Tamanho = %d \n" %len(lista))
    
    lista = [5,2,4,3]
    lista.sort()
    lista.insert(0,1)
    lista.reverse()
    lista.remove(2)
    del lista[1]
    exibir(lista)