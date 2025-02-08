from djitellopy import Tello

# Personal drone (variable) connected  to the Tello function
myTello = Tello()

# Connecting to the drone
myTello.connect()

# Launching the drone
myTello.takeoff()

# Moving the drone forward 100 cm
myTello.move_forward(100)

# Rotating the drone 180 degrees clockwise
myTello.rotate_clockwise(180)

# Moving the drone forward 100 cm again
myTello.move_forward(100)

# Landing on the landing pad
myTello.land()