
class Pessoa:
    def __init__(self,pais_origem, cor, registro_geral, idade, sexo):
        self.pais_bananinha = pais_origem
        self.cor = cor
        self.registro = registro_geral
        self.idade = int(idade)
        self.sexo = sexo
    
    def to_dict(self):
        return{
            'pais_origem':self.pais_bananinha,
            'cor':self.cor,
            'registro':self.registro,
            'idade':int(self.idade),
            'sexo':self.sexo
        }
    
  