"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
#i = inicio
#f = fim
#p = passo
cidade = "Nova Vitoria"
print(cidade[2:])#pega do indice 2(n) até o fim - toria
print(cidade[2:5])#pega do indice 2(n) até o indice 5(sem incluir o indice 5 - tor)
print(cidade[:5])#pega do inicio até o indice 5(sem incluir o indice 5 - tor)
print(len(cidade[:5]))#pega do inicio até o indice 5(sem incluir o indice 5 - tor)

print(cidade[1:7:2])#oaV

print(cidade[0:len(cidade):2]) #Nv ioi
print(cidade[::-1]) #do inicio ao fim , pegando de traz pra frente - airotiV avoN
print(cidade[-1:-10:-1]) #artVa

print(len(cidade))

