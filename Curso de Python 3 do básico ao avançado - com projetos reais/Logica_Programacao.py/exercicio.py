"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ') or ('')

idade = input('Digite sua idade: ') or ('')
if nome =='' or idade=='':
    print('Desculpe, você deixou campos vazios.')
    exit()


print(f'Seu nome é {nome}')
print(f'Seu nome invertido é {nome[::-1]}')
if ' ' in nome:
    print('Seu nome tem espaço')
else:
    print('Seu nome não tem espaço')   
print(f'Seu nome tem {len(nome)} letras.')
print(f'A primeira letra do seu nome é {nome[0]}.')
print(f'A ultima letra do seu nome é {nome[-1]}.')

#outro moddo de fazer:

nome_2 = input('Digite seu nome_2: ')

idade_2 = input('Digite sua idade_2: ')

#string vaxia é falsy
if nome_2 and idade_2:
    print(f'Seu nome é {nome_2}')
    print(f'Seu nome invertido é {nome_2[::-1]}')
    if ' ' in nome_2:
        print('Seu nome tem espaço')
    else:
        print('Seu nome não tem espaço')   
    print(f'Seu nome tem {len(nome_2)} letras.')
    print(f'A primeira letra do seu nome é {nome_2[0]}.')
    print(f'A ultima letra do seu nome é {nome_2[-1]}.')
else: 
    print('Desculpe, você deixou campos vazios.')
          

