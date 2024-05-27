import os
import model
from typing import List, Tuple
import time


class Scene:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scene = [['x' for _ in range(width)] for _ in range(height)]

    def get_pos(self, width, height):
        if width < 0 or width >= self.width:
            raise ValueError("Out of bound request")
        if height < 0 or height >= self.height:
            raise ValueError("Out of bound request")
        return self.scene[height][width]

    def add_object(self, obj: List[List], offset: Tuple):
        offset_x, offset_y = offset
        for i, line in enumerate(obj):
            for j, pixel in enumerate(line):
                self.scene[offset_y + i][offset_x + j] = pixel

    def clear_scene(self):
        self.scene = [['x' for _ in range(self.width)] for _ in range(self.height)]


class SceneManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []
        self.plane = model.Plane(width, height, (4, 3))
        self.scene = Scene(width, height)

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def collision(self, object_scene: List[List]):
        for y in range(object_scene):
            for x in range(object_scene[0]):
                if self.scene[y][x] != "x" and object_scene[y][x] != "x":
                    return True

    def update(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        scene = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def draw_scene(self):
        """
        Create scene object. Add an extra layer around it.
        :return:
        """
        print('-' * (self.width+2))
        for height in range(self.height):
            output_line = '|'
            for width in range(self.width):
                pixel = self.scene.get_pos(width, height)
                if pixel == 'x':
                    pixel = ' '
                output_line += pixel
            output_line += '|'
            print(output_line)
        print('-' * (self.width+2))




