from datetime import date

def voter(year):
  year = date.today().year - year
  if year < 16:
    return f'Com {year} anos: Não vota'
  elif 16 <= year < 18 or year > 65:
    return f'Com {year} anos: Voto opcional'
  else:
    return f'Com {year} anos: Voto obrigatório'

year = int(input('Data de nascimento: '))
print(voter(year))