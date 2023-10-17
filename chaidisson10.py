# exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
km= float(input("digite a velocidade em km/h;"))
vel = 60 
multa = (km-60)*7
if vel > int("60"):
    print("voce está dentro do limite de velocidade permitido")
else:
    print(f"você ultrapassou o limite de velocidade! sua multa é de {multa} R$" )