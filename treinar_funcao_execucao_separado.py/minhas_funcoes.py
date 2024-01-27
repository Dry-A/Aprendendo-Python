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