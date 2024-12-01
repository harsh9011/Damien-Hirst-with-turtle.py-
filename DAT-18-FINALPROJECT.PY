import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
colour_list =[(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 128, 0), (128, 0, 255), (0, 255, 128)]

tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_OF_dots = 101


for dot_count in range(1,number_OF_dots):
    tim.dot(20,random.choice(colour_list))
    tim.forward(50)

    if dot_count  % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
