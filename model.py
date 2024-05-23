class Plane:
    def __init__(self, position: tuple, direction):
        self.x_position, self.y_position = position
        self.direction = direction
        self.representation = ["   ~~~~ \\ \\", "         \\ \\", "|\\________\\ \\______", "|                   \\",
                               "| ________   _______/", "|/        / /", "         / /", "   ~~~~ / /"]

    def __str__(self):
        output = ""
        for _ in range(self.y_position):
            output += "\n"
        for line in self.representation:
            for _ in range(self.x_position):
                output += " "
            output += line + "\n"
        return output

    def fly(self, speed, time):
        for _ in range(time):
            print(self)
            self.x_position += speed
            print("\n\n\n\n\n\n")

    def move_y(self, direction):
        self.y_position += direction
        if self.y_position < 0:
            self.y_position = 0
        if self.y_position > 10:
            self.y_position = 10

    def move_x(self, direction):
        self.x_position += direction
        if self.x_position < 0:
            self.x_position = 0
        if self.y_position > 10:
            self.y_position = 10


class Obstacle:
    pass

