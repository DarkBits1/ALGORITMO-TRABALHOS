
def main():
  digitos = 1
  num = int(input('Número > '))
  for i in range(1, num, 1):
    if num < 10:
      print(digitos)
      break
    else:
      if num // 10 >= 1:
        num = num // 10
        digitos += 1
      else:
        continue




main()