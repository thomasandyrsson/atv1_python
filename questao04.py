
valor1 = input("Digite o valor 1: ")
valor2 = input("Digite o valor 2: ")
valor3 = input("Digite o valor 3: ")

if(valor1 > valor2 and valor1 > valor3):
    if(valor2 > valor3):
        print(valor1, valor2, valor3)
    else:
        print(valor1, valor3, valor2)
elif (valor1 > valor2 and valor1 > valor3):