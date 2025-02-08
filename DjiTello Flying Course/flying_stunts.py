from djitellopy import Tello

# Personal drone (variable) connected  to the Tello function
myTello = Tello()

# Connecting to the drone
myTello.connect()

# Launching the drone
myTello.takeoff()

# Elevates the drone 100 cm upwards
myTello.move_up(100)

# Drone flips forward
myTello.flip_forward() # No argument

# Drone flips backward
myTello.flip_back() # No argument

"""
Due to the nature of the flips,
the drone may not land perfectly on the
landing pad. 
"""

# Landing on the landing pad
myTello.land()