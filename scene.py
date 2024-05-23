import os
import model
from typing import List

class SceneManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []
        self.plane = model.Plane(width // 2, height // 2)
        self.scene = self.initial_scene()

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def collision(self, object_scene: List[List]):
        for y in range(object_scene):
            for x in range(object_scene[0]):
                if self.scene[y][x] != "x" and object_scene[y][x] != "x":
                    return true


    def update(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        scene = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def initial_scene(self):
        top_bottom_border = ["-"] * self.width
        middle_rows = [["|"] + ["x"] * (self.width - 2) + ["|"] for _ in range(self.height - 2)]
        boarder_scene = [top_bottom_border] + middle_rows + [top_bottom_border]
        return boarder_scene

    def draw_scene(self):
        for line in self.scene:
            output_line = ""
            for col in line:
                output_line += col
            print(output_line)



