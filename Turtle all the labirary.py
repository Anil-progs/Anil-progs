turtle.forward() 
turtle.left()
turtle.right()
turtle.backward()
turtle.exitonclick()
turtle.getscreen()
turtle.Turtle("arrow","Turtle")
turtle.penup()
turtle.pendown()
turtle.clear()
#we can also put these methods at object like if the object be windows

windows.shape("turtle")
windows.speed(0,1,2,9,10,...)
windows.circle(100)
#this is for pen color means the color of line
windows.pencolor("black")
#this is for internal of turtle color
windows.fillcolor("blue")
#this is use both for line and the internal of turtle color,first color is for line and second is for internal of turtle
windows.color("white","blue") or windows.color("blue")
#look to this example
windows.begin_fill()
windows.circle(100)
windows.end_fill()
#use to change the position of turtle 
windows.goto(x=30,y=40)
#show the Tip of pen the big ness of that 
windows.pensize(10)
#to show the turtle
windows.showturtle()
#is use to hide the turtle
windows.hideturtle()
#is one only show in black board of it True or False
windows.isvisible()
windows.isdown()
#sit up the screen of the turtle
windows.setup(width=500,height=600)
#make the back ground od screen to each color you write
windows.bgcolor("white")
#this one make the movement of turlte on the time you clear for it 
#like for 1 sec stop after move
import time
time.sleep(1) or time.sleep(0.1)
#this one will top the jap that is continue in screen it will show the screen but not the jap of it
#up to that time we update the screen after it will show it  it is like the past TV
windows.tracer(0)
screen.update()
#if you take it zero it will not show,if you take it 1 it will work and it show
windows.tracer(1)
# to write something in turtle with change it font
import turtle
tim=turtle.Turtle()
tim.write("some text",font="Time New Roman",80,"bold")
#======================================================================
#how can we we open picture in turtle:
    #for open picture in turtle 
        1:first you should change the picture in FIP from gpg 
        2:how to change it:  click on picture and with the picture with painting after save as click and get it as FIP 
            it will change to FIP


#if we use picture as turtle
import turtle
root=turtle.Screen()
root.title("Afghanistan game")
image="C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456\\forturtle.gif"
root.addshape(image)
turtle.shape(image)
root.exitonclick()
================================
#use when you put the picture in background
import turtle
root=turtle.Screen()
root.title("Afghanistan game")         
root.bgpic("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456\\forturtle.gif")
root.exitonclick()
















