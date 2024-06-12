lista_compras = []

for i in range(10):
    item = input(f">> Digite o item {i+1}: ")
    lista_compras.append(item)

for n in range(len(lista_compras)):
    print(f"{n+1} , {lista_compras[n]}")