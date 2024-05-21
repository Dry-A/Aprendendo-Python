# Tuplas são usadas para armazenar vários itens em uma única variável.
# Tuple é um dos 4 tipos de dados internos, ou built-in em Python usados para armazenar coleções de dados, os outros 3 são List, Set e Dict, todos com qualidades e uso diferentes.
# Uma tupla é uma coleção ordenada(que nao sera alterada) e imutável e permite valores duplicados.
#Os itens sao indexados, e podem ser de qualquer tipo
# As tuplas são escritas com parênteses. Sao objets, com o tipo de dados tupla

frutas = ("abacaxi", "banana", "caqui", "maçã", "abacaxi")
print(frutas)
print(len(frutas))

minha_tupla_de_um_item = ("abacaxi",)
print(type(minha_tupla_de_um_item))

tupla_mista = ("Anete", False, 1254, 45.2, "Márcio", "Bagageiro", '0800', 7512, False)
print(tupla_mista)

construtor_tupla = tuple(("caneta", "lápis", "caderno", "borracha", "marca-texto", "fichário"))

print(construtor_tupla)

print(tupla_mista[2]) #traz o indice 2 - terceiro elemento
print(tupla_mista[-2])#segundo item de traz pra frente
print(tupla_mista[2:5])#A busca começará no índice 2 (incluído) e terminará no índice 5 (não incluído).
print(tupla_mista[:3])#Retorna do indice 0 até terceiro elemento, e nao indice 3
print(tupla_mista[-3:-1])#retorna os itens do índice -3 (incluído) o terceiro de traz pra frente  para o índice -1 (excluído)

# Lista é uma coleção que é ordenada e mutável. Permite membros duplicados.
# Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
# Set é uma coleção que não está ordenada, imutável* e não indexado. Sem membros duplicados.
# Dicionário é uma coleção que é ordenada** e mutável. Sem membros duplicados.


#verificar se 'lapis'está na tupla

if "lápis" in construtor_tupla:
    print('Sim, lápis está na tupla')


#transformando tupla em lista para mudar os valores dela

x=("agenda", "lápis", "apontador", "caderno", "borracha")
y = list(x)
y[1]="caneta"
x = tuple(y)#('agenda', 'caneta', 'apontador', 'caderno', 'borracha')
print(x)

#tuplas nao podem usar append(), primeiro tem que ser transofrmadas em lista

nova_lista= list(frutas)

nova_lista.append("ameixa")
frutas = tuple(nova_lista)

print(frutas)

print(nova_lista)

# adicionar tuplas a tuplas
frutas_novas = ("uva", )
frutas += frutas_novas

print(frutas)

#nao da pra retirar itens da tupla
nova_lista.remove("banana")
print(nova_lista)

#metodos
print(frutas.index("banana"))
print(frutas.count("abacaxi"))


