from itertools import zip_longest, count

indice = count()
cidade = ['São Paulo', 'Rio de Janeiro', 'Mogi Mirim']
estados = ['SP', 'RJ', 'SP']

cidades_estados = zip(
    indice,
    estados,
    cidade,
)
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

for valor in cidades_estados:
    print(valor)
