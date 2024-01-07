import json
import pandas as pd

#Função para adicionar um produto no estoque e caso já exista ele informa que o produto já foi adicionado 

def add(nome, preco, quantidade):
    try:
        with open("produtos.txt", "r") as arq:
            info = arq.read()
            produtos = json.loads(info) if info else []
    except FileNotFoundError:
        produtos = []

    for produto in produtos: 
        if "nome" in produto and produto["nome"] == nome:
            print("Produto já está no estoque")
            return
    produto_novo = {"nome": nome , "valor": preco, "quantidade": quantidade}
    produtos.append(produto_novo)

    with open("produtos.txt", "w") as arq:
        json.dump(produtos, arq)


#Função para remover um produto do estoque  
        
def remove(nome):
    try:
        with open("produtos.txt", "r") as arq:
            produtos = json.load(arq) 
    except FileNotFoundError:
        return
    
    lista_final = []
    for produto in produtos:
        if produto['nome'] != nome:
            lista_final.append(produto)

    if len(lista_final) == len(produtos):
        print("Este produto não está no estoque")
    else:
        with open("produtos.txt", "w") as arq:
            json.dump(lista_final, arq)

#Função para mostrar os produtos no estoque 

def read():
    nomes =[]
    valor = []
    quantidade = []
    try:
        with open("produtos.txt", "r") as arq:
            info = arq.read()
            produtos = json.loads(info)
            for produto in produtos:
                nomes.append(produto['nome'])
                valor.append(produto['valor'])
                quantidade.append(produto['quantidade'])
                
    except FileNotFoundError:
        return
    
# Criando uma tabela para mostrar o estoque 

    df = pd.DataFrame({'Produto': nomes, 'Preço': valor, 'Quantidade': quantidade})

    print(df)


