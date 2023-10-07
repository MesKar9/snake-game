from turtle import Turtle

class Snake:
    def __init__(self):
        self.turtles = []
        self.xcor = 20
        self.turtle_objects()
        self.head = self.turtles[0]
    
    def turtle_objects(self):
        for i in range(3):
            self.new_turtle = Turtle()
            self.new_turtle.penup()
            self.new_turtle.shape('square')
            self.new_turtle.color('white')
            self.new_turtle.setpos(self.xcor, 0)
            self.turtles.append(self.new_turtle)
            self.xcor -= 20

    def not_stop_motion(self):
        for i in range(len(self.turtles)-1, 0, -1):
            self.new_x = self.turtles[i - 1].xcor()
            self.new_y = self.turtles[i - 1].ycor()
            self.turtles[i].setpos(self.new_x, self.new_y)
        
        self.turtles[0].forward(20)

    def move_up(self):
        if self.turtles[0].heading() != 90 and self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)
    
    def move_down(self):
        if self.turtles[0].heading() != 90 and self.turtles[0].heading() != 270:
            self.turtles[0].setheading(270)

    def move_left(self):
        if self.turtles[0].heading() != 0 and self.turtles[0].heading() != 180:
            self.turtles[0].setheading(180)

    def move_right(self):
        if self.turtles[0].heading() != 0 and self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)
    
    def growing_snake(self):
        self.new_turtle = Turtle()
        self.new_turtle.hideturtle()
        self.new_turtle.penup()
        self.new_turtle.shape('square')
        self.new_turtle.color('white')
        self.last_xcor = self.turtles[len(self.turtles) - 1].xcor()
        self.last_ycor = self.turtles[len(self.turtles) - 1].ycor()
        self.new_turtle.setpos(self.last_xcor, self.last_ycor)
        self.turtles.append(self.new_turtle)
        self.new_turtle.showturtle()
        
        