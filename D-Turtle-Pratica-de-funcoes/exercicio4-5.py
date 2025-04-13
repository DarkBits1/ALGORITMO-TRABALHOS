import turtle

def espiral_arquimedes():
    turtle.speed(10)
    turtle.bgcolor("white")
    turtle.pensize(2)
    
    a = 0.1  
    b = 5    
    
    for t in range(360):
        turtle.forward(a * t) 
        turtle.left(10)       
    
    turtle.done()

espiral_arquimedes()
