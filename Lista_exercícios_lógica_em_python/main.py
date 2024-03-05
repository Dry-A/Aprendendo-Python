#15
def informar_se_esta_no_intervalo(num):
    if 100<num<200:
       return 'Está no intervalo entre 100 e 200'

#16
def calcula_media_nota(nome, nota1, nota2, nota3):
    media = (nota1+nota2+nota3) /3
    
    if media >=7:
        print(f"{nome} foi aprovado com a média {media}")
    else:
        print(f"{nome} foi reprovado pois sua média ficou abaixo de sete -  Média {media}")
    
#17
def informar_numeros_no_intervalo(lista):
    numeros_que_estao= []
    numeros_que_nao_estao = []
    
    for numero in lista:
        if 10<=numero<=150:
            numeros_que_estao.append(numero)     
        else:
            numeros_que_nao_estao.append(numero)
            
    return numeros_que_estao, numeros_que_nao_estao
   
#18   
def informa_maioridade(lista_idades):
    lista_maioridade = []
  
    for pessoa in lista_idades:
        nome = pessoa['nome']
        idade = pessoa['idade']
        
        if idade >= 18:
            nome = pessoa['nome'],
            informacao_da_idade = 'é maior de idade'
            lista_maioridade.append(pessoa)
    
    return lista_maioridade

#19
def informar_sexo(lista):
    lista_nova =[]
    
    for pessoa in lista:
        nome = pessoa['nome']
        sexo = pessoa['sexo']
        
        if sexo == 'feminino':
            nome = pessoa['nome']
            genero = 'mulher'
            lista_nova.append(pessoa)
        else:
            nome = pessoa['nome']
            genero = 'homem'
            lista_nova.append(pessoa)
    
    return lista_nova

#20

def exibe_valor_desconto(valor_original, percentual_desconto):
    valor_do_desconto = valor_original *percentual_desconto
    print("Valor do desconto é ", valor_do_desconto)
    return valor_do_desconto



def calcula_novo_valor_com_desconto(valor_original, percentual_desconto):
    valor_do_desconto= exibe_valor_desconto(valor_original, percentual_desconto)
    novo_valor_carro = valor_original - valor_do_desconto
    print("O valor do carro com desconto é ", novo_valor_carro)
    return novo_valor_carro


def calcula_percentual_desconto(lista_carros):
    lista_valores_com_desconto = []
    
    for carro in lista_carros:
        modelo = carro['modelo']
        ano = carro['ano']
        valor = carro['valor']        
        
        if ano <=2000:
            percentual = 12/100
            modelo = carro['modelo']
            valor = carro['valor']
            ano = carro['ano']
            novo_valor = calcula_novo_valor_com_desconto(valor, percentual)
            lista_valores_com_desconto.append(carro)
        elif ano> 2000:
            percentual = 7/100
            modelo = carro['modelo']
            valor = carro['valor']
            ano = carro['ano']
            novo_valor = calcula_novo_valor_com_desconto(valor, percentual)
    
    return novo_valor

         
   #24
def avalia_numero(lista):
    
    for numero in lista:
        if numero < 0:
            print('Número negativo')
        elif numero>0:
            print('Número positivo')
        else:
            print('Número Zero')
            
#26
def escrever_por_extenso(numero):
    if numero==1:
        print('Um')
    elif numero==2:
        print('dois')
    elif numero==3:
        print('três')
    elif numero ==4:
        print('Quatro')
    elif numero ==5:
        print('Cinco')
    else:
        print('número inválido.')

#30
def identifica_maior_numero(lista_tripla):
    lista_tripla.sort()
    print(lista_tripla)
    
    
lista_nova = [ 14,8,52]
identifica_maior_numero(lista_nova)
                    
            
def calcula_pagamento():
    
    nivel = input('Digite seu nível: ')
    horas_aula = int(input('Digite quantidade de horas trabalhada neste mês: '))

    if nivel == '1':
        valor_salario = horas_aula *12
        print( f'R$ {valor_salario}') 
    elif nivel =='2':
        valor_salario = horas_aula*17
        print(f'R$ {valor_salario}') 
    elif nivel=='3':
        valor_salario = horas_aula*25
        print(f'R$ {valor_salario}') 
        
          
        
            
