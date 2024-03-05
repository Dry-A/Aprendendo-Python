from animal import Animal

meu_animal = Animal("mamífero","cachorro", "Dankan",4, ["raçao Proplan", "Carne","Verduras"] )
meu_passaro = Animal("pássaro", "papagaio","Curupato", 8, ["legumes", "alpiste", "semente de girassol"])

meu_peixe = Animal("peixator", "peixe", "Ferdinando", 11, ["comida de peixe", "alpiste", "farinha", "farofa"])

print(meu_animal)# nao vai - imprime: <animal.Animal object at 0x000001D3615F5B80>

print("Meu animal: ", vars(meu_animal))
print("Meu peixe: ", vars(meu_peixe))

del meu_animal.nome

print(meu_animal)# # Imprimindo o objeto inteiro usando o método __str__ que está na classe(parece um dto)
print(meu_passaro)

print(meu_passaro.nome)

