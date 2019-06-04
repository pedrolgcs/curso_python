words = ('aprender', 'programar', 'python', 'curso', 'gratis')

for word in words:
  print(f'\nNa palavra {word.upper()} temos: ', end='')
  for letter in word:
    if letter.lower() in 'aeiou':
      print(f'{letter}', end=' ')
