s = float(input('Qual é o salário do funcionário? R$ '))
a = float(input('Qual é a percetual de aumento? '))
va = s * (a / 100)
ns = s + va
print('O novo salário do funcionário é de R$ {:.2f}.'.format(ns))
