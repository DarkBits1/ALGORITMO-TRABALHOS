def validar_nota(nota):
    return 0 <= nota <= 10

def obter_notas():
    notas = []
    for i in range(3):
        nota = float(input(f'Digite a {i + 1}ª nota: '))
        while not validar_nota(nota):
            print('Nota inválida. Digite novamente.')
            nota = float(input(f'Digite a {i + 1}ª nota: '))
        notas.append(nota)
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao_aluno(media, notas):
    if 0 in notas:
        return 'Reprovado'
    elif media >= 7.0:
        return 'Aprovado'
    elif 5.0 <= media <= 6.9:
        return 'Recuperação'
    else:
        return 'Reprovado'

def main():
    notas = obter_notas()
    media = calcular_media(notas)
    situacao = situacao_aluno(media, notas)
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}')

main()
