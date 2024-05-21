import json


evento_dto = {
        "nome":"Monique",
        "idade": 17,
        "personalidade":"ISTJ"    
    }
print(evento_dto)
print("O tipo do event_dto é neste momento: ",type(evento_dto))# dict
print(f"acessando a idade do dict : {evento_dto["idade"]}")#imprime a idade do dict
print(15 *'- ')


evento_transformado_em_string_json = json.dumps(evento_dto)

print("agora o dict foi tranformado em ",type(evento_transformado_em_string_json)," pelo json.dumps")# transforma em string json
print(f"isso é uma string json: {evento_transformado_em_string_json}")#imprime uma string json

print(15 *'- ')

evento_transformado_de_string_json_em_dict = json.loads(evento_transformado_em_string_json) #transforma em dict

print("Agora com o json loads transformamos uma string json em um dict: ",type(evento_transformado_de_string_json_em_dict))# transforma em dict
print(f"Isso é a impressao de um dict: {evento_transformado_de_string_json_em_dict}")
print(15 *'- ')

aluno = {
    "nome":"Danilo",
    "curso": "Javascript",
    "sexo": "Masculino",
    "unidade" : "Vila formosa",
    "matricula": 23432
}

print(aluno["sexo"])
print(aluno["nome"])

