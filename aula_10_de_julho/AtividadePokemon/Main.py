
from Pokemon import Pokemon

class Agua(Pokemon):
    def __init__(self, especie, ataque, defesa, hp):
        super().__init__(especie, ataque, defesa, hp)
    
class Fogo(Pokemon):
    def __init__(self, especie, ataque, defesa, hp):
        super().__init__(especie, ataque, defesa, hp)

p1 = Agua("Squirtle", 56, 40, 89)
p2 = Fogo("Charmander", 51, 38, 78)

p1.atacar(p2)
