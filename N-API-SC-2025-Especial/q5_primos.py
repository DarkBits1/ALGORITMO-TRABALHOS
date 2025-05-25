#INÍCIO: 21:50 24/05/2025
#FINAL: 22:01 24/05/2025

from q1_number_utils import int_number


def main():
  n = int_number('Valor de N > ')
  m = int_number('Valor de M > ')
  while n <= m:
    if primo_verificador(n) == 1:
      print(f'{n} não é primo.')
      n += 1
    else:
      print(f'{n} é primo.')
      n += 1








def primo_verificador(n):
  divisores = 0
  i = 1
  while i <= n:
    if n % i == 0:
      divisores += 1
      i += 1
    else:
      i += 1
  if divisores > 2:
    resultado = 1
    return resultado
  else:
    resultado = 0
    return resultado


main()