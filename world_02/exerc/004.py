from datetime import date
now = date.today().year
year = int(input('Ano de nascimento: '))
age = now - year

print('Você tem {} em {}'.format(age, now))

if age <= 9:
  print('Classificação: Mirim')
elif age <= 14:
  print('Classificação: Infantil')
elif age <= 19:
  print('Classificação: Junior')
elif age <= 25:
  print('Classificação: Sênior')
else:
  print('Classificação: Master')