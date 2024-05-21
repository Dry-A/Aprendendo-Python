import json

clientes = [
    {
        'nome': 'João',
        'sobrenome': 'Silva',
        'sexo': 'Masculino',
        'endereco': {
            'logradouro': 'Rua das Flores',
            'numero': 123,
            'bairro': 'Jardim das Acácias',
            'cidade': 'São Paulo'
        }
    },
    {
        'nome': 'Maria',
        'sobrenome': 'Pereira',
        'sexo': 'Feminino',
        'endereco': {
            'logradouro': 'Avenida Brasil',
            'numero': 456,
            'bairro': 'Centro',
            'cidade': 'Rio de Janeiro'
        }
    },
    {
        'nome': 'Ana',
        'sobrenome': 'Costa',
        'sexo': 'Feminino',
        'endereco': {
            'logradouro': 'Travessa dos Artistas',
            'numero': 789,
            'bairro': 'Vila Nova',
            'cidade': 'Belo Horizonte'
        }
    },
    {
        'nome': 'Pedro',
        'sobrenome': 'Almeida',
        'sexo': 'Masculino',
        'endereco': {
            'logradouro': 'Praça da Sé',
            'numero': 1011,
            'bairro': 'Sé',
            'cidade': 'São Paulo'
        }
    },
    {
        'nome': 'Carla',
        'sobrenome': 'Dias',
        'sexo': 'Feminino',
        'endereco': {
            'logradouro': 'Rua das Palmeiras',
            'numero': 1213,
            'bairro': 'Santa Teresa',
            'cidade': 'Recife'
        }
    },
    {
        'nome': 'Lucas',
        'sobrenome': 'Machado',
        'sexo': 'Masculino',
        'endereco': {
            'logradouro': 'Alameda dos Anjos',
            'numero': 1415,
            'bairro': 'Santo Ângelo',
            'cidade': 'Porto Alegre'
        }
    }
]

clientes_json = json.dumps(clientes)

print("clientes em dict ou objeto: ",clientes_json)
print(16 *"- - ")

novos_clientes = json.loads(clientes_json)

print("em dict novamente",novos_clientes)

print(16 *"- - ")

print(clientes[0]['nome'])

endereco_cliente_2 = clientes[4].get('endereco', {}).get('numero')

print(endereco_cliente_2)

print(clientes[1]['endereco']['cidade'])
print(clientes[1]['sobrenome'])
# pra acessar um elemento de json eu preciso transformar em dict primeiro
# mas posso fazer assim

clientes_inadimplentes = json.loads(clientes_json)
nome_inadimplente  = clientes_inadimplentes[2]['nome']
print(nome_inadimplente)

nova_lista_clientes = []

for cliente in clientes:
    dto = {
        'nome': cliente['nome'],
        'sexo': cliente['sexo'],
        'cidade_do_cliente': cliente['endereco']['cidade']
    }
    nova_lista_clientes.append(dto)
    
print(nova_lista_clientes)


print(16 *"- - ")

for cliente_nova_lista in nova_lista_clientes:
    print(cliente_nova_lista)