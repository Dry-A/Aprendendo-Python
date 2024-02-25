a=15
b='bananinha'
c=82.5

formatando = 'a={} b={} c={:.1f} {} {}'.format(a,b,c,526,'salada mista')
print(formatando)


#paramentro nomeado é quando se da nome paras as coisas na criaçao das funcoes
# nome(parametro) a(argumento)
#assim que nomeamos um, temos que nomear os que vem depois e só poderá ser chamado pelo parametro

formatando_com_parametros_nomeados = 'a={var2} b={var1} c={var3:.1f} {var1} {var3}'.format(var1=a,var2=b,var3=c)
print(formatando_com_parametros_nomeados)