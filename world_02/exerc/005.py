from random import choice
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']
computer_choice = choice(itens)

while True:
  print(''' Suas opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
  ''')
  choice = int(input('Qual sua jogada? '))
  if choice <= 2:
    player_choice = itens[choice]
    break

print('JO')
sleep(0.5)
print('kEN')
sleep(0.5)
print('PO!!!')

print('-=' * 11)
print('Computador jogou {}'.format(computer_choice))
print('Jogador jogou {}'.format(player_choice))
print('-=' * 11)

# * Pedra
if computer_choice == 'Pedra':
  if player_choice == 'Pedra':
    print('Jogo empatado')
  elif player_choice == 'Papel':
    print('Jogador venceu!')
  else:
    print('Computador venceu!')

# * Papel
elif computer_choice == 'Papel':
  if player_choice == 'Papel':
    print('Jogo empatado')
  elif player_choice == 'Pedra':
    print('Jogador venceu!')
  else:
    print('Computador venceu!')

# * Tesoura
else:
  if player_choice == 'Tesoura':
    print('Jogo empatado')
  elif player_choice == 'Papel':
    print('Computador venceu!')
  else:
    print('Jogador venceu!')