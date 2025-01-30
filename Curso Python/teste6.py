# operadores Aritimeticos
# ordem de precedencia
# ()
# **
# * / // %
# + -
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
soma = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão é {:.2f}'.format(soma, m, d), end=' >>>> ')
print('Divisão inteira {}, e potência {}' .format(di, e))


