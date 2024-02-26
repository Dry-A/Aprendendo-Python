# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  A u d r e y
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = 'Audrey'
print(nome[1])
print(nome[-2])
print(10*'- ')
print('dr'in nome)
print('drei'not in nome)

nome_usuario = input('Digite o seu nome: ')
deseja_encontrar = input('Digite o que deseja encontrar ')

if deseja_encontrar in nome_usuario:
    print(f'{deseja_encontrar} está em {nome_usuario}')
else:
    print(f'{deseja_encontrar} não está em {nome_usuario}')
    
nome_mulher = 'Maria do Carmo'
 
if ' ' in nome_mulher:
    print(f'O nome {nome_mulher} tem espaços.')
else:
    print(f'O nome {nome_mulher} NÃO tem espaços.')