carrinho = []


def adiciona_item_carrinho(item, price):
    carrinho.append((item, price))


def retornar_total():
    total = sum(float(y) for x, y in carrinho)
    return total


adiciona_item_carrinho("Produto 1", 50)
adiciona_item_carrinho("Produto 1", 20)
adiciona_item_carrinho("Produto 1", 30)
adiciona_item_carrinho("Produto 1", 50)

print(retornar_total())
