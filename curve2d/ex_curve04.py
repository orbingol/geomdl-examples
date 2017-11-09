# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017
"""
from geomdl import NURBS

# Create a NURBS curve instance (full circle)
curve = NURBS.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up curve
curve.read_ctrlpts_from_txt("ex_curve04.cptw")
curve.degree = 2
# Use a specialized knot vector
curve.knotvector = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Evaluate curve
curve.evaluate()

# Save control points and evaluated curve points
curve.save_curvepts_to_csv("curvepts04_orig.csv")
curve.save_ctrlpts_to_csv("ctrlpts04_orig.csv")

# Good to have something here to put a breakpoint
pass
