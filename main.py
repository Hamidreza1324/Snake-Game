"""
Snake Game
Created by: Hamidreza Mirzaei Danaloo
A classic Snake game in Python using the Turtle module with minor enhancements.
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Global objects
snake = None
food = None
scoreboard = Scoreboard()
game_is_on = False


def start_game(x=None, y=None):
    """Start or restart the game."""
    global snake, food, scoreboard, game_is_on

    # Reset game objects
    snake = Snake()
    food = Food()
    scoreboard.score = 0
    scoreboard.update_scoreboard()

    # Key controls
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_loop()


def game_loop():
    """Run the main game loop."""
    global snake, food, scoreboard, game_is_on
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Collision with wall
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            end_game()

        # Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                end_game()


def end_game():
    """Handle game over, show scores, update high score, enable restart."""
    global game_is_on
    game_is_on = False
    scoreboard.game_over()
    scoreboard.check_high_score()
    screen.onclick(start_game)  # click to restart


# Start first game
start_game()

screen.exitonclick()
