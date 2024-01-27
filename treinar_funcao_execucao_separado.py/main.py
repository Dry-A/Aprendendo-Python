from minhas_funcoes import calcula_media, saudacao, inclui_media

nome_usuario= "Alice"
mensagem = saudacao(nome_usuario)
print(mensagem)

lista_notas = [8,9,10,9]
lista_idades = [65,50,41,42,48,42,85]

media_notas_2023 = calcula_media(lista_notas)
print(media_notas_2023)

print(calcula_media(lista_idades))

print(saudacao("Fernanda"))

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

print(inclui_media(alunos))

