# calcula desconto de produto
prec = float(input('Digite o preço do produto? R$ '))
valdesc = float(input('Digite o valo do desconto em % ' ))
desc = (prec/100)*valdesc
prodcomdesc = prec-desc
print('o valor do produto inicial é de R${:.2f}, com o desconto de {:.0f}% ele passará a custar R${:.2f}'.format(prec, desc, prodcomdesc))