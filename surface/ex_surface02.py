# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
from geomdl import BSpline
from geomdl import utilities

# Create a BSpline surface instance
surf = BSpline.Surface()

# Set evaluation delta
surf.delta = 0.01

# Set up surface
surf.read_ctrlpts_from_txt("ex_surface02.cpt")
surf.degree_u = 3
surf.degree_v = 3
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 6)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, 6)

# Evaluate surface
surf.evaluate()

# Evaluate 1st order surface derivative at the given u and v
u = 0.2
v = 0.9
surftan = surf.tangent(u, v)
print("* Surface point at u = %.2f and v = %.2f is (%.2f, %.2f, %.2f)" % (u, v, surftan[0][0], surftan[0][1], surftan[0][2]))
print("* First derivative w.r.t. u is (%.2f, %.2f, %.2f)" % (surftan[1][0], surftan[1][1], surftan[1][2]))
print("* First derivative w.r.t. v is (%.2f, %.2f, %.2f)\n" % (surftan[2][0], surftan[2][1], surftan[2][2]))
# Evaluate normal at the given u and v
norm = surf.normal(u, v)
print("* Normal at u = %.2f and v = %.2f is [%.1f, %.1f, %.1f]\n" % (u, v, norm[0], norm[1], norm[2]))

# Good to have something here to put a breakpoint
pass
