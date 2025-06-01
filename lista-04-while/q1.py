

def main():
  lista = int(input('Quantos algarismos terá a lista? > '))
  for i in range(1, lista+1, 1):
    i = int(input('Insira o algarismo > '))
    divisores = ''
    for j in range(1, i+1, 1):
      if i % j == 0 and j != i:
        divisores += str(j)
        divisores +=  ', '
      elif j == i:
        divisores += str(j)
    print(f'{i} > divisores: {divisores}')



main()