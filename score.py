from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.setpos(0, 260)
        self.score = 0
        self.update_score()
        
    
    def update_score(self):
        self.write(f'Score = {self.score}', False, align=ALIGNMENT, font=FONT)

    def score_inc(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.setpos(0, 0)
        self.write('GAME OVER!', False, align=ALIGNMENT, font=FONT)