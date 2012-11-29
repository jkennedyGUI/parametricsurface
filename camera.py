# Camera object for parametric surface viewer!
# Stores position, forward, up and projection matrix for a
# camera object.

from numpy import *

projection = 0

class Camera:
    def __init__(self, forward, left, up):
        self.forward = forward
        self.left = left
        self.up = up

    
