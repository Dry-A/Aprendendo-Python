   
while True:
    sair = input('Quer sair? [s]im:')
    sair = sair.lower().startswith('s')
    print(sair)
    if sair is True:
        break
    
# ou assim:

while True:
    print('meu código.......... pedir numero , operador, etc')
    #####
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)
    
    if sair is True:
        break