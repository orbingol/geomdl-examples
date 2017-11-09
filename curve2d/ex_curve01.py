# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
from geomdl import BSpline
from geomdl import utilities

# Create a B-Spline curve instance
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up curve
curve.read_ctrlpts_from_txt("ex_curve01.cpt")
curve.degree = 4

# Auto-generate  knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Calculate curve
curve.evaluate()

# Save control points and evaluated curve points
curve.save_curvepts_to_csv("curvepts01_orig.csv")
curve.save_ctrlpts_to_csv("ctrlpts01_orig.csv")

# Insert a knot
u = 0.2
curve.insert_knot(u)

# Save control points and evaluated curve points after knot insertion
curve.save_curvepts_to_csv("curvepts01_knotins.csv")
curve.save_ctrlpts_to_csv("ctrlpts01_knotins.csv")

# Good to have something here to put a breakpoint
pass
