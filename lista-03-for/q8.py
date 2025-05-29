def main():
  multiplo = 0
  n = int(input('n > '))
  limite_superior = int(input('Limite superior > '))
  limite_inferior = int(input('Limite inferior > '))
  for i in range(1, limite_superior +1, 1):
      multiplo = n * i
      if multiplo >= limite_inferior and multiplo <= limite_superior:
        print(multiplo)



main()