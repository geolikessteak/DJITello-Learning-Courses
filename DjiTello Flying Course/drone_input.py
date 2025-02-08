from djitellopy import Tello
# keyboard library allows user input
import keyboard

myTello = Tello()

myTello.connect()

while True:
    if keyboard.is_pressed('t'):
        myTello.takeoff()
    elif keyboard.is_pressed('w'):
        myTello.move_forward(100)
    elif keyboard.is_pressed('a'):
        myTello.move_left(100)
    elif keyboard.is_pressed('s'):
        myTello.move_back(100)
    elif keyboard.is_pressed('d'):
        myTello.move_right(100)
    elif keyboard.is_pressed('l'):
        myTello.land()
    else:
        pass