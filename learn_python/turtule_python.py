# -*- coding: utf-8 -*-
# 作者: tides
# 日期: 2021/9/14

import turtle

turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(16)
turtle.pencolor('yellow')
turtle.seth(-40)

for i in range(3):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40*2/3)
turtle.done()

python = 2
"dafdjaflda"