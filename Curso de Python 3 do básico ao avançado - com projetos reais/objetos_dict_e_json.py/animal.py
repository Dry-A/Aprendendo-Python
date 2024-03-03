
class Animal:
    def __init__(self, especie, raca, nome, idade, comidas_preferidas):
        self.especie = especie
        self.raca = raca
        self.nome = nome
        self.idade = int(idade)
        self.comidas = comidas_preferidas
    
    def __str__(self):
        return f"Animal({self.especie},{self.raca},{self.comidas})"
        
        
