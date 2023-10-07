from snake import Snake
from random import randint
from turtle import Turtle

class Food(Turtle, Snake):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        
    
    def refresh(self):
        self.setpos(randint(-280, 280), randint(-280, 280))
