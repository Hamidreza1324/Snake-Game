from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGH_SCORE_FILE = "high_score.txt"


class Scoreboard(Turtle):
    """Scoreboard displays current score, high score, and handles Game Over."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        """Load high score from file; return 0 if file not found."""
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Save high score to file."""
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        """Show current score and high score at top."""
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase current score by 1 and update display."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Display GAME OVER and current score below."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write(f"Your score: {self.score}", align=ALIGNMENT, font=FONT)

    def check_high_score(self):
        """Update and save high score if current score is higher."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
