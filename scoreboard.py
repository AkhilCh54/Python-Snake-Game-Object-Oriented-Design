from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.write(f"SCORE : {self.score} ",align = 'center',font=('Arial',24,'normal'))
        self.ht()

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align = 'center', font=('Arial',24,'bold'))
        self.goto(0,-50)
        self.write(f"SCORE : {self.score} ", align='center', font=('Arial', 24, 'normal'))