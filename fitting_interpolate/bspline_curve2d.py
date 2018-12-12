#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    2-dimensional curve fitting by global interpolation
"""

from geomdl import fitting
from geomdl.visualization import VisMPL as vis


# The NURBS Book Ex9.1
points = ((0, 0), (3, 4), (-1, 4), (-4, 0), (-4, -3))
degree = 3  # cubic curve

# Do global curve interpolation
curve = fitting.interpolate_curve(points, degree)

# Plot the interpolated curve
curve.delta = 0.01
curve.vis = vis.VisCurve2D()
curve.render()

# # Visualize data and evaluated points together
# import numpy as np
# import matplotlib.pyplot as plt
# evalpts = np.array(curve.evalpts)
# pts = np.array(points)
# plt.plot(evalpts[:, 0], evalpts[:, 1])
# plt.scatter(pts[:, 0], pts[:, 1], color="red")
# plt.show()
