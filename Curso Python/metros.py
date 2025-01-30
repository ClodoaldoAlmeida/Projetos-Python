# Converte metros em centrimetros e milimetros
numero = float(input('Digite quantos metros você quer transformar: '))
centimetro = numero * 100
milimetro = numero * 1000
print('O números em metros é {} em centrimetros {:.0f} e em milimetros {:.0f}' .format(numero, centimetro, milimetro))