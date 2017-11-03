# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
from geomdl import BSpline
from geomdl import utilities

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve()

# Set up curve
curve.read_ctrlpts_from_txt("data/CP_Curve2.txt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaulate curve
curve.evaluate()

# Compute curve tangent at u = 0.6
curvetan = curve.tangent(0.6)

# Save control points and evaluated curve points
curve.save_surfpts_to_csv("curve2.csv")
curve.save_ctrlpts_to_csv("ctrlpts2.csv")

print("End of NURBS-Python Example")
