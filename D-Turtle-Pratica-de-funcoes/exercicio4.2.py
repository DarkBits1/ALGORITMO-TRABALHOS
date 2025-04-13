
import math
import turtle

def arco(t, raio, angulo):
    tamanho_arco = 2 * math.pi * raio * abs(angulo) / 360
    n = int(tamanho_arco / 4) + 1  
    comprimento_passo = tamanho_arco / n
    angulo_passo = float(angulo) / n

    t.lt(angulo_passo / 2)
    for _ in range(n):
        t.fd(comprimento_passo)
        t.lt(angulo_passo)
    t.rt(angulo_passo / 2)

def petala(t, raio, angulo):
    for i in range(2):
        arco(t, raio, angulo)
        t.lt(180 - angulo)

def flor(t, n, raio, angulo):
    for i in range(n):
        petala(t, raio, angulo)
        t.lt(360.0 / n)

def mover(t, distancia):
    t.pu()
    t.fd(distancia)
    t.pd()

renato = turtle.Turtle()
renato.speed(0)


mover(renato, -100)
flor(renato, 7, 60.0, 60.0)

mover(renato, 100)
flor(renato, 10, 40.0, 80.0)

mover(renato, 100)
flor(renato, 20, 140.0, 20.0)

renato.hideturtle()
turtle.mainloop()
