# Camera object for parametric surface viewer!
# Stores position, forward, up and projection matrix for a
# camera object.

import numpy as N

class Camera:
    def __init__(self, forward, left, up, R):
        self.forward = forward
        self.left = left
        self.up = up
        self.pMatrix = projectionMatrix(1.0, 10.0, 1.0, 1.0)
        self.eye = N.eye(4, dtype=N.float32)
        self.R = R


    def rotateBy(x, y):
        """Rotate by given x and y changes in the mouse coordinates."""
        moveUp = y * 1.0
        moveLeft = x * 1.0
        self.eye += self.up * moveUp
        self.eye += self.left * moveLeft

        # normalize?
        # Point back at the origin!

        # Now, put back onto the sphere!
        distanceOff = self.eye - R
        

        

    
