class Triangle:
    
    def __init__(self, ladoA, ladoB, ladoC):
            self.ladoA = ladoA
            self.ladoB = ladoB
            self.ladoC = ladoC

    def getLadoA(self):
         return self.ladoA
    
    def getLadoB(self):
         return self.ladoB
    
    def getLadoC(self):
         return self.ladoC
    
    def setLadoA(self, ladoA):
         self.ladoA = ladoA

    def setLadoB(self, ladoB):
         self.ladoB = ladoB

    def setLadoC(self, ladoC):
         self.ladoC = ladoC
    
    def novoTriangulo(self):
         self.setladoA()

    def calcularPerimetro(self):
        valor = self.ladoA + self.ladoB + self.ladoC
        return valor
    
    def getMaiorLado(self):
        
        valores = [self.ladoA, self.ladoB, self.ladoC]
        maior = max(valores)
        
        return maior

    def calculoArea(self):
        area = self.ladoA + self.ladoB / 2
        return area