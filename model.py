import scene


class Plane:
    def __init__(self, scene_width, scene_height, position: tuple):
        self.x_position, self.y_position = position
        self.representation = ["   ~~~~ \\ \\", "         \\ \\", "|\\________\\ \\______", "|                   \\",
                               "| ________   _______/", "|/        / /", "         / /", "   ~~~~ / /"]
        self.scene = scene.Scene(scene_width, scene_height)
        self.scene.add_object(self.representation, position)

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
            self.x_position += speed

    def move_y(self, direction):
        self.scene.clear_scene()
        self.y_position += direction
        self.scene.add_object(self.representation, (self.x_position, self.y_position))

    def move_x(self, direction):
        self.scene.clear_scene()
        self.x_position += direction
        self.scene.add_object(self.representation, (self.x_position, self.y_position))


class Obstacle:
    pass

