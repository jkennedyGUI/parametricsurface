import numpy as N

def newMatrix():
    return N.zeros((4,4),dtype=N.float32)

def setMatrix(m1, m2):
    m1[:,:] = m2

def projectionMatrix(n,f,w,h):
    return N.array(((2.0*n/w, 0, 0, 0),
                    (0, 2.0*n/h, 0, 0),
                    (0, 0, -(f+n)/(f-n), -2.0*f*n/(f-n)),
                    (0, 0, -1, 0)), dtype = N.float32)

def setProjection(m,n,f,w,h):
    m[:,:] = 0.0
    m[0,0] = 2.0*n/w
    m[1,1] = 2.0*n/h
    m[2,2] = -(f+n)/(f-n)
    m[2,3] = -2.0*f*n/(f-n)
    m[3,2] = -1.0
    
def translationMatrix(x,y,z):
    return N.array(((1, 0, 0, x),
                    (0, 1, 0, y),
                    (0, 0, 1, z),
                    (0, 0, 0, 1)), dtype = N.float32)

def setTranslation(m,x,y,z):
    m[:,:] = N.eye(4, dtype=N.float32)
    m[:,3] = (x,y,z,1)
    
def rotationXMatrix(angle):
    s = N.sin(angle)
    c = N.cos(angle)
    return N.array(((1.0, 0.0, 0.0, 0.0),
                    (0.0,   c,  -s, 0.0),
                    (0.0,   s,   c, 0.0),
                    (0.0, 0.0, 0.0, 1.0)), dtype = N.float32)

def setRotationX(m,angle):
    s = N.sin(angle)
    c = N.cos(angle)
    m[:,:] = N.eye(4, dtype=N.float32)
    m[1,1] = c
    m[2,2] = c
    m[1,2] = -s
    m[2,1] = s

def rotationYMatrix(angle):
    s = N.sin(angle)
    c = N.cos(angle)
    return N.array(((  c, 0.0,  -s, 0.0),
                    (0.0, 1.0, 0.0, 0.0),
                    (  s, 0.0,   c, 0.0),
                    (0.0, 0.0, 0.0, 1.0)), dtype = N.float32)

def setRotationY(m,angle):
    s = N.sin(angle)
    c = N.cos(angle)
    m[:,:] = N.eye(4, dtype=N.float32)
    m[0,0] = c
    m[2,2] = c
    m[0,2] = -s
    m[2,0] = s
    
def rotationZMatrix(angle):
    s = N.sin(angle)
    c = N.cos(angle)
    return N.array(((  c,  -s, 0.0, 0.0),
                    (  s,   c, 0.0, 0.0),
                    (0.0, 0.0, 1.0, 0.0),
                    (0.0, 0.0, 0.0, 1.0)), dtype = N.float32)


def setRotationZ(m,angle):
    s = N.sin(angle)
    c = N.cos(angle)
    m[:,:] = N.eye(4, dtype=N.float32)
    m[0,0] = c
    m[1,1] = c
    m[0,1] = -s
    m[1,0] = s
