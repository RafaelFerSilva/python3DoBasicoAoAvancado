perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '40', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
            'pergunta': 'Quanto é 2 + 1?',
            'respostas': {'a': '1', 'b': '4', 'c': '3', },
            'resposta_certa': 'c',
        },
    'Pergunta 3': {
            'pergunta': 'Quanto é 2 + 4?',
            'respostas': {'a': '6', 'b': '4', 'c': '40', },
            'resposta_certa': 'a',
        },
    'Pergunta 4': {
            'pergunta': 'Quanto é 2 + 0?',
            'respostas': {'a': '1', 'b': '2', 'c': '40', },
            'resposta_certa': 'b',
        },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha uma das opções abaixo:\n')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        respostas_certas += 1
        print('Voce Acertou')
    else:
        print('Voce Errou')

    print()

print(f'Respostas Certas {respostas_certas}')
print(f'Respostas Erradas {len(perguntas) - respostas_certas}')
print(f'Você acertou {respostas_certas / len(perguntas) * 100} % das questões')
print()
