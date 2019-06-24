ficha = []

while True:

  name = str(input('Nome: '))
  value_1 = float(input('Nota 1: '))
  value_2 = float(input('Nota 2: '))
  average = (value_1 + value_2) / 2

  ficha.append([name, [value_1, value_2], average])

  choice = str(input('Quer continuar? [S/N]'))

  if choice in 'Nn':
    break

print('=-=' * 10)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for index, aluno in enumerate(ficha):
  print(f'{index:<4}{aluno[0]:<10}{aluno[2]:>8}')
  
while True:
  print('-' * 35)
  student = int(input('Ver qual aluno? [999 para sair] '))
  if student == 999:
    print('Finalizando')
    break
  elif student <= len(ficha) - 1:
    print(f'Nota de {ficha[student][0]} são {ficha[student][1]}')
  else:
    print('Nº de aluno não encontrado')
