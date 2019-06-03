cont = (
  'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
  'seis', 'sete', 'oito', 'nove', 'dez'
)

while True:
  x = int(input('Informe um número: '))
  if 0 <= x <= 10:
    break
  print('Tente novamente. ', end = '')

print(f'Você digitou o número: {cont[x]}')