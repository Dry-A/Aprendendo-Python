from pessoa import Pessoa
import json


def faz_tracinhos():
    print(15*"- ")

pessoa_1 = Pessoa("Noruega", "branca","5002356A",52,"M")

print("Imprime o self.blablabla :", vars(pessoa_1))
print(f"Acessando registro no objeto - com o . ponto: {pessoa_1.registro}")
faz_tracinhos()

pessoa_1_dict = pessoa_1.to_dict()

print("Pessoa dict: imprime como esta definido no dict: ", pessoa_1_dict)
print(f"Acessando um registro no dict - com colchetes []: {pessoa_1_dict['registro']}")
faz_tracinhos()

#agora vamos serializar em json

# Serialização para JSON:
# Ao trabalhar com APIs ou armazenar dados em formato JSON, você frequentemente precisa 
# converter objetos para dicionários para posteriormente serializá-los em JSON.

pessoa_1_json = json.dumps(pessoa_1_dict)

print("Imprimindo agora Pessoa em json ( só depois de passar para dict) :",pessoa_1_json)

