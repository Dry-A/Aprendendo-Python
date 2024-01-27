class Pessoa:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso


pessoas = [
    Pessoa("Anacleto", "Python"),
    Pessoa("Ruivo", "Javascript"),
    Pessoa("Vinicius", "Java"),
    Pessoa("Romário","Front-end")
]

print("Informaçao sobre as pessoas: ")

for pessoa in pessoas:
    print(f"Nome: {pessoa.nome}, Curso: {pessoa.curso}")