import colorgram
import turtle as turtle_module
import random

colors=colorgram.extract('DAY_18_Hirst Painting\image.jpg',30)

listed=[]
for i in range(30):
    color=colors[i]
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    rgb=(r, g, b)
    listed.append(rgb)

tim=turtle_module.Turtle()
turtle_module.colormode(255)

tim.speed('fastest')
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.hideturtle()

no_of_dots=100

for dot_count in range(1, no_of_dots+1):
    tim.dot(20,random.choice(listed))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()