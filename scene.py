import os

import main
import model
from typing import List, Tuple
import time
import random


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

    def add_object(self, obj: List[List], offset: Tuple[int, int]):
        offset_x, offset_y = offset
        obj_height = len(obj)
        obj_width = len(obj[0])

        if offset_x + obj_width > self.width:
            raise IndexError(f"Object exceeds scene bounds: access {offset_x} {obj_width}, boundary {self.width}")

        if offset_y + obj_height > self.height:
            raise IndexError(f"Object exceeds scene bounds: access {offset_y} {obj_height}, boundary {self.height}")

        for i, line in enumerate(obj):
            for j, pixel in enumerate(line):
                self.scene[offset_y + i][offset_x + j] = pixel

    def clear_scene(self):
        self.scene = [['x' for _ in range(self.width)] for _ in range(self.height)]

    def add_scene(self, other_scene):
        if self.width != other_scene.width or self.height != other_scene.height:
            raise ValueError("Scene dimensions must match")

        for i in range(self.height):
            for j in range(self.width):
                if self.scene[i][j] != 'x' and other_scene.scene[i][j] != 'x':
                    raise ValueError(f"Collision at {i}, {j}.\n Value in scene: {self.scene[i][j]}.\n"
                                     f"Value in otherScene: {other_scene.scene[i][j]}")
                elif other_scene.scene[i][j] != 'x':
                    self.scene[i][j] = other_scene.scene[i][j]

    def move_left(self):
        # Get the dimensions of the scene
        num_rows = len(self.scene)
        if num_rows == 0:
            return  # No rows, nothing to move
        num_cols = len(self.scene[0])

        # Iterate over each element in the scene
        for row_index in range(num_rows):
            # Shift all elements in the current row to the left
            for col_index in range(num_cols - 1):
                # Move the element to the left if possible
                if col_index + 1 < num_cols:
                    self.scene[row_index][col_index] = self.scene[row_index][col_index + 1]
                else:
                    # If moving out of bounds, remove the element
                    self.scene[row_index][col_index] = ' '  # You can use any character to represent an empty space


class SceneManager:
    def __init__(self, width, height, fps, tick_speed):
        self.width = width
        self.height = height
        self.obstacles = []
        self.scene = Scene(width, height)
        self.fps = fps
        self.plane = None
        self.tick_speed = tick_speed

    def add_plane(self, plane):
        self.plane = plane

    def run(self):
        self.scene.clear_scene()
        spawn_time = time.time()
        spawn_speed = random.uniform(2, 8)
        tick_time = time.time()
        while main.running:
            os.system('cls' if os.name == 'nt' else 'clear')
            if time.time() > tick_time + (1. / self.tick_speed):
                tick_time = time.time()
                for obst in self.obstacles:
                    obst.scene.move_left()
            if time.time() > spawn_time + spawn_speed:
                spawn_time = time.time()
                self.spawn_obstacle()
            self.update_scene()
            self.draw_scene()
            time.sleep(1. / self.fps)

    def update_scene(self):
        self.scene.clear_scene()
        if self.plane is not None:
            print("Add plane")
            self.scene.add_scene(self.plane.scene)
        for obst in self.obstacles:
            self.scene.add_scene(obst.scene)

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def draw_scene(self):
        """
        Create scene object. Add an extra layer around it.
        :return:
        """
        print('-' * (self.width + 2))
        for height in range(self.height):
            output_line = '|'
            for width in range(self.width):
                pixel = self.scene.get_pos(width, height)
                if pixel == 'x' or pixel == '#':
                    pixel = ' '
                output_line += pixel
            output_line += '|'
            print(output_line)
        print('-' * (self.width + 2))

    def spawn_obstacle(self):
        diameter = 3
        y_pos, x_pos = (random.randint(0+diameter, self.height-diameter), (self.width//2) +
                        random.randint(0+diameter, (self.width//2)-diameter))
        obst = model.Obstacle(self.width, self.height, (x_pos, y_pos), diameter)
        self.obstacles.append(obst)

