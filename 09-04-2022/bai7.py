import turtle as t

def square(size, border):
    for i in range(4):
        t.pensize(border)
        t.forward(size)
        t.right(90)

square(100, 1)
for i in range(1):
    t.right(45)
    t.left(90)
    
    t.backward(50)
    square(100, 1)
