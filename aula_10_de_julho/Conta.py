class Conta:
    def __init__(self, titular, saldo): #construtor
        self.__titular = titular #private atributos
        self.__saldo = saldo #saldo private 
    
    #Getters and setters
    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getTitular(self):
        return self.__titular
    
    def setTitular(self, titular):
        self.__titular = titular
    
    #metodo deposito
    def depositar(self, valor):
        self.setSaldo(self.getSaldo() + valor)

    #metodo saque
    def sacar(self):
        valor = int(input(f"Qual valor deseja sacar da conta de {self.__titular}? >> R$ ")) #Digitar valor
        self.setSaldo(self.getSaldo() - valor) #calculo
        print("SAQUE EFETUADO COM SUCESSO") #saque feito
    
    #metodo titular novo
    def novoTitular(self):
        novoTitular = input("Quem é o novo titular da conta? >> ") #digita novo dado
        self.setTitular(novoTitular) #atribuição
        print("DADOS ATUALIZADOS!") #operador feito
    
    #metodo impressão de dados
    def imprimeDados(self):
        print(f'''
              INFORMAÇÕES DA CONTA:
              Titular: {self.getTitular()}
              Saldo em conta: {self.getSaldo():.2f}
        ''')