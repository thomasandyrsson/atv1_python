print('''
      TABELA DE PREÇOS
      Produto                  Preço      
100 Cachorro Quente      R$ 1.10
101 Bauru Simples        R$ 1.30
102 Bauru c/ovo          R$ 1.50
103 Hamburguer           R$ 1.10
104 Cheeseburguer        R$ 1.30
105 Refrigerante         R$ 1.00  
106 Batata Frita         R$ 0.90
      ''')

escolha = int(input("|| DIGITE O CÓDIGO DO PRODUTO QUE VOCÊ DESEJA >> "))
if(escolha == 100):
    preco = 1.10
elif(escolha == 101):
    preco = 1.30
elif(escolha == 102):
    preco = 1.50