person = {}

person['name'] = str(input('Nome: '))
person['year'] = int(input('Ano de Nascimento: '))
person['work'] = int(input('Carteira de trabalho (0 não tem): '))

if(person['work'] != 0):
  person['year_work'] = int(input('Ano de contratação: '))
  person['salary'] = float(input('Salário: '))

print('-' * 20)

for key, value in person.items():
  print(f'- {key} tem o valor {value}')

print('-' * 20)
