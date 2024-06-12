#cadastrar 5 nomes de pessoas em uma lista
cadastro = []

#loop para inserir nome
for n in range(5):
    nome = input(">> QUAL O NOME QUE DESEJA GUARDAR? ")
    cadastro.append(nome)

#imprime
print(cadastro)