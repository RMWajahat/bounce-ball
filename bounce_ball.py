from turtle import Turtle
import ballrod
from random import choice

BALL_SHAPE = "circle"
BALL_COLOR = "#1E90FF"


class BounceBall(Turtle):
    
    
    def __init__(self, shape: str = BALL_SHAPE, undobuffersize: int = 1000, visible: bool = True):
        super().__init__(shape, undobuffersize, visible)
        self.GAME_OVER = False
        self.speed("fastest")
        self.penup()
        self.color(BALL_COLOR)
        self.ball_angles = [35,-35,145,-145]
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.setheading(choice(self.ball_angles))
    
    def wall_collision(self):
        if self.xcor()<(-(ballrod.SCREEN_SIZE_X)/2)+20 or self.xcor()>((ballrod.SCREEN_SIZE_X)/2)-20:
            self.GAME_OVER= True
        if self.ycor()<(-(ballrod.SCREEN_SIZE_Y)/2)+10 or self.ycor()>((ballrod.SCREEN_SIZE_Y)/2)-10:
            if int(self.heading()) in range(270,361):
                self.setheading(35)
                self.forward(30)
            elif int(self.heading()) in range(0 ,91):

                self.setheading(325)
                self.forward(30)
            elif int(self.heading()) in range(90 ,181):

                self.setheading(215)
                self.forward(30)
            elif int(self.heading()) in range(180 ,271):
                self.setheading(125)
                self.forward(30)
            
            
            
    def bar_collision(self,bar: object):
        if self.distance(bar)<25 or self.distance((bar.xcor(),bar.ycor()+30))<25 or self.distance((bar.xcor(),bar.ycor()-30))<25:
            if bar.xcor()<0 and bar.POs == "left":
                self.setheading(choice([self.ball_angles[0],self.ball_angles[1]]))
                bar.score+=1
            elif bar.xcor()>0 and bar.POs =="right":
                self.setheading(choice([self.ball_angles[2],self.ball_angles[3]]))
                bar.score+=1
            
            
    def move(self):
        self.wall_collision()
        self.forward(15)
            
            
            