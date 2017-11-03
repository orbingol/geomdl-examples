# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017

    This example is contributed by John-Eric Dufour (@jedufour)
"""
from geomdl import NURBS

# Create a NURBS surface instance
surf = NURBS.Surface()

# Set up surface
surf.read_ctrlpts_from_txt("ex_surface03.cptw")
surf.degree_u = 1
surf.degree_v = 2
surf.knotvector_u = [0, 0, 1, 1]
surf.knotvector_v = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Evaluate surface
surf.evaluate()

print("End of NURBS-Python Example")
