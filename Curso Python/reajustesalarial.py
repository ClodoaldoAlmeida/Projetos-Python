#calcula o reajuste salarial de um funcionário
sal = float(input('Digite o valor do salario do funcionário R$ '))
novosal = sal + (sal*15)/100
print('O funcionário ganhava R${:.2f} o novo salário e de R${:.2f}'.format(sal, novosal))