__author__ = 'student'
import turtle as tr

tr.speed(100000)
tr.shape('turtle')
tr.penup()
tr.goto(-200, -100)
tr.pendown()

def levi(l,n):
     if n == 0:
        tr.forward(l)
        return
     elif n > 0:
        tr.left(45)
        levi(l*(2)**0.5/2, n-1)
        tr.right(90)
        levi(l*(2)**0.5/2, n-1)
        tr.left(45)

levi(400,7)
tr.mainloop()
