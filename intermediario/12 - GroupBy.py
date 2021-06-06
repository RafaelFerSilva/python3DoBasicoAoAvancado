from itertools import groupby, tee  

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Rafael', 'nota': 'B'},
    {'nome': 'Denise', 'nota': 'C'},
    {'nome': 'Marlene', 'nota': 'D'},
    {'nome': 'Fatima', 'nota': 'A'},
    {'nome': 'Monika', 'nota': 'A'},
    {'nome': 'Fernanda', 'nota': 'B'},
    {'nome': 'Cristina', 'nota': 'D'},
    {'nome': 'Vania', 'nota': 'C'},
    {'nome': 'Artina', 'nota': 'A'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    # realiza a cópias do iterador
    var1, var2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in var1:
        print(f'\t{aluno}')

    quantidade = len(list(var2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()


