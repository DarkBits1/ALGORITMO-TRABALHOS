#INÍCIO: 11:55 25/05/2025
#FINAL: 12:29 25/05/2025
def main():
  colaboracao_atual = 0
  maior_colaboracao = 0
  menor_colaboracao = 0
  maior_premio = 0
  menor_premio = 0
  i = 1
  colaboracao_anterior = 0
  total_colaborado = 0
  amigos = 0
  premio_total = float(input('Qual foi o prêmio da mega-sena? > '))
  while i != 0:
    colaboracao_anterior = colaboracao_atual
    colaboracao_atual = float(input('Quanto esse amigo colaborou > '))
    if colaboracao_atual == 0:
      break
    else:
      amigos += 1
      total_colaborado += colaboracao_atual
    if colaboracao_atual != 0 and colaboracao_atual > colaboracao_anterior:
      maior_colaboracao = colaboracao_atual
    if amigos == 1 or colaboracao_atual < menor_colaboracao:
      menor_colaboracao = colaboracao_atual
  premio_liquido = premio_total - (premio_total * 0.2)
  maior_premio = (maior_colaboracao / total_colaborado) * premio_liquido
  menor_premio = (menor_colaboracao / total_colaborado) * premio_liquido

  print(f"""
------------------------------
        MAIOR PRÊMIO INDIVIDUAL > R$ {maior_premio:.2f}
        MENOR PRÊMIO INDIVIDUAL > R$ {menor_premio:.2f}
---------------------------------------

""")
  
main()