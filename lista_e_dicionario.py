#criando uma lista com alguns produtos 
produtos = ["rodas", "câmbio", "volante"]
#acessando elementos pelo índice 
#Lembre-se: o primeiro produto sempre está em 0
print(produtos[0])  #rodas
print(produtos[1])  #câmbio

# append() adiciona um elemento ao final da lista 
produtos.append("turbina ")

#insert() adiciona um elemento em uma posição específica
produtos.insert(1, "faróis")

#removendo elementos 
#remove() remove um elemento pelo seu valor 
produtos.remove("rodas")

# pop() remove um elemento pelo seu índice
removido = produtos.pop(1)
print("Produsto removido:", removido)

# ALTERANDO ELEMENTOS 

#Altere o valor de um elemento utilizando seu índice 
produtos[0] = "Câmbio automatico "

#consultando a lista

# len() retorna a quantidade de elementos 
print("Quantidade de produtos:", len(produtos))

#in verifica se determinado elemento existe 
if "Volante" in produtos:
    print("Volante encontrado!")

#for percorree todos os elementos da lista 
print("\n== LISTA DE PRODUTOS ===")

for produto in produtos:
    print(produto)

'''1. Listas — Lista de compras
Crie um programa que permita organizar uma lista de compras.
O programa deve: 
    Criar uma lista vazia chamada compras.
    Adicionar 3 produtos utilizando append().
    Adicionar mais um produto na segunda posição utilizando insert().
    Exibir todos os produtos utilizando for.
    Remover um produto utilizando remove().
    Exibir todos os produtos utilizando for.
    Mostrar quantos produtos existem na lista utilizando len().'''

compras = []

compras.append("Pão ")
compras.append("Gelatina ")
compras.append("Banana ")

compras.insert(1, "Maçã")

for compra in compras:
    print(compra)

compras.remove("Banana ")

for compra in compras:
    print(compra)

print("Quantidade de compras:", len(compras))







