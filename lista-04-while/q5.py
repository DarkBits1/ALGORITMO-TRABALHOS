def main():
  x = int(input('X > '))
  n = int(input('N > '))
  for i in range(n, 1, -1):
    x = x / i
  print(x)
main()