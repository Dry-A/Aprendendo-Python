def calcula_media(lista):
    soma = 0

    for item in lista:
        soma += item

    media = soma / len(lista)
    return media


def saudacao(nome):
    return f"Olá, {nome}"

def inclui_media(lista):
    novo_array = []

    for aluno in lista:
        nota1semestre = aluno['nota_primeiro_semestre']
        nota2semestre = aluno['nota_segundo_semestre']
        nota3semestre = aluno['nota_terceiro_semestre']
        nota4semestre = aluno['nota_quarto_semestre']

        # Lista das notas de cada semestre
        notas = [nota1semestre, nota2semestre, nota3semestre, nota4semestre]

        # Calcula a média do aluno
        media_aluno = calcula_media(notas)

        # Cria um novo dicionário com o nome, notas e média do aluno
        novo_aluno = {
            'nome': aluno['nome'],
            'nota_primeiro_semestre': aluno['nota_primeiro_semestre'],
            'nota_segundo_semestre': aluno['nota_segundo_semestre'],
            'nota_terceiro_semestre': aluno['nota_terceiro_semestre'],
            'nota_quarto_semestre': aluno['nota_quarto_semestre'],
            'media': media_aluno,
        }

        # Adiciona o novo dicionário ao novo array
        novo_array.append(novo_aluno)

    return novo_array

#Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 10;

def mostra_mensagem_se_maior_que_dez(numero):
    mensagem = f"O número {numero} é maior que 10."
     
    if numero > 10:
        return mensagem
    
def mostra_se_numero_esta_no_intervalo(num):
    mensagem_acerto = f"O número {num} está entre 100 e 200"
    mensagem_erro = f"O número {num} não está entre 100 e 200"
    
    if num >100 and num < 200:
        print(mensagem_acerto)
    else:
        print(mensagem_erro)
        
def maior_idade(lista):
    
    pessoas = []
    
    for pessoa in lista:
        nome = pessoa['nome'],
        idade = pessoa['idade']
        
        if idade >=18:
            pessoa = {
                'nome': pessoa['nome'],
                'idade': pessoa['idade'],
                'maior_idade': "sim"
            }
        else:
             pessoa = {
                'nome': pessoa['nome'],
                'idade': pessoa['idade'],
                'maior_idade': "não"
            }
        
        pessoas.append(pessoa)
        
    return pessoas

def contabiliza_por_sexo(lista):
    homem = 0
    mulher = 0
    
    nova_lista = []
    
    for pessoa in lista:
        sexo = pessoa['sexo']
        
        if sexo == 'masculino':
            homem +=1
            pessoa = {
                'nome': pessoa['nome'],
                'sexo': "homem"
            }
        else:
            mulher +=1
            pessoa = {
                'nome': pessoa['nome'],
                'sexo': "mulher"
            }
            
        nova_lista.append(pessoa)
    
    print(f"homens {homem} e mulheres {mulher}")
    
    return nova_lista

def autoriza_servico_militar_obrigatorio(lista):
    nova_lista = []
    
    for candidato in lista:
        sexo = candidato['sexo']
        idade= candidato['idade']
        saude= candidato['saude']
        if sexo == 'masculino':
            if 18 <= idade <= 28 and saude != "ruim":
                     candidato = {
                        'nome': candidato['nome'],
                        'situacao': "apto"
                  }
            else:
                candidato = {
                    'nome': candidato['nome'],
                    'situacao': "inapto"
                }      
        else:
            candidato = {
                'nome': candidato['nome'],
                'situacao': "inapto"
            }
        nova_lista.append(candidato)
        
    return nova_lista


def escreve_por_extenso(num):
    if num == 1:
        return "um"
    elif num ==2:
        return "dois"
    else:
        return "número inválido"
    
def define_aumento_salario(funcionario):
    
    salario = funcionario['salario']
    
    if salario < 3600:
        novo_salario = salario*1.50
    elif 3600 <=salario <= 12000:
        novo_salario = salario*1.20
    elif 12000 < salario <=24000:
        novo_salario = salario*1.15
    else:
        novo_salario = salario*1.10
    
    return novo_salario
            
    


            
    
    
    