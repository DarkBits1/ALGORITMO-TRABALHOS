

import string
def main():
  print('SEJA BEM-VINDO!')
  senha = input('INSIRA SUA SENHA: ')
  caracteres(senha)
  maiuscula(senha)
  minuscula(senha)
  numero(senha)
  caractere_especial(senha)
  print('SENHA ACEITA. BEM VINDO.')
def caracteres(senha):
  if (len(senha) >= 8):
    return print('SENHA COM NO MÍNIMO 8 CARACTERES INSERIDA. MUITO BEM.')
  else:
     print('SENHA NAO POSSUI 8 OU MAIS CARACTERES') 
     print('Tente novamente.')
     return main()
  

def maiuscula(senha):

  if any(c.isupper() for c in senha):
    return print('Senha contém letra maiúscula.')
  else:
    print('SENHA NAO CONTEM LETRA MAIÚSCULA.')
    print('Tente novamente.')
    return main()
   

def minuscula(senha):
   if any(c.islower() for c in senha):
      return print('Senha contém letra minúscula')   
   else:
      print('Senha não contem letra minúscula.')
      print('Tente novamente.')
      return main()
   
def numero(senha):
   if any(char.isdigit() for char in senha):
      print('Senha possui números. Válida.')

   else: 
      print('Sua senha não possui números. ')
      print('Tente novamente.')
      return main()
      
def caractere_especial(senha):
   if any(char in string.punctuation for char in senha):
      return print('Sua senha possui caracteres especiais.')

   else:
    print('Insira um caractere especial na senha.')
    return main()
   



main()
