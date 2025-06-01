import random
def main():
  tentativa = 0
  num = int(input('Número > '))
  for i in range(1, 999999999, 1):
    tentativa = random.randint(0, 7)
    if tentativa != num:
      continue
    else:
      print(f'Achamos o número na tentativa de número {i}.')
      break



main()