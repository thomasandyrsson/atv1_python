idades = []
soma = 0

for n in range(5):
    idade = int(input(f">> DIGITE A IDADE DA PESSOA {n+1} "))
    idades.append(idade)
    
for n in range(len(idades)):
    soma += idades[n]

media = soma / len(idades)

print(f"A MÉDIA DAS IDADES É {media}")