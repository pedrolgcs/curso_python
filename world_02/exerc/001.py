house = float(input('Valor da casa: '))
money = float(input('Salario do comprador: '))
years = int(input('Quantidade de anos: '))
provision = house / (years * 12)
minimum = money * 0.3

print('Casa R${:.2f} em {} anos'.format(house, years), end = ', ')
print('a prestação será de R${:.2f}'.format(provision))

if minimum <= provision:
  print('Emprestimo pode ser concedido!)
else:
  print('Emprestimo negado')


