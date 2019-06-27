def data(*nums, situation = False):
  """
  -> Função para analisar notas e situações de vários alunos
  :param nums: aceita 0 ou várias notas
  :param situation: valor opcional, indicando se deve ou não adicionar a situação
  :return: dicionário com várias informações sobre a situação do aluno
  """
  dic = {}
  dic['total'] = len(nums)
  
  if dic['total'] == 0:
    bigger = 0
    smaller = 0
    dic['average'] = 0
  else:
    bigger = nums[0]
    smaller = nums[0]
    dic['average'] = round((sum(nums) / len(nums)), 2)

  for n in nums:
    if n > bigger:
      bigger = n
    elif n < smaller:
      smaller = n
  dic['bigger'] = bigger
  dic['smaller'] = smaller
  
  if situation:
    if dic['average'] < 5:
      dic['situation'] = 'Ruim'
    elif 5 <= dic['average'] <= 7:
      dic['situation'] = 'Boa'
    else:
      dic['situation'] = 'ótima'

  return dic


resp = data(10, 7, 5.4, situation=True)

for k, v in resp.items():
  print(f'{k} = {v}')
