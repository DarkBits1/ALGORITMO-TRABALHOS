
def main():
  mdc = 1
  num1_ini = int(input('Número 1 > '))
  num2_ini = int(input('Número 2 > '))
  num1 = num1_ini
  num2 = num2_ini
  for i in range(1, num1+1, 1):
   for j in range(1, num1+1, 1):
    if num1 % j == 0 and num2 % j == 0:
      mdc *= j
      num1 = num1 // j
      num2 = num2 // j

      
  print(f'O valor do mdc({num1_ini}, {num2_ini}) é igual a > {mdc}')



main()