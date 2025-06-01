

def string_input(label):
  while True:
    try:
      palavra = input(label)
      return palavra
    except ValueError:
      input('Valor inválido. Aperte ENTER para tentar novamente.')
      string_input(label)
    except:
      input('Erro inesperado. Aperte ENTER para tentar novamente.')
 

def int_input(label):
  while True:
    try:
      valor_inteiro = int(input(label))
      return valor_inteiro
    except ValueError:
      input('Valor inválido. Aperte ENTER para tentar novamente')
    except:
      input('Erro inesperado. Aperte ENTER para tentar novamente.')

def float_input(label):
  while True:
    try:
      valor_float = float(input(label))
      return valor_float
    except ValueError:
      input('Valor inválido. Aperte ENTER para tentar novamente')
    except:
      input('Erro inesperado. Aperte ENTER para tentar novamente.')
    
def string_input_q9(label):
  while True:
    try:
      clube_letra = input(label)
      if (clube_letra != 'a' and clube_letra != 'A') and (clube_letra != 'b' and clube_letra != 'B'):
        input('Valor inválido. Aperte ENTER para tentar novamente.')
        continue
      else:
        return clube_letra
    except ValueError:
      input('Valor inválido. Aperte ENTER para tentar novamente.')
    except:
      input('Erro inesperado. Aperte ENTER para tentar novamente.')

    