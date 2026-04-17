p = float(input('Qual é o preço do produto? R$ '))
d = float(input('Qual é a porcentagem de desconto? '))
pd = p * (d / 100)
np = p - pd
print('O novo preço do produto de R$ {:.2f} com desconto de {}% é de R$ {:.2f}.'.format(p, d, np))
