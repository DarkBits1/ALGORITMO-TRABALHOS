
def main():
  num = int(input('num > '))
  sim = 5
  for i in range(0, 9999, 1):
    sim += 6
    tentativa = int(input('tentativa > '))
    if tentativa == num:
      print('Parabéns! O número é igual!')
      break
    else:
      sim += 1



main()