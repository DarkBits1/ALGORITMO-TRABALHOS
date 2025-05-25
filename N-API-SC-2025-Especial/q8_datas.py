#INÍCIO: 11:00 25/05/2025
#FINAL: 11:50 25/05/2025



def main():
    data1 = input("Digite a primeira data (dd mm aaaa): ").split()
    data2 = input("Digite a segunda data (dd mm aaaa): ").split()

    d1 = int(data1[0])
    m1 = int(data1[1])
    a1 = int(data1[2])

    d2 = int(data2[0])
    m2 = int(data2[1])
    a2 = int(data2[2])

    if a1 > 3000 or a2 > 3000:
        print("Ano inválido! O ano não pode ser maior que 3000.")
    else:
        total1 = a1 * 365 + m1 * 30 + d1
        total2 = a2 * 365 + m2 * 30 + d2

        if total1 > total2:
            temp = total1
            total1 = total2
            total2 = temp

        diferenca = total2 - total1

        anos = 0
        meses = 0
        dias = 0

        while diferenca >= 365:
            diferenca = diferenca - 365
            anos = anos + 1

        while diferenca >= 30:
            diferenca = diferenca - 30
            meses = meses + 1

        dias = diferenca

        if anos > 0 and meses > 0 and dias > 0:
            print(f"{anos} ano(s) e {meses} mês(es) e {dias} dia(s)")
        elif anos > 0 and meses > 0:
            print(f"{anos} ano(s) e {meses} mês(es)")
        elif anos > 0 and dias > 0:
            print(f"{anos} ano(s) e {dias} dia(s)")
        elif meses > 0 and dias > 0:
            print(f"{meses} mês(es) e {dias} dia(s)")
        elif anos > 0:
            print(f"{anos} ano(s)")
        elif meses > 0:
            print(f"{meses} mês(es)")
        elif dias > 0:
            print(f"{dias} dia(s)")
        else:
            print("0 dia(s)")

main()
