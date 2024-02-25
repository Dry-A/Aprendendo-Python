# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
print(not True)  # False
print(not False)  # True

senha = input('Digite a senha: ')

if senha == '1234':
    print('Entrou')
else:
    print('Senha incorreta.')
    

senha_digitada = input('Digite a sua senha2: ')

if not senha_digitada:
    print('Voce nao digitou nada')
elif senha_digitada != '2345':
    print('Senha incorreta')
else:
    print('Entrou')