__author__ = 'student'
import turtle as tr

tr.speed(1000)
tr.shape('turtle')
tr.penup()
tr.goto(-200, -200)
tr.pendown()

def minkovski(l,n):
    if n == 0:
        tr.forward(l)
        return
    elif n > 0:
        minkovski(l/4, n-1)
        tr.left(90)
        minkovski(l/4, n-1)
        tr.right(90)
        minkovski(l/4, n-1)
        tr.right(90)
        minkovski(l/4, n-1)
        minkovski(l/4, n-1)
        tr.left(90)
        minkovski(l/4, n-1)
        tr.left(90)
        minkovski(l/4, n-1)
        tr.right(90)
        minkovski(l/4, n-1)

minkovski(1200, 4)
tr.mainloop()