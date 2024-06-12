import random

numeroSecreto = int(random.randint(1, 10))
numTentativa = 0

print(" ||| VAMOS BRINCAR? ||| \n Eu estou pensando em um número, você tem que advinhar")

while(True):
    tentativa = int(input("\n>> QUE NÚMERO ESTOU PENSANDO? --> "))
    numTentativa += 1

    if(tentativa == numeroSecreto):
        print(f"    VOCÊ ACERTOU! E VOCÊ LEVOU APENAS {numTentativa} VEZ(ES) PARA ACERTAR")
        break

    else:
        print("QUE PENINHA, VOCÊ ERROU HAHA")

        if (tentativa > numeroSecreto):
            print("SEU PALPITE É MENOR QUE O NÚMERO QUE EU PENSEI")
        else: 
            print("SEU PALPITE É MAIOR QUE O NÚMERO QUE EU PENSEI")