name = str(input('Informe seu nome: ')).strip().lower()

if name == 'pedro':
  print('Pedro é um belo nome')
elif name == 'isabel' or name == 'janaina':
  print('belo nome feminino')
else:
  print('Não conheço seu nome')