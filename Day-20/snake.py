from turtle import *
positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for position in positions:
            self.add_block(position)
    def add_block(self, position):
        new_block = Turtle(shape="square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.blocks.append(new_block)

    def extend(self):
        self.add_block(self.blocks[-1].position())


    def move(self):
        for num in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[num - 1].xcor()
            new_y = self.blocks[num - 1].ycor()
            self.blocks[num].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



