import random
import turtle
import time

def up():
    bread.setheading(90)
    bread.forward(30)
def down():
    bread.setheading(270)
    bread.forward(30)
def left():
    bread.setheading(180)
    bread.forward(30)
def right():
    bread.setheading(0)
    bread.forward(30)

def give_x_y(event):
    x = event.x - 240
    y = 180 - event.y

def move(event):
    turtle.pos()
    x = turtle.xcor()
    y = turtle.ycor()
    x1 = x - 240
    y1 = 180 - y
    bread.goto(x, y)

def exchange(event):
    #坐标转换
    x = event.x - 240
    y = 180 - event.y

playground = turtle.Screen()
playground.register_shape('dog.gif')
playground.register_shape('bread.gif')
playground.onkey(up, 'Up')
playground.onkey(down, 'Down')
playground.onkey(left, 'Left')
playground.onkey(right, 'Right')
playground.listen()



writer = turtle.Turtle()
writer.color('brown')
writer.hideturtle()
writer.penup()
writer.home()
writer.write("肉包子扔狗", align='center', font=("Comic Sans MS", 50, 'bold'))
writer.goto(0, -50)
writer.write("有去无回", align='center', font=("Comic Sans MS", 20, 'bold'))
time.sleep(2)

writer.clear()

dog = turtle.Turtle()
dog.shape('dog.gif')
dog.speed(0)
dog.penup()
dog.goto(random.randint(-200, 200), random.randint(-200, 200))
dog.pendown()
dog.pensize(3)
dog.color('blue')

bread = turtle.Turtle()
bread.shape('bread.gif')
bread.penup()
bread.goto(random.randint(-200, 200), random.randint(-200, 200))
bread.pendown()
bread.pensize(3)
bread.color('green')


while True:
     dog.setheading(dog.towards(bread))
     dog.forward(5)
     if dog.distance(bread) < 2:
         playground.clear()
         break
turtle.mainloop()




