import model
import time
import scene


if __name__ == '__main__':
    """"
    plane = model.Plane((0, 0), 0)
    plane.fly(10, 10)
    """
    sceneManager = scene.SceneManager(90, 20)
    sceneManager.draw_scene()
    time.sleep(1)
    plane = model.Plane(sceneManager.width, sceneManager.height, (2, sceneManager.height // 2))
    sceneManager.
    sceneManager.draw_scene()

