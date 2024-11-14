from math import hypot
ca=float(input('Qual o comprimento do cateto adjacente?'))
co=float(input('Qual o comprimento do cateto oposto?'))
hipotenusa= hypot(ca,co)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
