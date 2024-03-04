"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

#input sempre vai trazer uma string
numero_string = input('digite um numero que vou dobrar: ')
#sempre que o usuario te mandar qualquer coisa, precisamos tratar esse valor

#tenta executar um codigo que vier aqui
try:
    #print('STR: ', numero_string)
    numero_float = float(numero_string)
    print('FLOAT: ', numero_float)
    print(f' O dobro de {numero_string} é {numero_float*2:.2f}')
  
  #se ocorrer um erro no meu try, pula imediatamente pro except  
except:
   
    print('Isso não é um número')





#checa se o usuario digitou apenas numeros, sem pontos
print(numero_string.isdigit()) #retorna true or false(se tiver um ponto, por exemplo)

#if numero_string.isdigit():
#    numero_float = float(numero_string)
#    print(f' O dobrio de {numero_string} é {numero_float*2:.2f}')
#else:
 #   print('Isso não é um')

#o if nao evita excecao/erros, ele só checa uma condicao a logica em codigo sem excecao