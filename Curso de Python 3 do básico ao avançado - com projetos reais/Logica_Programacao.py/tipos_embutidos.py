#tipos imutaveis: str, int, float, bool

string = 'Rua Elvira'
cidade = 'Vila Velha'
profissao = 'programador'


#Fatiamento [i:f:p] [::]
#inicio, fim, passo(de quanto em quanto)

##string[6] = 'e' # voce nao muda o valor da variavel, vc cria outra
print(string[6])


outra_variavel = f'{string[:3]}'#pega os 3 primeiros caracteres

print(outra_variavel)

mais_uma_variavel = f'{string[0:7:2]}'

print(mais_uma_variavel)

fatiando_profissao = f'preu{profissao[2:7:1]}aria{string[4:8:1]}'

print(fatiando_profissao.capitalize())

print(outra_variavel.isalpha())
print(outra_variavel.zfill(8))
