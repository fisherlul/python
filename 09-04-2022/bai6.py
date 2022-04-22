import turtle as t

def draw_square(border, size):
    t.pensize(border)
    t.forward(size / 2)
    t.right(90)
    t.forward(size / 2)
    for i in range(4):
        t.right(90)
        t.forward(size)
    t.backward(size/2)
    t.left(90)
    t.backward(size / 2)
    
draw_square(1, 100)
draw_square(3, 150)