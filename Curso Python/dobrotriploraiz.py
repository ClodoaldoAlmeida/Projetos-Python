# mostra o dobro o triplo e a raiz quadrada de um número
numero = int(input('Digite um numero: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('O numero é {}, Seu dobro é {}. \nSeu triplo é {}. \nSua Raiz Quadrada é {:.2f}' .format(numero, dobro, triplo, raiz))