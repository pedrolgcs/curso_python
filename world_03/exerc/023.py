def earth(width, length):
  land = width * length
  return print(f'A área de um terro {width:.2f} x {length:.2f} é de {land:.2f}m²')


print('Controle de Terrenos')
print('-' * 10)

width = float(input('Largura (m): '))
length = float(input('Comprimento (m): '))

earth(width, length)