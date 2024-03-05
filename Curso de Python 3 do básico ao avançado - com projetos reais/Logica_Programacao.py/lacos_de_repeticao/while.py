contador = 0

while contador <= 100:
    
    contador += 1
    
    if contador == 7:
        print('Nao vou mostrar o 7')
        continue
    
    if 11<contador< 25:
        print('nao vou mostrar o ', contador)
        continue
    
    print(contador)
    
    if contador ==14:
        break
   
    
 
print('acabou')   