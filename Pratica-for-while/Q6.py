
def main():
  qtd_Sessoes = int(input('Qtd sessões > '))
  volume_atual = 0
  volume_anterior = 0
  progresso = 0
  tendencia = ''
  melhor_sessao = 0
  for i in range(qtd_Sessoes):
    volume_anterior = volume_atual
    peso = float(input('Insira o peso (KG) > '))
    reps = int(input('Repetições > '))
    volume_atual = peso * reps
    if i == 0:
      volume_anterior = volume_atual
    if volume_atual > volume_anterior:
      melhor_sessao = i + 1
      progresso += 1
    elif volume_atual < volume_anterior:
      progresso -= 1
  if progresso >= 2:
    tendencia = 'Melhora.'
  elif progresso <= 1:
    tendencia = 'Melhora pequena.'
  elif progresso < 0:
    tendencia = 'Piora.'
  print(f"""
---------------------
    Melhor sessão > {melhor_sessao}
    Tendência > {tendencia}
--------------------------------
""")


main()
