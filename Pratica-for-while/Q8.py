
receitas = []
despesas = []

qt_receitas = int(input("Quantas receitas? "))
for _ in range(qt_receitas):
    desc = input("Descrição da receita: ")
    valor = float(input("Valor: R$ "))
    receitas.append((desc, valor))

qt_despesas = int(input("Quantas despesas? "))
for _ in range(qt_despesas):
    desc = input("Descrição da despesa: ")
    valor = float(input("Valor: R$ "))
    despesas.append((desc, valor))

total_receitas = sum(r[1] for r in receitas)
total_despesas = sum(d[1] for d in despesas)
saldo = total_receitas - total_despesas

maior_receita = max(receitas, key=lambda x: x[1])
maior_despesa = max(despesas, key=lambda x: x[1])

print(f"Total de receitas: R$ {total_receitas:.2f}")
print(f"Total de despesas: R$ {total_despesas:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")
print(f"Maior receita: {maior_receita[0]} - R$ {maior_receita[1]:.2f}")
print(f"Maior despesa: {maior_despesa[0]} - R$ {maior_despesa[1]:.2f}")
