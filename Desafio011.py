alt=float(input('Qual a altura da parede (m)?'))
lar=float(input('E a largura (m)?'))
area=(alt * lar)
tinta= area / 2
print('Com esses valores, podemos dizer que a área dessa parede é de:{:.3f} m².'.format(area))
print('Com o m² no valor de {:.3f} m², a quantidade de tinta necessária em litros, para pintar essa parede é de:\n{:.1f} L'.format(area,tinta))
