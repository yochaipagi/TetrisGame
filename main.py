import time
from turtle import Screen
from shapes import Shape

# Global set to track occupied positions
occupied_positions = set()

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Tetris")
screen.setup(width=600, height=600)  # Adjusted height to 600
screen.tracer(0)

# Create the first shape
current_shape = Shape(occupied_positions)

# Move the shape down at a regular interval
def move_shape():
    global current_shape
    if current_shape.detect_floor_collision() or current_shape.detect_collision(0, -20, occupied_positions):
        current_shape.add_to_occupied_positions(occupied_positions)
        current_shape = Shape(occupied_positions)
        if current_shape.detect_collision(0, 0, occupied_positions) or current_shape.detect_ceiling_collision():
            screen.bye()  # End game if new shape collides immediately (game over)
            return
    else:
        current_shape.move(0, -20)
    screen.update()
    screen.ontimer(move_shape, 500)

# Define functions to move the shape left, right, and down
def move_left():
    current_shape.move(-20, 0)
    screen.update()

def move_right():
    current_shape.move(20, 0)
    screen.update()

def move_down():
    current_shape.move(0, -20)
    screen.update()

# Start the game
move_shape()

# Bind the arrow keys to move the shape left, right, and down
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")

# Exit the game when the screen is clicked
screen.exitonclick()
