# -*- coding: utf-8 -*-
# 作者: tides
# 日期: 2021/9/14
from turtle import *

setup(900, 600, 300, 100)
penup()
bk(300)
pensize(3)
pencolor("black")
seth(90)
fd(80)
pendown()

# 开始绘画
seth(0)
fd(200)  # 屋量长
seth(250)
fd(90)   # 屋梁宽
seth(180)
fd(200)
seth(70)
fd(90)  # 斜长
penup()
seth(250)
fd(90)
pendown()
# 下方
seth(270)
fd(110)
seth(0)
fd(200)
seth(90)
fd(110)

seth(30)
fd(60)

seth(111)
fd(60)

seth(-69)
fd(60)

seth(-90)
fd(110)
seth(210)
fd(60)
# door set
seth(180)
fd(40)
# door draw
seth(90)
fd(73.2)  # 门右上角
seth(210)
fd(30)
seth(270)
fd(58.2)
# ---门
penup()
seth(90)
fd(58.2/2) # 一半门
seth(0)
fd(8)
pendown()
circle(3)
penup()
seth(180)
fd(8)
seth(90)
fd(29.1)
seth(30)
fd(30)
pendown()
# 返回门右上角原点
seth(180)
fd(40)
seth(270)
fd(73.2)
# door over

# window judge
seth(180)
fd(80)
seth(90)
penup()
fd(36.6)
pendown()

# window
fd(36.6)
seth(0)
fd(36.6)
seth(270)
fd(36.6)
seth(180)
fd(36.6)
seth(90)

fd(18.3)
seth(0)
fd(36.6)
seth(90)
fd(18.3)
seth(180)
fd(18.3)
seth(270)
fd(36.6)
# window over
penup()
fd(36.6)
seth(180)
fd(36.6)
fd(18.3)
seth(90)
fd(110)
pendown()
# roof start
for i in range(4):
    seth(0)
    fd(20)
    seth(70)
    fd(90)
    seth(0)
    fd(20)
    seth(250)
    fd(90)

seth(0)
fd(20)
seth(70)
fd(90)
seth(0)
fd(20)

# 瓦片

for i in range(2):
    penup()
    seth(250)
    fd(18)
    seth(180)
    pendown()
    for i in range(10):
        seth(220)
        circle(-16, 80)
    penup()
    seth(250)
    fd(18)
    seth(0)
    pendown()
    for i in range(10):
        seth(-40)
        circle(16, 80)


done()


