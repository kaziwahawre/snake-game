import random
from turtle import Turtle
colors = ["blue", "orange", "green", "red","purple","brown"]

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-320,320)
        random_y = random.randint(-320,320)
        self.color(random.choice(colors))
        self.goto(random_x,random_y)
