numeros = [20,25,32,38]

#iterando sobre a lista
for numero in numeros:
    print(numero)
    
numeros.append(60)

print(numeros)

primeiro_numero = numeros[0]
print(primeiro_numero)

numeros.extend([52,14,25,48])
print(numeros)

idades = []

idades.extend([12,14,18,18,52,54])

print(idades)


alunos = [
    {
        'nome': 'Ivan',
        'nota_1': 10,
        'nota_2': 9
    },
    {
        'nome': 'Celia',
        'nota_1': 8,
        'nota_2': 6
    },
    {
        'nome': 'Carolina',
        'nota_1': 7,
        'nota_2': 8
    }   
]

print(alunos)

for aluno in alunos:
    print(aluno)

    

minha_lista = [1,3,5,7]

print("Minha lista original: ", minha_lista)

minha_lista.append(9)
print("Minha lista modificada: ", minha_lista)

minha_lista.remove(3)

print("Minha lista após remover o 3: ", minha_lista)


