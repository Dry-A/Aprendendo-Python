# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy  0   0.0   'string vazia'   False
# Também existe o tipo None que é
# usado para representar um não valor (nao existe nenhum valor)

entrada = input('[E]ntrar [S]air: ')

if entrada=='S':
    print('Sair')
    exit()

senha_digitada = input('Digite a Senha: ')
senha_permitida = '446688'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito - para no primeiro valor que é false pra poupar recurso
print(True and False and True)# isso vai dar False devido ao False do meio 
print(True and 0 and True) #será impresso o 0(zero) 

desempregado = False
filhos = 3
renda = 4500

if desempregado and filhos >=2:
    print('Pode participar do programa BDDS')
elif desempregado and filhos ==1:
    print('Procure Casa Mariana')
elif not desempregado and filhos>2:
    if renda >= 3600:
        print('direito a isençao de material')
else:
    print('verifique suas opcoes novamente')
    
      