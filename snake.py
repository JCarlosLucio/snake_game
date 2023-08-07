from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS: list[tuple[float, float]] = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self.create()

    def create(self) -> None:
        for pos in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self) -> None:
        for i in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[i - 1].pos()
            self.segments[i].goto(pos)

        self.segments[0].forward(MOVE_DISTANCE)
