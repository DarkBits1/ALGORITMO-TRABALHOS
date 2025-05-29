def main():
  limite_superior = int(input('Limite superior > '))
  limite_inferior = int(input('Limite inferior > '))
  for i in range(limite_inferior, limite_superior +1, 1):
    if i == 1 or i == 2:
      print(i)
    else:
      divisores = 0
      for j in range(1, i+1, 1):
         if i % j == 0:
           divisores += 1
         if j == i:
           if divisores <= 2:
             print(f'{i} > é primo.')


main()