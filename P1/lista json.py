import os
os.system('cls')

"""Contextualização
Uma empresa do ramo de varejo de alimentos precisa de um sistema computacional para gerenciar o
estoque dos seus produtos. Um produto é definido pelas seguintes características: código, nome, valor de compra, valor de venda e quantidade em estoque. Baseado neste contexto, construa uma aplicação Python capaz de:

1. Apresentar para o usuário um menu contendo as seguintes opções:

Varejão do João
[1] Cadastrar de produto
[2] Relatório de produtos
[3] Relatório de Estoque Baixo
[4] Exportar dados
[0] Sair

A execução da aplicação é finalizada quando a opção 0 (zero) é escolhida.

2. Implementar a opção Cadastrar Produto que permite ao usuário informar o nome do produto, o valor de compra e a quantidade em estoque.

     • O código deve ser gerado de maneira incremental a partir de 1 (um).
     • O valor de venda é calculado automaticamente, acrescendo 25% no valor de compra.

3. Escrever uma função que apresente na tela o Relatório de Produtos ordenados pelo nome do produto.
Este relatório deve apresentar todas as informações dos produtos: {código, nome, valor compra, valor
de venda e quantidade}.

4. Elaborar uma função que exibe na tela o Relatório de Estoque Baixo. Neste relatório devem ser incluídos apenas os produtos que contenham a quantidade em estoque inferior ou igual a 5 (cinco).

5. Implementar uma função capaz de exportar todos os dados no formato JSON.
[
{ "codigo": "1", "nome": "Arroz Branco (5 kg)", "valor_compra": "8.75", "quantidade": "26"},
{ "codigo": "2", "nome": "Feijão Carioca (1 kg)", "valor_compra": "5.20", "quantidade": "18"}
]
"""

import json

# Lista para armazenar os produtos
produtos = []
codigo_inicial = 1  # Código do primeiro produto

def cadastrar_produto():
    global codigo_inicial
    nome = input("Informe o nome do produto: ")
    valor_compra = float(input("Informe o valor de compra: "))
    quantidade = int(input("Informe a quantidade em estoque: "))
    
    # Cálculo do valor de venda
    valor_venda = valor_compra * 1.25
    
    produto = {
        "codigo": codigo_inicial,
        "nome": nome,
        "valor_compra": valor_compra,
        "valor_venda": valor_venda,
        "quantidade": quantidade
    }
    
    produtos.append(produto)
    codigo_inicial += 1  # Incrementa o código do próximo produto
    print("Produto cadastrado com sucesso!")

def relatorio_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    produtos_ordenados = sorted(produtos, key=lambda x: x["nome"])
    
    print("\nRelatório de Produtos:")
    print("{:<10} {:<30} {:<15} {:<15} {:<10}".format("Código", "Nome", "Valor Compra", "Valor Venda", "Quantidade"))
    for produto in produtos_ordenados:
        print("{:<10} {:<30} {:<15.2f} {:<15.2f} {:<10}".format(produto["codigo"], produto["nome"], produto["valor_compra"], produto["valor_venda"], produto["quantidade"]))
    print()

def relatorio_estoque_baixo():
    produtos_baixo = [p for p in produtos if p["quantidade"] <= 5]
    
    if not produtos_baixo:
        print("Nenhum produto com estoque baixo.")
        return
    
    print("\nRelatório de Estoque Baixo:")
    print("{:<10} {:<30} {:<15} {:<15} {:<10}".format("Código", "Nome", "Valor Compra", "Valor Venda", "Quantidade"))
    for produto in produtos_baixo:
        print("{:<10} {:<30} {:<15.2f} {:<15.2f} {:<10}".format(produto["codigo"], produto["nome"], produto["valor_compra"], produto["valor_venda"], produto["quantidade"]))
    print()

def exportar_dados():
    with open('produtos.json', 'w') as json_file:
        json.dump(produtos, json_file, indent=4)
    print("Dados exportados com sucesso para produtos.json!")

def menu():
    while True:
        print("Varejão do João")
        print("[1] Cadastrar produto")
        print("[2] Relatório de produtos")
        print("[3] Relatório de Estoque Baixo")
        print("[4] Exportar dados")
        print("[0] Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            relatorio_produtos()
        elif opcao == '3':
            relatorio_estoque_baixo()
        elif opcao == '4':
            exportar_dados()
        elif opcao == '0':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()