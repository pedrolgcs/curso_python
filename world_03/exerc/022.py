person = {}
person_list = []
avarege = sum_age = 0

while True:

  person.clear()

  person['name'] = str(input('Nome: '))

  while True:
    person['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    if person['sexo'] in 'MF':
      break
    else:
      print('Erro, informe M ou F')
  
  person['age'] = int(input('Idade: '))
  sum_age += person['age']
  
  person_list.append(person.copy())

  while True:
    choice = str(input('Quer continuar: [S/N] ')).upper()[0]
    if choice in 'SN':
      break
    else:
      print('Erro, informe S ou N')

  if choice == 'N':
    break


print('-' * 20)
print(f'A) Ao todo temos {len(person_list)} pessoas cadastradas')
avarege = sum_age / len(person_list)
print(f'A média de idade é de {avarege:.2f}')
print(f'As mulheres cadastradas foram ', end = '')
for p in person_list:
  if p['sexo'] == 'F':
    print(f'{p["name"]}', end = ', ')
print()
print(f'Lista de pessoas que estão acima da média: ')
for p in person_list:
  if p['age'] >= avarege:
    for k, v in p.items():
      print(f'{k} = {v}; ', end = '')
    print()

print('Fim')
