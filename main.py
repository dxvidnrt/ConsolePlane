import model
import scene
import threading
import sys
import keyboard

running = True
threads = []


def stop_all():
    global running
    running = False
    for thread in threading.enumerate():
        if thread.ident in threads and thread.is_alive():
            thread.join()


if __name__ == '__main__':
    """"
    plane = model.Plane((0, 0), 0)
    plane.fly(10, 10)
    """
    scene_width = 90
    scene_height = 20
    fps = 60
    tick_speed = 1
    scene_manager = scene.SceneManager(scene_width, scene_height, fps, tick_speed)
    plane = model.Plane(90, 20, (0, scene_height // 2), fps)
    scene_manager.add_plane(plane)
    update_thread = threading.Thread(target=scene_manager.run)
    threads.append(update_thread.ident)
    fly_thread = threading.Thread(target=plane.fly)
    threads.append(fly_thread.ident)

    # Start the threads
    update_thread.start()
    fly_thread.start()

    # Wait for the threads to finish
    try:
        update_thread.join()
        fly_thread.join()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        stop_all()
        sys.exit()  # Exit the program after stopping the threads

        # Program finished, should exit here
    print("Calling sys exit")
    sys.exit()

