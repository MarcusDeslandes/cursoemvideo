from math import radians, sin, cos, tan
a=float(input('Qual o valor do ângulo?'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O valor do ângulo é {}. Com isso os valores de:\nseno é {:.2f}\ncosseno é {:.2f}\ntangente é {:.2f}.'.format(a, s, c, t))