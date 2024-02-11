alunos = [
    {
        'nome': 'José',
        'nota_primeiro_semestre': 8,
        'nota_segundo_semestre': 7,
        'nota_terceiro_semestre': 9,
        'nota_quarto_semestre': 10,
    },
    {
        'nome': 'Raiana',
        'nota_primeiro_semestre': 5,
        'nota_segundo_semestre': 10,
        'nota_terceiro_semestre': 9,
        'nota_quarto_semestre': 8,
    },
    {
        'nome': 'Bento',
        'nota_primeiro_semestre': 4,
        'nota_segundo_semestre': 6,
        'nota_terceiro_semestre': 8,
        'nota_quarto_semestre': 9,
    },
    {
        'nome': 'Luma',
        'nota_primeiro_semestre': 9,
        'nota_segundo_semestre': 10,
        'nota_terceiro_semestre': 10,
        'nota_quarto_semestre': 10,
    },
]

def calcula_media(lista):
    soma = 0
    
    for item in lista:
        soma += item
    
    media = soma / len(lista)
    
    return media

def inclui_media(lista):
    novo_array = []
    
    for aluno in lista:
        
        nota_um = aluno["nota_primeiro_semestre"]
        nota_dois = aluno["nota_segundo_semestre"]
        nota_tres = aluno["nota_terceiro_semestre"]
        nota_quatro = aluno["nota_quarto_semestre"]
        
        notas = [nota_um, nota_dois, nota_tres, nota_quatro]
        
        media_aluno = calcula_media(notas)
        
        novo_aluno = {
            
            'nome': aluno['nome'],
            'nota_primeiro_semestre': aluno['nota_primeiro_semestre'],
            'nota_segundo_semestre': aluno['nota_segundo_semestre'],
            'nota_terceiro_semestre': aluno['nota_terceiro_semestre'],
            'nota_quarto_semestre': aluno['nota_quarto_semestre'],
            'media': media_aluno
        }
        
        novo_array.append(novo_aluno)
        
    return novo_array
    
print(inclui_media(alunos)) 
        
        