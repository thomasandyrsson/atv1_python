#Atribuindo variavel
soma = 0
media = 0
qtdNota = 0

#Inserção de notas, somando-as, quantificando-as e verificando se é menor que 4
while(qtdNota < 4):
    nota = float(input(">> Digite a nota a ser inserida: "))

#Se a nota for válida, soma, se não, repete o loop
    if(nota >= 0 and nota <= 10):
        soma += nota
        qtdNota += 1
    else:
        print("!!! DIGITE UMA NOTA DE 0 A 10 !!!")
        continue

#Calculo da media aritmética
media = soma / qtdNota

#Imprimir a média do aluno
print(f"SUA MÉDIA É {media:.2f}")

