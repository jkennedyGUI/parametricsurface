# Defines points and norms for the paramtric surface for use
# in saddly.py (which, really, should probably be renamed to "driver.py"
# or some such).

# Parametric surface given by the equation:

import numpy as N

def surfacePoint(s,t):
    return [0.5 * N.cos(s), 1.5 * N.cos(t) + 0.5*N.sin(s),N.sin(t), 1.0]
    #return [s, t, s*s-t*t, 1.0]
def surfaceNorm(s,t):
    #x,y,z = -2*s, 2*t, 1.0
    x, y, z = 0.5*N.sin(s), 1.5 * N.sin(t), N.cos(t)
    mag = N.sqrt(x*x+y*y+z*z)
    return [x/mag, y/mag, z/mag, 0.0]
def surfaceTex(s,t):
    v1,v2 = s*0.5 + 0.5, t*0.5+0.5
    return [s,t]
def createSurfacePosNormTex():
    """For each quad in a parametric surface, create
       two triangles with position, normal and texture
       coordinates."""
    verts = []
    inc = 0.2
    for s in N.arange(-7,7,inc):
        for t in N.arange(-7,7,inc):
            p00 = surfacePoint(s,t)
            n00 = surfaceNorm(s,t)
            t00 = surfaceTex(s,t)
            p01 = surfacePoint(s,t+inc)
            n01 = surfaceNorm(s,t+inc)
            t01 = surfaceTex(s,t+inc)
            p10 = surfacePoint(s+inc,t)
            n10 = surfaceNorm(s+inc,t)
            t10 = surfaceTex(s+inc,t)
            p11 = surfacePoint(s+inc,t+inc)
            n11 = surfaceNorm(s+inc,t+inc)
            t11 = surfaceTex(s+inc,t+inc)
            
            verts.extend(p00+n00+t00)
            verts.extend(p10+n10+t10)
            verts.extend(p01+n01+t01)

            verts.extend(p01+n01+t01)
            verts.extend(p11+n11+t11)
            verts.extend(p10+n10+t10)

    return N.array(verts, dtype=N.float32)
