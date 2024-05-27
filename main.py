import model
import time
import scene


if __name__ == '__main__':
    """"
    plane = model.Plane((0, 0), 0)
    plane.fly(10, 10)
    """
    sceneManager = scene.SceneManager(90, 12)
    sceneManager.draw_scene()
    time.sleep(1)
    sceneManager.scene.add_object(sceneManager.plane.representation, (sceneManager.plane.y_position, sceneManager.plane.x_position))
    sceneManager.draw_scene()
    time.sleep(1)

