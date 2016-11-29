__author__ = 'student'


import turtle as tr
tr.shape('turtle')
tr.penup()
tr.goto(-200, 0)
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

koch(400,2)