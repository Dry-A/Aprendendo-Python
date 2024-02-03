from minhas_funcoes import define_aumento_salario, escreve_por_extenso,autoriza_servico_militar_obrigatorio, contabiliza_por_sexo, maior_idade, mostra_se_numero_esta_no_intervalo, calcula_media, saudacao, inclui_media, mostra_mensagem_se_maior_que_dez

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

print(mostra_mensagem_se_maior_que_dez(40))
print(mostra_se_numero_esta_no_intervalo(50))


pessoas = [
    {
        "nome": "Valente",
        "idade": 25
    },
     {
        "nome": "Ricardo",
        "idade": 45
    },
      {
        "nome": "Roberto",
        "idade": 60
    },
       {
        "nome": "Elizeu",
        "idade": 15
    },
]
print(maior_idade(pessoas))

candidatos = [
    {
        'nome':"Carlitos",
        'sexo': 'masculino',
        "idade": 60,
        "saude": "boa"
    },
     {
        'nome':"Felipe",
        'sexo': 'masculino',
        "idade": 17,
        "saude": "ruim"
    },
      {
        'nome':"Fernanda",
        'sexo': 'feminino',
        "idade": 18,
        "saude": "ótima"
    },
       {
        'nome':"Clebers",
        'sexo': 'masculino',
        "idade": 25,
        "saude": "ruim"
    },
        {
        'nome':"Jeová",
        'sexo': 'masculino',
        "idade": 38,
        "saude": "ótimo"
    },
         {
        'nome':"Sergio",
        'sexo': 'masculino',
        "idade": 26,
        "saude": "boa"
    }

]

print(autoriza_servico_militar_obrigatorio(candidatos))

print(escreve_por_extenso(2))

funcionario = {
    'nome': 'Fonseca',
    'salario': 25000
}

print(define_aumento_salario(funcionario))
