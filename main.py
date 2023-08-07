from turtle import Screen, Turtle

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# create snake
starting_positions: list[tuple[float, float]] = [(0, 0), (-20, 0), (-40, 0)]

segments: list[Turtle] = []

for pos in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)


screen.exitonclick()
