from turtle import Turtle

BAR_SHAPE = "square"
SCREEN_SIZE_X = 500
SCREEN_SIZE_Y = 500
displace = [(-(SCREEN_SIZE_X/2)+10,0),((SCREEN_SIZE_X/2)-15,0)]

class Bar(Turtle):
    
    def __init__(self, PosX:str, playerName:str = "player",teamColor:str = "white"):
        super().__init__(BAR_SHAPE, 1000, True)
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.player = playerName
        self.score = 0
        self.color(teamColor)
        self.shape(BAR_SHAPE)
        self.POs = PosX
        if PosX == "right":
            self.goto(displace[1])
        elif PosX =="left":
            self.goto(displace[0])
        self.left(90)
        self.showturtle()
        self.shapesize(stretch_len=5.2,stretch_wid=0.5)
        
    def Up(self):
        if self.ycor()<(SCREEN_SIZE_Y/2):
            self.forward(15)
    def Down(self):
        if self.ycor()>-(SCREEN_SIZE_Y/2): 
            self.backward(15)