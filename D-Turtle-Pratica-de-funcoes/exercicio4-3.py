import turtle
import math

def tri(t, r, a):
    h = r * math.sin(math.radians(a))
    t.right(a)
    t.forward(r)
    t.left(90 + a)
    t.forward(2 * h)
    t.left(90 + a)
    t.forward(r)
    t.left(180 - a)

def desenhar_triangulo(t, q, r):
    ang = 360 / q
    for i in range(q):
        tri(t, r, ang / 2)
        t.left(ang)

def quant_triangulos(t, q, r):
    desenhar_triangulo(t, q, r)
    t.penup()
    t.forward(r * 2 + 10)
    t.pendown()

t = turtle.Turtle()
t.speed(0)

t.penup()
t.backward(150)
t.pendown()

r = 40

quant_triangulos(t, 5, r)
quant_triangulos(t, 6, r)
quant_triangulos(t, 7, r)

t.hideturtle()
turtle.mainloop()
