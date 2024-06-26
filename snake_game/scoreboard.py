from turtle import Turtle
ALIGNTMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.teleport(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNTMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", move=False, align=ALIGNTMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
