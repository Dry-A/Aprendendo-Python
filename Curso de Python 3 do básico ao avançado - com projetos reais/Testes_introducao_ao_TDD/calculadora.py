def soma(a,b):
    """Soma a e b
    >>> soma(10,20)
    30 
    
    >>> soma(-15,5)
    -10
    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: a precisa ser int ou float
    """
     #verifica se a e b é uma instancia de int ou float
    assert isinstance(a,(int,float)), 'a precisa ser int ou float'
    assert isinstance(b,(int,float)), 'b precisa ser int ou float'
    return a+b

#assert náo é pro ususario final, e sim, pra outros devs saberem

def subtrai(a,b):
    """Subtrai a e b
    
    >>> subtrai(10,8)
    2
    >>> subtrai('10', 2)
    """
    assert isinstance(a,(int,float)), 'a precisa ser int ou float'
    assert isinstance(b,(int,float)), 'b precisa ser int ou float'
    return a-b

#para rodar o teste da linha 2 diretamente aqui
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)