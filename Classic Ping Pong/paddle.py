from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,position) -> None:
        super().__init__()
        self.position = position
        self.create_paddle()
        
    def create_paddle(self):
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5,1)
        self.setpos(self.position[0],self.position[1])
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)        
            
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)        
            

        
        