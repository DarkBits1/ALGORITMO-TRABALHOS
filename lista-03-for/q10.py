def main():
  limite_superior = int(input('Limite superior > '))
  limite_inferior = int(input('Limite inferior > '))
  for i in range(limite_inferior, limite_superior +1, 1):
    if i % 2 != 0:
      print(i)




main()