from dados import produtos, pessoas, lista

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p

# nova_lista = map(lambda x: x*2, lista)
# nova_lista = [x * 2 for x in lista]
# print(lista)
# print(list(nova_lista))

# novos_produtos = map(aumenta_preco, produtos)
# for produto in novos_produtos:
#     print(produto)

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)