# Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.


def main():
  try:
   numero1 = float(input('Insira o primeiro número: '))
   numero2 = float(input('Insira o segundo número:'))
   menor_maior(numero1, numero2)
  except ValueError:
   print('Insira um valor válido.')
   return main()




def menor_maior(numero1, numero2):
  if (numero1 > numero2):
    return print(f'O {numero1} é o maior. O menor é o {numero2}')
  elif numero1 == numero2: 
    return print('Os números são iguais.')
  else:
    print(f'O número {numero2} é o maior. O menor é o {numero1}')
main()
