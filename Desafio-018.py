import math
angulo = float(input('Qual o valor do ângulo: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cos = math.cos(rad)
print('Para o ângulo {:.0f}º, o valor de seno é {:.2f} e o do cosseno {:.2f}'.format(angulo, seno, cos))
