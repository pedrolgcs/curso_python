students = {}

students['name'] = str(input('Digite seu nome: '))
students['media'] = float(input('Digite sua média: '))

if(students['media'] >= 70):
  students['situation'] = 'Aprovado'
elif 5 <= students['media'] < 7:
  students['situation'] = 'Recuperação'
else:
  students['situation'] = 'Reprovado'

print('=-=' * 10)

for key, value in students.items():
  print(f'- {key} é igual a {value}')