from pessoa import Pessoa
import json

pessoa_1 = Pessoa("Noruega", "branca","5002356A",52,"M")
print(15*"- ")
print("Imprime o self.blablabla :", vars(pessoa_1))

pessoa_1_dict = pessoa_1.to_dict()

print(15*"- ")
print("Pessoa dict: imprime como esta definido no dict: ", pessoa_1_dict)

#agora vamos serializar em json

# Serialização para JSON:
# Ao trabalhar com APIs ou armazenar dados em formato JSON, você frequentemente precisa 
# converter objetos para dicionários para posteriormente serializá-los em JSON.

pessoa_1_json = json.dumps(pessoa_1_dict)

print(15*"- ")
print("Imprimindo agora Pessoa em json ( só depois de passar para dict) :",pessoa_1_json)

