number = (
  int(input('Primeiro: ')),
  int(input('Segundo: ')),
  int(input('Terceiro: ')),
  int(input('Quarto: '))
)
print('Você digitou os valores: {}'.format(number))
print('O valor 9 apareceu {} vezes'.format(number.count(9)))
if 3 in number:
  print('O primeiro valor três apareceu na posição: {}'.format(number.index(3) + 1 ))
else:
  print('O valor três não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in number:
  if n % 2 == 0:
    print(n, end = ' ')
