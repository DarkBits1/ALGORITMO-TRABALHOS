
def main():
  mmc = 1
  num1 = int(input('Número 1 > '))
  num2 = int(input('Número 2 > '))
  num2_temp = num2
  num1_temp = num1
  for i in range(1, num1+1, 1):
    if (num1 % i == 0 or num2 % i == 0) and (num1 != 1 or num2 != 1):
      mmc *= i
      if num1 % i == 0:
        num1 = num1 // i
      if num2 % i == 0:
        num2 = num2 // i
      
  print(f'O valor do mmc({num1_temp}, {num2_temp}) é igual a > {mmc}')



main()

  