#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais
#deverá somar os dois, caso contrário multiplique A por B. Ao final de qualquer um
#dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo
#na tela.

#var
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))

#condicional
if num1 == num2:
    soma = num1 + num2
    print(f"A operação realizada é a soma e o resultado é {soma}")
else:
    mult = num2 * num1
    print(f"A operação realizada é a multiplicação e o resultado é {mult}")