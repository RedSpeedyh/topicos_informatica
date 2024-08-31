import os
os.system('cls')

"""Tratamento de Exceções"""

s = "aeiou"
try:
    print(s[5])
except IndexError as erro:
    print("O valor informado não é um número")
    print(erro)