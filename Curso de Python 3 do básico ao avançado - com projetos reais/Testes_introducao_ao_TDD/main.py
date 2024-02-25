from calculadora import soma, divisao


#try:
#    print(soma(15,'oi'))
#except TypeError as erro:
#    print('Dá nao, conta inválida')
#    print(erro)

try:
    print(soma('ola ',40))
except AssertionError as erro:
    print(f'Que conta maluca: {erro}')
    
try:
    print(divisao(40,0))
except AssertionError as erro2:
    print(f'Assim nào dá nao: {erro2}')
