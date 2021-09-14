# -*- coding: utf-8 -*-
# 作者: tides
# 日期: 2021/9/14

import turtle as t
t.penup()
t.seth(-90)
t.fd(160)
t.pendown()
t.pensize(20)
t.colormode(255)
for i in range(10):
    t.speed(1000)
    t.pencolor(25*i, 5*i, 15*i)
    t.seth(130)
    t.fd(220)
    for j in range(23):
        t.circle(-80, 10)
    t.seth(100)
    for j in range(23):
        t.circle(-80, 10)
    t.fd(220)

