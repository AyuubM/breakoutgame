from turtle import Turtle
colors = ["red", "white", "blue", "green"]
import random

class Blocks(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(position)
        self.penup()

