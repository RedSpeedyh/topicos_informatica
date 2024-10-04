import os
os.system('cls')

"""Escreva um programa Python para
manipulação de datas e apresente na tela:
- Data atual
- Ano atual
- Mês atual
- Dia atual
- Data atual formatada dia/mês/ano
 Data atual no formato:
      dia de mês_por_extenso de ano
"""

from datetime import datetime

# Obtendo a data atual
data_atual = datetime.now()

# Extraindo ano, mês e dia
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day

# Formatando a data
data_formatada = data_atual.strftime("%d/%m/%Y")
data_extenso = data_atual.strftime(f"{dia_atual} de {data_atual.strftime('%B')} de {ano_atual}")

# Exibindo as informações
print(f"Data atual: {data_atual}")
print(f"Ano atual: {ano_atual}")
print(f"Mês atual: {mes_atual}")
print(f"Dia atual: {dia_atual}")
print(f"Data atual formatada (dia/mês/ano): {data_formatada}")
print(f"Data atual no formato: {data_extenso}")