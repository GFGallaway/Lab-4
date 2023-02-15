#authors are Gabby and Emily
import turtle
jack=turtle.Turtle()
jack.color("yellow")

for side in range(4):
    if side==1:
        jack.color("blue")
    if side==2:
        jack.color("red")
    if side==3:
        jack.color("purple")
    jack.forward(100)
    jack.right(90)
