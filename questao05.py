# Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o
# semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado
# (media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9)

        #insira nome

nome = input(">> INSIRA O SEU NOME: ")

        #insira notas

somanota = 0
resposta = "sim"
qtdNotas = 0
media = 0
situacao = ""

        #laço de repetição com o pedido de notas

while resposta == "Sim" or resposta == "sim" or resposta == "SIM" or resposta == "S" or resposta == "s":
    nota = float(input(">> INSIRA A NOTA REGISTRADA: "))
            # while nota >= 10 or nota <= 0:
            #     print("\n!!! NOTA INVÁLIDA! VALORES PERMITIDOS ENTRE 0 E 10 !!!")
            #     nota = float(input(">> INSIRA A NOTA REGISTRADA: "))
            #     if nota <= 10 or nota >= 0:
            #         break
    resposta = input(">> DESEJA INSERIR MAIS NOTAS? Digite Sim ou Não: ")
    qtdNotas += 1
    somanota += nota

        #condicional do laço

    if resposta == "Não" or resposta == "não" or resposta == "NÃO" or resposta == "N" or resposta == "n":
        break

        #calculo da soma

media = somanota / qtdNotas

        #condicional da situação academica
        
if media >= 7 and media:
    situacao = "Aprovado(a)"
elif media >= 5.1 or media >= 6.9:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado(a)"

        #impressão final
        
print(f"\n>> {nome}, SUA MÉDIA É {media:.2f} E VOCÊ ESTÁ {situacao}")