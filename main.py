from turtle import Screen, Turtle
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create snake
starting_positions: list[tuple[float, float]] = [(0, 0), (-20, 0), (-40, 0)]

segments: list[Turtle] = []

for pos in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)

# snake movement
game_over = False
while not game_over:
    screen.update()  # update screen here to avoid the choppy animation
    time.sleep(0.1)  # slowdown snake movement

    # segments follow the segment in front of them
    for i in range(len(segments) - 1, 0, -1):
        pos = segments[i - 1].pos()
        segments[i].goto(pos)

    segments[0].forward(20)

screen.exitonclick()
