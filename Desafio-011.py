l = float(input('Qual é a largura da parede? '))
h = float(input('Qual é a altura da parede? '))
a = l * h
t = a / 2
print('A área da parede é de {:.2f}m².'.format(a))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(t))
