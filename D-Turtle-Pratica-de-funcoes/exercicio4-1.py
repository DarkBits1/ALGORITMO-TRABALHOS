
import turtle
import math

def desenhar_linhas(tartaruga, n, comprimento, angulo):
    for _ in range(n):
        tartaruga.forward(comprimento)
        tartaruga.left(angulo)

def arco(tartaruga, raio, angulo):
    comprimento_arco = 2 * math.pi * raio * abs(angulo) / 360
    n = int(comprimento_arco / 4) + 1
    passo = comprimento_arco / n
    angulo_passo = angulo / n

    tartaruga.left(angulo_passo / 2)
    desenhar_linhas(tartaruga, n, passo, angulo_passo)
    tartaruga.right(angulo_passo / 2)

def circulo(tartaruga, raio):
    arco(tartaruga, raio, 360)


renato = turtle.Turtle()
raio = 100

renato.penup()
renato.forward(raio)
renato.left(90)
renato.pendown()

circulo(renato, raio)

turtle.mainloop()
