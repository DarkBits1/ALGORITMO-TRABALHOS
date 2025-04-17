def main():
  try:
        numero = int(input('Insira o número: '))
        verificar_primo(numero)
  except ValueError:
        print('Insira um número válido.')



def verificar_primo(numero):
  if numero <= 1:
   return print('Não é primo.')
    
  if numero == 2:
     return print('Não é primo.')
      
  if numero % 2 == 0:
   return print('Não é primo.')  
    

  for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            print('Não é primo.')
            return

  print('É primo.')







main()