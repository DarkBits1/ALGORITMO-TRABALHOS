#INÍCIO: 18:21 24/05/2025
#FIM: 18:33 24/05/2025

def int_number(label):
  while True:
   try:
    num = int(input(label))
    return num
   except ValueError:
    print('Valor inválido. Digite um número inteiro.')
    int_number(label)

def positive_int_number(label):
 while True:
  try:
    num = int(input(label))
    if num > 0:
     return num
    else:
     print('O número deve ser positivo.')
     positive_int_number(label)
  except ValueError:
   print('Valor inválido. Tente novamente.')
   positive_int_number(label)

def negative_int_number(label):
 while True:
  try:
    num = int(input(label))
    if num < 0:
     return num
    else:
     print('O número deve ser negativo.')
     negative_int_number(label)
  except ValueError:
   print('Valor inválido. Tente novamente.')
   negative_int_number(label)

def x_int_number(label):
 while True:
  try:
    x = int(input('Valor de x > '))
    num = int(input(label))
    if num >= x:
     return num
    else:
     print(f'O valor deve ser de no mínimo {x}.')
     x_int_number(label)
  except ValueError:
   print('Valor inválido. Tente novamente.')
   x_int_number(label)


def x_max_int_number(label):
 while True:
  try:
    x = int(input('Valor de x > '))
    num = int(input(label))
    if num <= x:
     return num
    else:
     print(f'O valor deve ser de no MÁXIMO {x}.')
     x_int_number(label)
  except ValueError:
   print('Valor inválido. Tente novamente.')
   x_int_number(label)


def interval_int_number(label):
 while True:
  try:
    x = int(input('Valor de x > '))
    y = int(input('Valor de y > '))
    num = int(input(label))
    if num >= x and num <= y:
     return num
    else:
     print(f'O valor deve ser de no mínimo {x} e no máximo {y}.')
     x_int_number(label)
  except ValueError:
   print('Valor inválido. Tente novamente.')
   x_int_number(label)

