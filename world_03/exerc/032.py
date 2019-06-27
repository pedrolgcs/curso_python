from time import sleep

def ajuda(command):
  help(command)


while True:
  command = str(input('Função ou comando > '))
  if command.upper() == 'FIM':
    break
  else:
    ajuda(command)