# calcula área de uma parede e a quantidade de tinta necessária para pinta-la
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a larfura da parede: '))
area = altura*largura
print('Sua parede tem a dimenção {} x {} e sua área é de {}m'.format(altura, largura, area))
tinta = area / 2
print('Para pintar essa perede, você precisará de {}L de tinta.'.format(tinta))