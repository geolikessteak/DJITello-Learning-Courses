from djitellopy import Tello

# Personal drone (variable) connected  to the Tello function
myTello = Tello()

# Connecting to the drone; we need to connect before calling any functions
myTello.connect()

# Launching the drone
myTello.takeoff()

# Flies the drone forward 100 cm
myTello.move_forward(100)

# Lands on the landing pad
myTello.land()