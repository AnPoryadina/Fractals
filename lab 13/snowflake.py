__author__ = 'student'
import turtle as tr

tr.speed(1000)
tr.shape('turtle')
tr.penup()
tr.goto(-200, 100)
tr.pendown()

def koch(l, n):
    if n == 0:
        tr.forward(l)
        return
    elif n > 0:
        koch(l/3, n-1)
        tr.left(60)
        koch(l/3, n-1)
        tr.right(120)
        koch(l/3, n-1)
        tr.left(60)
        koch(l/3, n-1)

def turn (l, u):
    koch(l, u)
    tr.right(120)
    koch(l, u)
    tr.right(120)
    koch(l, u)
    tr.right(120)
    return

turn(400, 5)
