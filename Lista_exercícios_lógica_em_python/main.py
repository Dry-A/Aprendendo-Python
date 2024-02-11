#15
def informar_se_esta_no_intervalo(num):
    if 100<num<200:
       return 'Está no intervalo entre 100 e 200'

#16
def calcula_media_nota(nome, nota1, nota2, nota3):
    media = (nota1+nota2+nota3) /3
    
    if media >=7:
        print(f"{nome} foi aprovado com a média {media}")
    else:
        print(f"{nome} foi reprovado pois sua média ficou abaixo de sete -  Média {media}")
    