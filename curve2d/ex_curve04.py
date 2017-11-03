# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017
"""
from geomdl import NURBS

# Create a NURBS curve instance
curve = NURBS.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# The full circle with NURBS
curve.read_ctrlpts_from_txt("CPw_Curve4.txt")
curve.degree = 2
# Use a specialized knot vector
curve.knotvector = [0, 0, 0, 0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1, 1]

# Evaluate curve
curve.evaluate()

# Save control points and evaluated curve points
curve.save_surfpts_to_csv("curve4.csv")
curve.save_ctrlpts_to_csv("ctrlpts4.csv")

print("End of NURBS-Python Example")
