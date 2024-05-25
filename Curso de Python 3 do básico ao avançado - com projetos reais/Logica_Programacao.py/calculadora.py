""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite o segundo número: ')
    operador_recebido = input('Digite o operador (+ - / * )')
    
    numeros_validos = None
    #aqui estamos 
    num_1_float = 0 #definindo variaveis pra poder usar globalmente
    num_2_float = 0
    
    try:
        #tente converter os numeros em float
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        #se ele conseguir os numeros_validos se tormnam verdadeiros
        numeros_validos = True
    
    except:
        #se nao conseguir faça algo aqui
        numeros_validos = None
        
    if numeros_validos is None:
        print('Os numeros ou um dos números digitados são inválidos')
        
        ##e para o laço. Terrm que voltar e pedir de novo os numeros, com o comando continue
        continue
    
    operadores_permitidos = '+/-*'
    
    if operador_recebido not in operadores_permitidos:
        print('Operador inválido')
        
    if len(operador_recebido) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Fazendo a sua conta .....')
    if operador_recebido == '+':
        print(num_1_float + num_2_float)
    elif operador_recebido == '*':
        print(num_1_float * num_2_float)
    elif operador_recebido == '-':
        print(num_1_float - num_2_float)
    elif operador_recebido == '/':
        print(num_1_float / num_2_float)
        
    else:
        print('nao deveria chegar aqui')
    
    
    
    
    
    
    sair = input('Quer sair? [s]im: ?').lower().startswith('s')
    if sair is True:
        break