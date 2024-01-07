import Produtos


print("Qual das operações você deseja fazer? \n 1- Adicionar produto \n 2- Remover produto \n 3- Verificar estoque")

opcao = int(input())

if opcao == 1:
    nome = input("Escreva o nome do produto: ")
    valor = input("Escreva o valor do produto: ")
    quantidade = input("Escreva a quantidade do produto: ")
    Produtos.add(nome, valor, quantidade)

elif opcao == 2:
    nome = input("Escreva o nome do produto: ")
    Produtos.remove(nome)

elif opcao == 3:
    Produtos.read()

