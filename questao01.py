#if
valorsoma = 0
for i in range (2):

    valor = int(input(f"\nDIGITE O VALOR {i+1} >> "))
    valorsoma += valor

valorC = int(input("\nDIGITE O ÚLTIMO VALOR >> "))

if(valorsoma < valorC):
    print(f"A SOMA DE A + B É MENOR QUE C")
else:
    print(f"A SOMA DE A + B É MAIOR QUE C")