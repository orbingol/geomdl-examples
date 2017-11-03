# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
from geomdl import BSpline
from geomdl import utilities

# Create a BSpline curve instance
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up the NURBS curve
curve.read_ctrlpts_from_txt("ex_curve03.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaulate curve
curve.evaluate()

# Evaluate curve tangent at u = 0.0
curvetan = curve.tangent(0.0)
nvec1 = utilities.vector_normalize((curvetan[1][0], curvetan[1][1]))

# Evaluate curve tangent at u = 0.2
curvetan = curve.tangent(0.2)
nvec2 = utilities.vector_normalize((curvetan[1][0], curvetan[1][1]))

# Evaluate curve tangent at u = 0.5
curvetan = curve.tangent(0.5)
nvec3 = utilities.vector_normalize((curvetan[1][0], curvetan[1][1]))

# Evaluate curve tangent at u = 0.6
curvetan = curve.tangent(0.6)
nvec4 = utilities.vector_normalize((curvetan[1][0], curvetan[1][1]))

# Evaluate curve tangent at u = 0.8
curvetan = curve.tangent(0.8)
nvec5 = utilities.vector_normalize((curvetan[1][0], curvetan[1][1]))

# Evaluate curve tangent at u = 1.0
curvetan = curve.tangent(1.0)
nvec6 = utilities.vector_normalize((curvetan[1][0], curvetan[1][1]))

print("End of NURBS-Python Example")
