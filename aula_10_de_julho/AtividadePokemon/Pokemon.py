class Pokemon:
    def __init__(self, especie, ataque, defesa, hp):
        self._especie = especie
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp

    def atacar(self, pokemon):
        dano = self._hp - ((pokemon._ataque / self._defesa)*2)
        return dano





class Aço(Pokemon):
    def __init__(self, especie, ataque, defesa, hp):
        super().__init__(especie, ataque, defesa, hp)

