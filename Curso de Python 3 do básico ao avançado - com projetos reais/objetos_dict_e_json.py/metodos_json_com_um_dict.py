
import json


evento_dto = {
        "nome":"Manuela",
        "idade": 17,
        "personalidade":"ISTJ"    
    }

print(type(evento_dto))# dict
print(evento_dto)


evento_transformado_em_string_json = json.dumps(evento_dto)

print(type(evento_transformado_em_string_json))# transforma em string json
print(f"isso é uma string json: {evento_transformado_em_string_json}")#imprime uma string json
print(f"idade: {evento_dto["idade"]}")#imprime a idade do dict


evento_transformado_de_string_json_em_dict = json.loads(evento_transformado_em_string_json) #transforma em dict

print(type(evento_transformado_de_string_json_em_dict))# transforma em dict
print(f"Isso é a impressao de um dict: {evento_transformado_de_string_json_em_dict}")

