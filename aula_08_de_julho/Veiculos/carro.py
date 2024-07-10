class Carro:
    def __init__(self, modelo, ano, placa, fabricante, velocidade):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.fabricante = fabricante
        self.velocidade = velocidade

    def acelerar(self, velocidade):
        self.velocidade += velocidade
    
    def zerar(self):
        self.velocidade = 0
    
    def verInformacoes(self):
        print(f''' INFORMAÇÕES DO VEÍCULO 
              Modelo: {self.modelo}
              Ano do veículo: {self.ano}
              Placa: {self.placa}
              Fabricante: {self.fabricante}           
              ''')
        if self.velocidade == 0:
            print("O veículo está parado")
        else:
            print(f"O veículo está a {self.velocidade}km/h")