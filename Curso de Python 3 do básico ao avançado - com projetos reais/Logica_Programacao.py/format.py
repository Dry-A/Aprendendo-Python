#format
#tudo em python é um objeto. pois tudo da pra vc colocar ponto e acionar metodos

a=15
b='bananinha'
c=82.5

formatando = 'a={} b={} c={:.1f} {} {}'.format(a,b,c,526, 'salada mista')

formatando_sem_depender_da_ordem = 'a={1} b={2} c={3:.1f} {0} {4}'.format(a,b,c,526, 'salada mista')

formatando_2 = '{} {}'.format('bololo', 'haha')

print(formatando)
print(formatando_sem_depender_da_ordem)
print(formatando_2)