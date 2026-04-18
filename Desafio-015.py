p = float(input('Quantos quilômetros (km) foram percorridos? '))
d = int(input('Quantos dias locados? '))
vp = p * 0.15
dl = d * 60.00
tp = vp + dl
print('O total a pagar é de R$ {:.2f}'.format(tp))
