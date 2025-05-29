
def main():
  num = int(input('Número > '))
  fatorial = 1
  for i in range(num, 1, -1):
    fatorial *= i

  print(fatorial)




main()
