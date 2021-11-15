from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.rotate_counter_clockwise(90)

tello.land()