from random import randint
computer_choice = randint(0, 10)

print('''Sou seu computado...
Acabei de pensar em um palpite entre 0 e 10
Será que você consegue adivinhar qual foi ?
''')

choices = 0
while True:
  player_choice = int(input('Informe seu palpite: '))
  choices += 1
  if player_choice == computer_choice:
    break
  else: 
    if player_choice > computer_choice:
      print('Errou! Tente um número menor!: ')
    else:
      print('Errou! Tente um número maior!: ')

print('Parabéns você acertou o número {} com {} palpites'
  .format(computer_choice, choices))