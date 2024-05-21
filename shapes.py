# shapes.py
from basicShape import BasicShape
import random

class Shape:
    shapes = {
        "I": [(-20, 0), (0, 0), (20, 0), (40, 0)],
        "O": [(0, 0), (20, 0), (0, 20), (20, 20)],
        "T": [(-20, 0), (0, 0), (20, 0), (0, 20)],
        "L": [(-20, 0), (0, 0), (20, 0), (20, 20)],
        "J": [(-20, 0), (0, 0), (20, 0), (-20, 20)],
        "S": [(0, 0), (20, 0), (-20, 20), (0, 20)],
        "Z": [(-20, 0), (0, 0), (0, 20), (20, 20)]
    }

    def __init__(self):
        self.shape = random.choice(list(Shape.shapes.keys()))
        self.coordinates = Shape.shapes[self.shape]
        self.blocks = [BasicShape(x, y, "blue") for x, y in self.coordinates]

    def move(self, dx, dy):
        # Check boundaries and collision with other shapes
        if not self.check_boundaries(dx, dy) or self.detect_collision(dx, dy):
            return False
        for block in self.blocks:
            block.goto(block.xcor() + dx, block.ycor() + dy)
        return True

    def check_boundaries(self, dx, dy):
        for block in self.blocks:
            new_x = block.xcor() + dx
            new_y = block.ycor() + dy
            if new_x < -300 or new_x > 300 or new_y < -400:
                return False
        return True

    def detect_collision(self, dx, dy):
        global occupied_positions
        for block in self.blocks:
            new_x = block.xcor() + dx
            new_y = block.ycor() + dy
            if (new_x, new_y) in occupied_positions:
                return True
        return False

    def add_to_occupied_positions(self):
        global occupied_positions
        for block in self.blocks:
            occupied_positions.add((block.xcor(), block.ycor()))

    def detect_floor_collision(self):
        for block in self.blocks:
            if block.ycor() <= -380:
                return True
        return False
