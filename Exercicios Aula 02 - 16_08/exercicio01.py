import os
os.system('cls')
"""- Elabore uma aplicação que receba o nome de um produto
e o seu valor. O desconto deve ser calculado de acordo
com o valor fornecido conforme a Tabela.
- Apresente em tela o nome do produto, valor original do
produto e o novo valor depois de ser realizado o desconto.
Caso o valor digitado seja menor que zero, deve ser
emitida uma mensagem de aviso."""

"""
Valor (R$)          Desconto(R$)
>= 50 e <200            5
>=200 e <500            6
>=500 e <1000           7
>=1000                  8
"""

nome = input("Entre com o produto: ")
valor = float(input("Entre com o valor: "))

if valor>=0:
    if valor >=50 and valor <200:
        desconto = 0.95
    elif valor >=200 and valor <500:
        desconto = 0.94
    elif valor >=500 and valor <1000:
        desconto = 0.97
    elif valor >=1000:
        desconto = 0.92

print (f"Nome: {nome}")
print (f"Valor: {round (valor, 2)}")
print (f"Valor com desconto: {round (valor*desconto, 2)}")

