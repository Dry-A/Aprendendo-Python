"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_digitado = input('Digite um número inteiro: ')

if not numero_digitado.isdigit():
    print('Este não é um número inteiro! ')
    exit()

numero_int = int(numero_digitado)

numero_digitado.isdigit()

if numero_int % 2 ==0:
    print('Número par')
else:
    print('Numero ímpar')
    
    
print(15* '- ')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_digitada = int(input('Que horas são agora ( Digite no formato hh): '))

if 0<hora_digitada<=11:
    print('Bom dia! ')
elif 12<hora_digitada<=17:
    print('Boa tarde!')
elif 18<hora_digitada<23:
    print('Boa noite!')

print(15* '- ')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 8 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_digitado = input('Digite seu primeiro nome: ')

tamanho_nome = len(nome_digitado)

if tamanho_nome <=4:
    print('Nome curto')
elif 5<=tamanho_nome<=8:
    print('Nome normal')
else:
    print('Nome muito grande')
