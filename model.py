import scene
import keyboard
import time
import sys
import main


class Plane:
    def __init__(self, scene_width, scene_height, position: tuple, fps):
        self.x_position, self.y_position = position
        self.representation = ["###~~~~#\\ \\", "#########\\#\\", "|\\________\\#\\______", "|###################\\",
                               "|#________###_______/", "|/########/#/", "#########/#/", "###~~~~#/#/"]
        self.scene = scene.Scene(scene_width, scene_height)
        self.scene.add_object(self.representation, position)
        self.fps = fps
        self.speed = 1

    def __str__(self):
        output = ""
        for _ in range(self.y_position):
            output += "\n"
        for line in self.representation:
            for _ in range(self.x_position):
                output += " "
            output += line + "\n"
        return output

    def fly(self):
        while main.running:
            if keyboard.is_pressed('c'):
                main.stop_all()
            for direction in ['w', 'a', 's', 'd']:
                if keyboard.is_pressed(direction):
                    self.move(direction, 1)
                    time.sleep(1 / self.fps)
                    while keyboard.is_pressed(direction):
                        time.sleep(0.01)  # Wait until the key is released
            time.sleep(0.05)  # Adjust delay as needed

    def move(self, direction, speed):
        controls = ['w', 'a', 's', 'd']
        if direction not in controls:
            return
        self.scene.clear_scene()
        if direction is 'w':
            self.y_position -= speed
        if direction is 's':
            self.y_position += speed
        if direction is 'a':
            self.x_position -= speed
        if direction is 'd':
            self.x_position += speed
        self.scene.add_object(self.representation, (self.x_position, self.y_position))


class Obstacle:
    pass

