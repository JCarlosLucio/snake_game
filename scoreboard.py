from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        try:
            with open("highscore.txt") as file:
                self.high_score = int(file.read())
        except IOError:
            self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def increase_score(self) -> None:
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(
            f"Score: {self.score} Highscore: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()
