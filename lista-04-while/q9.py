from utils import string_input
from utils import string_input_q9
from utils import int_input
from utils import float_input

def main():
  clube_a_pontos = 0
  clube_b_pontos = 0
  prova_number = int(input('Insira o número da prova > '))
  qtd_nadadores = int(input('Insira a quantidade de nadadores > '))
  for _ in range(qtd_nadadores):
    name = string_input('Nome do atleta > ')
    classificacao = int_input('Classificação(1 a 4) > ')
    tempo = float_input('Tempo (em segundos) > ')
    clube = string_input_q9('Qual o clube(a ou b) > ')
    if clube == 'a' or clube == 'A':
      if classificacao == 1:
        clube_a_pontos += 9
      elif classificacao == 2:
        clube_a_pontos += 6
      elif classificacao == 3:
        clube_a_pontos += 4
      else:
        clube_a_pontos += 3
    if clube == 'b' or clube == 'B':
      if classificacao == 1:
        clube_b_pontos += 9
      elif classificacao == 2:
        clube_b_pontos += 6
      elif classificacao == 3:
        clube_b_pontos += 4
      else:
        clube_b_pontos += 3
  if clube_a_pontos > clube_b_pontos:
    vencedor = 'CLUBE "A"'
  elif clube_b_pontos > clube_a_pontos:
    vencedor = 'CLUBE "B"'
  else:
    vencedor = 'EMPATE'
  resultado(vencedor, clube_a_pontos, clube_b_pontos)

def resultado(vencedor, a_pontos, b_pontos):
  print(f"""
===================================
        PONTUAÇÃO DO CLUBE 'A' > {a_pontos}
        PONTUAÇÃO DO CLUBE 'B' > {b_pontos}
        CLUBE VENCEDOR > {vencedor}
===================================
""")



main()