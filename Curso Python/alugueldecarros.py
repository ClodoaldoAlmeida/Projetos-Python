km = float(input('Digite a quantidade de quilometros percorrido pelo carro: '))
dias = int(input('Digite a quantidade de dias usados com o carro: '))
total = (dias*60)+(km*0.15)
print('O valor a ser pago e de R$: {:.2f}'.format(total))