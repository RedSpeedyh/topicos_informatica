import os
os.system('cls')

"""Tratamento de Exceções"""

"""• Exercício 1
- Elabore uma aplicação que receba o peso e altura
de um número indeterminado de pessoas.
- Utilize tratamento de exceção para garantir que os
valores informados são válidos.
- Após a entrada correta dos dados apresente o
IMC.
- Para cada entrada de dados pergunte ao usuário
“Deseja continuar?”
"""

def limpar_tela():
    os.system('cls')

def weight():
    return int(input("Informe o seu peso: "))

def height():
    return float(input("Informe o sua altura: "))

def imc(peso, altura):
    return peso/(altura**2)

def continuidade():
    return print(input("Deseja continuar?"))


def main():
    limpar_tela()
    peso = weight()
    altura = height()
    print(imc(peso, altura))

main()

"incompleto"


