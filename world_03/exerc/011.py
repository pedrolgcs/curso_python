numbers = list()
par = list()
impar = list()

while True:
  n = int(input('Digite um número: '))
  numbers.append(n)
  if(n % 2 == 0):
    par.append(n)
  else:
    impar.append(n)
  while True:
    choice = str(input('Quer continuar? [S/N]: '))
    if choice in ('SsNn'):
      break
  if choice in 'Nn':
    break

print(f'Lista completa: {numbers}')
print(f'Pares: {par}')
print(f'Impares: {impar}')