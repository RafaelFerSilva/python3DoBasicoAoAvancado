import sys
import time

# lista = list(range(10))

# print(hasattr(lista, '__iter__'))

# for v in lista:
#     print(v)

# Dentro do for a lista vira um iterador porém em sua natureza ela não e

#  Podemos transformar uma lista em um iterador
# lista = iter(lista)
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(hasattr(lista, '__next__'))

# Geradores entregam os elementos conforme solicitados, isso faz com que seja utilizado menos memória
# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
#
# g = gera()
# # print(g)
#
# for v in g:
#     print(v)

# l1 = [x for x in range(10000)]
# l2 = (x for x in range(10000))
#
# print(sys.getsizeof(l1))
# print(sys.getsizeof(l2))



