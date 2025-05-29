def main():
  a_zero = int(input('A0 > '))
  limite = int(input('Limite > '))
  r = int(input('R > '))
  variavel = a_zero
  for i in range (a_zero, limite, r):
    if variavel < limite:
     print(variavel)
     variavel *= r
    else:
      break



main()