import model
import scene
import threading
import sys
import keyboard

running = True


def stop_all():
    print("Stop all is called")
    global running
    running = False
    for thread in threading.enumerate():
        if thread != threading.current_thread():  # Skip the current thread
            thread.join()
    sys.exit()


if __name__ == '__main__':
    """"
    plane = model.Plane((0, 0), 0)
    plane.fly(10, 10)
    """
    scene_width = 90
    scene_height = 20
    fps = 60
    scene_manager = scene.SceneManager(scene_width, scene_height, fps)
    plane = model.Plane(90, 20, (0, scene_height // 2), fps)
    scene_manager.add_plane(plane)
    update_thread = threading.Thread(target=scene_manager.run)
    fly_thread = threading.Thread(target=plane.fly)

    # Start the threads
    update_thread.start()
    fly_thread.start()

    # Wait for the threads to finish
    update_thread.join()
    fly_thread.join()

