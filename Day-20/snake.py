from turtle import *
blocks = []
positions = [(0, 0), (-20, 0), (-40, 0)]
class Snake():

    def __init__(self):
        for position in positions:
            new_block = Turtle(shape="square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(position)
            blocks.append(new_block)
    def move(self):
        for num in range(len(blocks) - 1, 0, -1):
            new_x = blocks[num - 1].xcor()
            new_y = blocks[num - 1].ycor()
            blocks[num].goto(new_x, new_y)
        blocks[0].forward(20)
    def up(self):
        blocks[0].setheading(90)




