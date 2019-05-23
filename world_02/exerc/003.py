from datetime import date
now = date.today().year
year = int(input('Em qual ano você nasceu? '))
age = now - year

print('você tem {} anos de idade em {}'.format(age, now))
if age == 18:
  print('você precisa de alistar imediatamente')
elif age < 18:
  print('Você aidna não tem 18 anos, ainda faltam {} anos'.format(18 - age))
  print('Seu alistamento vai ser em {} ano'.format(now + (18 - age)))
else:
  print('Você já deveria ter se alistado a {} anos'.format(age - 18))
  print('Você deveria ter ser alistado em {}'.format(now - (age - 18)))
