def soma(a,b):
     #verifica se a é uma instancia de int ou float?
    assert isinstance(a,(int,float)), 'a precisa ser int ou float fii'
    assert isinstance(b,(int,float)), 'a precisa ser int ou float fii'
    return a+b

def divisao(a,b):
    assert isinstance(a, (int, float))  , 'a precisa ser int ou float'
    assert isinstance(b, (int, float))  and b != 0 , 'b precisa ser int ou float e precisa ser diferente de Zero'
    return a/b

#assert náo é pro ususario final, e sim, pra outros devs saberem