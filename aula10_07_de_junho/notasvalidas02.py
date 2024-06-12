#criando quantidade de notas
soma = 0
media = 0
qtdNotas = int(input("  >> QUANTAS NOTAS DESEJA INSERIR? ---> "))

#usuario digita a quantidade de notas
for i in range(qtdNotas):

#inserção de notas
    while (True):

        nota = float(input(f"\n--> Digite a nota {i+1}: "))
#notas validas
        if(nota >= 0 and nota <= 10):
            soma += nota
            break

        else:
            print("!!! DIGITE UMA NOTA DE 0 A 10 !!!")
#Calculo da media aritmética
media = soma / qtdNotas

#Imprimir a média do aluno
print(f"SUA MÉDIA É {media:.2f}")