string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10

# verificar quantos fatias de 10 conseguimos fazer com a string
contadores = [i for i in range(0, len(string), n)]

# Criou tuplas juntando os contadores de 10 em 10 para indicar o inicio e o fim
tuplas = [(i, i + n) for i in range(0, len(string), n)]

#  Usando os indices de 10 em 10 nós criamos novas listas
lista = [string[i: i + n] for i in range(0, len(string), n)]
raw = [f'string[{i}: {i + n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(contadores)
print(tuplas)
print(raw)
print(lista)
print(retorno)
