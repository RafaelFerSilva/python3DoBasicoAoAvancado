
try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro: ',erro)
except Exception as erro:
    print('Erro inesperado: ',erro)

print('Continuando')
