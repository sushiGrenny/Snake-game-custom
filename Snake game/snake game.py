import turtle
import time
import random
import pygame
from pygame import mixer
import pygame_menu
import tk as TK

score=0
highscore=0

delay= 0.1

mixer.init()
mixer.music.load('egypt.mp3')
mixer.music.play()

wn= turtle.Screen()
wn.title("Snake GAme")
wn.bgcolor("green")
wn.setup(width= 600, height= 600 )
wn.bgpic('desert1.GIF')
wn.tracer(0)

head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#000000")
head.penup()
head.goto(0,0)
head.direction = "stop"

food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#780000")
food.penup()
food.goto(0,100)

segments = []

pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.ht()
pen.goto(0,250)
pen.write("score: 0   High-score: 0", align="center", font= ("Ariel", 24, "normal"))

#functions
    
global bigfood
bigfood =turtle.Turtle()
bigfood.speed(0)
bigfood.shape("circle")
bigfood.color("blue")
bigfood.penup()
bigfood.goto(1000,1000)
bigfood.shapesize(3)

#def notsobigfood():
    #if head.distance(bigfood)<20:
        #bigfood.goto(1000,1000)


def go_up():
    if head.direction != "down":
        head.direction= "up"

def go_down():
     if head.direction != "up":
         head.direction= "down"

def go_right():
     if head.direction != "left":
         head.direction= "right"

def go_left():
     if head.direction != "right":
         head.direction= "left"
     

def move():
    if head.direction== "up":
        y= head.ycor()
        head.sety(y +20)

    if head.direction== "down":
        y= head.ycor()
        head.sety(y - 20)

    if head.direction== "right":
        x= head.xcor()
        head.setx(x +20)

    if head.direction== "left":
        x= head.xcor()
        head.setx(x - 20)

#def pause():
    #if head.direction== "up":
        #y= head.ycor()
        #head.sety(y + 0)

    #if head.direction== "down":
        #y= head.ycor()
        #head.sety(y - 0)

    #if head.direction== "right":
        #x= head.xcor()
        #head.setx(x + 0)

    #if head.direction== "right":
       # x= head.xcor()
        #head.setx(x - 0)

#speed = 1
#def incspeed():
    #global speed
    #speed += 1


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
#wn.onkeypress(pause, "p")



#Main game loop

while True:

   # pause()
    wn.update()

    if head.distance(food)<20:
        x= random.randint(-280,280)
        y= random.randint(-280,280)
        food.goto(x,y)


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("triangle")
        new_segment.color("#57574d")
        new_segment.penup()
        segments.append(new_segment)

        score = score + 10
        if score> highscore:
            highscore = score
        pen.clear()
        pen.write("score: {}  Highscore: {}".format(score, highscore), align = "center",font= ("Courier", 24, "normal"))
        pb = highscore


        if score%50 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            bigfood.goto(999,999)
        if score%50 == 0 and score> 0:
            x= random.randint(-270,270)
            y= random.randint(-270,270)
            bigfood.goto(x,y)

        

        #score = score + 20
        #if score> highscore:
            #highscore = score
        #pen.clear()
        #pen.write("score: {}  Highscore: {}".format(score, highscore), align = "center",font= ("Courier", 24, "normal"))
        #pb = highscore   


    
    for i in range(len(segments)-1, 0, -1):
        x= segments[i-1].xcor()
        y= segments[i-1].ycor()
        segments[i].goto(x,y)



    if len(segments) >0 :
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)
    
    if head.xcor()>290 or head.xcor()< -290 or head.ycor()>290 or head.ycor()< -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        pen.clear()
        score = 0
        highscore = pb 
        pen.write("score: {}  Highscore: {}".format(score, highscore), align = "center",font= ("Courier", 24, "normal"))
        if score> highscore:
            highscore = score
        pen.clear()
        pen.write("score: {}  Highscore: {}".format(score, highscore), align = "center",font= ("Courier", 24, "normal"))


        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()


    move()
    

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"


            pen.clear()
            score = 0
            highscore = pb 
            pen.write("score: {}  Highscore: {}".format(score, highscore), align = "center",font= ("Courier", 24, "normal"))
            if score> highscore:
                highscore = score
            pen.clear()
            pen.write("score: {}  Highscore: {}".format(score, highscore), align = "center",font= ("Courier", 24, "normal"))

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            

    time.sleep(delay)

wn.mainloop()