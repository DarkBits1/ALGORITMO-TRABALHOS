#INÍCIO: 10:42 25/05/2025
#FINAL: 11:02 25/05/2025
from q1_number_utils import positive_int_number

def main():
  alunos = positive_int_number('Insira o total de alunos > ')
  backend = 0
  frontend = 0
  mobile = 0
  dados = 0
  total_alunos = 0
  while True:
    quantidade, area = input('Insira quantidade e área > ').split()
    area = area.lower()
    quantidade = int(quantidade)
    total_alunos += quantidade
    if area == 'b':
      backend += quantidade
    elif area == 'f':
      frontend += quantidade
    elif area == 'm':
      mobile += quantidade
    else:
      dados += quantidade
    if total_alunos >= alunos:
      break
  print(f"""
----------------------------------
    Total: {total_alunos} alunos
    Total de Backend: {backend}
    Total de Frontend: {frontend}
    Total de Mobile: {mobile}
    Total de Dados: {dados}
    Percentual de Backend: {backend / total_alunos * 100:.2f}%
    Percentual de Frontend: {frontend / total_alunos * 100:.2f}%
    Percentual de Mobile: {mobile / total_alunos * 100:.2f}%
    Percentual de Dados: {dados / total_alunos * 100:.2f}%
----------------------------------

""")
  


main()


