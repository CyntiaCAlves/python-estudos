import math
c1 = int(input('Qual o valor do cateto 1: '))
c2 = int(input('Qual o valor do cateto 2: '))
h = math.sqrt(c1**2 + c2**2)
print('O valor da hipotenusa é igual a {:.2f}'.format(h))
