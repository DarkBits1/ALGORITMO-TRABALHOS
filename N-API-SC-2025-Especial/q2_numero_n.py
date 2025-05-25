#INÍCIO: 19:47 24/05/2025
#FINAL: 20:18 24/05/2025
from q1_number_utils import int_number
from q1_number_utils import positive_int_number

def main():
  pares = 0
  pares = 0
  media = 0
  maior = 0
  menor = 0
  sequencia = 0
  soma = 0
  n = positive_int_number('Valor de n > ')
  i = n
  while i >= 0:
    if sequencia >= n:
      break
    valor = int_number('Insira um valor > ')
    soma += valor
    if i == n:
       maior = valor
       menor = valor
    i -= 1
    if valor > maior:
       maior = valor
    elif valor < menor:
       menor = valor
    if valor % 2 == 0:
      pares += valor
   
    if i == 0:
         media = soma / n
         print(f"""
-------------------
  SOMA DOS NÚMEROS PARES > {pares}
  MÉDIA DOS NÚMEROS > {media:.2f}
  MENOR NÚMERO DA SEQUÊNCIA > {menor}
  MAIOR NÚMERO DA SEQUÊNCIA > {maior}
-------------------------------------

""")
         i = n
         sequencia += 1
         pares = 0
         media = 0
         soma = 0
      
    

main()