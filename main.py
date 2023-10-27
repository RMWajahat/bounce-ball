from turtle import Screen
import ballrod
from bounce_ball import BounceBall
from time import sleep


SCREEN_BG = "#000013"


screen = Screen()
screen.setup(width = ballrod.SCREEN_SIZE_X+20,height = ballrod.SCREEN_SIZE_Y+20)
screen.bgcolor(SCREEN_BG)
screen.title("Bounce_it Back")
screen.listen()

def action_listeners():
    screen.onkey(bar_left.Up,"w")
    screen.onkey(bar_left.Down,"s")
    screen.onkey(bar_right.Up,"Up")
    screen.onkey(bar_right.Down,"Down")






ball = BounceBall()


bar_left = ballrod.Bar(PosX="left", playerName="Wajahat",teamColor = "green")
bar_right = ballrod.Bar(PosX="right", playerName="Ali",teamColor = "red")

while not ball.GAME_OVER:
    ball.move()
    action_listeners()
    ball.bar_collision(bar_left)
    ball.bar_collision(bar_right)
    sleep(0.1)
    
ball.hideturtle()
bar_left.hideturtle()
bar_right.hideturtle()
ball.setpos(-100,100)
ball.color("red")
if bar_left.score>bar_right.score:
    ball.write(f"{bar_left.player} wins",font=("Arial",24,"bold"))
elif bar_left.score==bar_right.score:
    ball.write(f"Oohh! That's a tie",font=("Arial",24,"bold"))
else:
    ball.write(f"{bar_right.player} wins",font=("Arial",24,"bold"))
ball.color("#1E90FF")
ball.home()
ball.write(f"Scores\n\n{bar_left.player}  :  {bar_left.score}\n{bar_right.player}  :  {bar_right.score}",align="Center",font=("monospace",14,"bold"))


print("GAME is Over")



    
    
    
screen.exitonclick()
