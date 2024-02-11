alunos = [
    {
        "nome": "Luma",
        "nota_primeiro_semestre": 8,
        "nota_segundo_semestre": 8.5,
        "nota_terceiro_semestre": 8,
        "nota_quarto_semestre": 7.5,
    },
    {
        "nome": "Rafael",
        "nota_primeiro_semestre": 10,
        "nota_segundo_semestre": 8.5,
        "nota_terceiro_semestre": 9,
        "nota_quarto_semestre": 10,
    },
    {
        "nome": "Julia",
        "nota_primeiro_semestre": 9,
        "nota_segundo_semestre": 6,
        "nota_terceiro_semestre": 6.5,
        "nota_quarto_semestre": 7,
    },
    {
        "nome": "Lucas",
        "nota_primeiro_semestre": 8,
        "nota_segundo_semestre": 7,
        "nota_terceiro_semestre": 5,
        "nota_quarto_semestre": 9,
    },
]

# Calcular a média de cada aluno e adicionar a informação no objeto
for aluno in alunos:
    notas = [
        aluno["nota_primeiro_semestre"],
        aluno["nota_segundo_semestre"],
        aluno["nota_terceiro_semestre"],
        aluno["nota_quarto_semestre"],
    ]
    media = sum(notas) / len(notas)
    aluno["media"] = media

# Imprimir o novo array com a informação da média
for aluno in alunos:
    print(aluno)