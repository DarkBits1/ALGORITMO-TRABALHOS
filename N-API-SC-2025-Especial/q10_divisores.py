def main():
  a = int(input('Valor de A > '))
  b = int(input('Valor de B > '))
  if a < 0 or b < 0:
    print('Insira um valor positivo para os números.')
    main()
  else:
    diferenca = b - a
    if diferenca < 11:
      print('B deve ser pelo menos 11 unidades maior que A.')
    else:
     n = a
     while True:
      
      divisores(n)
      n += 1
      if n > b:
        break

def divisores(n):
  divisores = 0
  i = 1
  while i <= n:
    if n % i == 0:
      divisores += 1
    i += 1
  return print(f'{n}({divisores})')
    
main()
