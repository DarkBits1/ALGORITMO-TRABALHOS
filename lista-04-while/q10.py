from utils import int_input
from utils import float_input

def main():
  bagagem_total = 0
  passageiro_quant = 0
  peso_container_total = 0
  containers_number = int_input('Insira a quantidade de containers > ')
  for i in range(1, containers_number+1, 1):
    peso_container = float_input(f'Peso do container {i} > ')
    peso_container_total += peso_container
  input('Agora os dados dos passageiros serão lidos. Aperte ENTER para continuar.')
  for i in range(1, 999999, 1):
    bilhete = int_input(f'Número do bilhete do passageiro {i} > ')
    if bilhete == 0:
      break
    else:
      passageiro_quant += 1
    bagagem = int_input(f'Quantas bagagens o passageiro {i} estará levando? > ')
    bagagem_total += bagagem
  peso_bagagem = bagagem_total * 10
  peso_passageiros = 70 * passageiro_quant
  resultado(peso_bagagem, peso_container_total, peso_passageiros, passageiro_quant)



def resultado(bagagem, container, passageiro_peso, passageiro_quant):
  peso_total_parcial = bagagem + passageiro_peso + container 
  quant_sobrando = 500000 - peso_total_parcial
  litros = quant_sobrando / 1.5
  if litros < 10000:
    liberacao = 'NEGADA.'
  else:
    liberacao = 'LIBERADA.'
  print(f"""
--------------------------------------
    Quantidade de passageiros > {passageiro_quant}
    Quantidade total de volume de bagagem > {bagagem} KG
    Peso dos passageiros > {passageiro_peso} KG
    Peso da carga > {container} KG
---------------------------------------

O MÁXIMO DE COMBUSTIVEL QUE A AERONAVE SUPORTARÁ É {litros} L

LOGO, O VÔO ESTÁ {liberacao}
-----------------------------
""")
main()