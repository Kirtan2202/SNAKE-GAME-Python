from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.updated_score()
        
        
    def updated_score(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT, move = False)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = ALIGNMENT, font = FONT, move = False)
        
          
    def increase_score(self):
        self.clear()
        self.score += 1
        self.updated_score()