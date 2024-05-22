import model
import scene


def draw_scene():
    init_scene = scene.initial_scene()
    for line in init_scene:
        output_line = ""
        for col in line:
            output_line += col
        print(output_line)


if __name__ == '__main__':
    """"
    plane = model.Plane((0, 0), 0)
    plane.fly(10, 10)
    """
    draw_scene()
