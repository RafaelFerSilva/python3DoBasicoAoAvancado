from itertools import combinations, permutations, product

pessoas = ['Rafael', 'Denise', 'Marlene', 'Monika', 'Fatima']
#  Combina sem repetir elementos
for grupo in combinations(pessoas, 2):
    print(grupo)

# Não combina o mesmo elemento
# for grupo in permutations(pessoas, 2):
#     print(grupo)

# todas as combinações possiveis
# for grupo in product(pessoas, repeat=2):
#     print(grupo)