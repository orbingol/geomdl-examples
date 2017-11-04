# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
from geomdl import BSpline
from geomdl import utilities

# Create a BSpline (NUBS) curve instance
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up curve
curve.read_ctrlpts_from_txt("ex_curve02.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaulate curve
curve.evaluate()

# Evaluate derivatives at u = 0.6
ders = curve.derivatives(0.6, 4)

# Compute curve tangent at u = 0.6
curvetan = curve.tangent(0.6)

# Save control points and evaluated curve points
curve.save_surfpts_to_csv("curve2.csv")
curve.save_ctrlpts_to_csv("ctrlpts2.csv")

# Good to have something here to put a breakpoint
pass
