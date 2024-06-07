
valor1 = input("Digite o valor 1: ")
valor2 = input("Digite o valor 2: ")
valor3 = input("Digite o valor 3: ")


if (valor1 == valor2 or valor2 == valor3 or valor1 == valor3):
    print("!!! ERRO: INFORME VALORES DIFERENTES !!!")
else:
    if(valor1 < valor2 and valor1 < valor3):
        if(valor2 < valor3):
            print(valor1, valor2, valor3)
        else:
            print(valor1, valor3, valor2)
    elif (valor2 < valor1 and valor2 < valor3):
        if(valor1 < valor3):
            print(valor2, valor1, valor3)
        else:
            print(valor2, valor3, valor1)
    elif(valor3 < valor1 and valor3 < valor2):
        if(valor2 < valor3):
            print(valor3, valor2, valor1)
        else:
            print(valor3, valor1, valor2)