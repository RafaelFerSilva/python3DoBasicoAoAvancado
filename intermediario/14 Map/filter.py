from dados import produtos, pessoas, lista

# nova_list = [x for x in lista if x > 5]
# nova_list = filter(lambda x: x > 5, lista)
# print(list(nova_list))

# nova_list = filter(lambda p: p['preco'] > 50, produtos)

# for produto in nova_list:
#     print(produto)

nova_lista = filter(lambda p: p['idade'] > 18, pessoas)
for pessoa in nova_lista:
    print(pessoa)
