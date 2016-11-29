__author__ = 'student'
import turtle as tr

tr.speed(100000)
tr.shape('turtle')
tr.penup()
tr.goto(-100, 0)
tr.pendown()

def dragon(l, n, s):
    if n == 0:
        tr.forward(l)
        return
    elif n > 0:
        if s%2 == 0:
            tr.right(45)
            dragon(l/(2)**0.5, n-1, s)
            tr.left(90)
            dragon(l/(2)**0.5, n-1, s+1)
            tr.right(45)
        else:
            tr.left(45)
            dragon(l/(2)**0.5, n-1, s+1)
            tr.right(90)
            dragon(l/(2)**0.5, n-1, s)
            tr.left(45)


dragon(300, 14, 0)
tr.mainloop()
