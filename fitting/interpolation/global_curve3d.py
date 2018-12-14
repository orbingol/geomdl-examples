#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    3-dimensional curve fitting by global interpolation
"""

from geomdl import fitting
from geomdl import exchange
from geomdl.visualization import VisMPL as vis

# Read data points from a .csv file (ref: https://github.com/idealab-isu/de-la-mo)
points = exchange.import_csv("ex_curve3d.cpt")

# Do global curve interpolation
curve = fitting.interpolate_curve(points, degree=3)

# Plot the interpolated curve
curve.delta = 0.005
curve.vis = vis.VisCurve3D(vis.VisConfig(ctrlpts=False))
curve.render()

# # Visualize data and evaluated points together
# import numpy as np
# import matplotlib.pyplot as plt
# evalpts = np.array(curve.evalpts)
# datapts = np.array(points)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot(evalpts[:, 0], evalpts[:, 1], evalpts[:, 2])
# ax.scatter(datapts[:, 0], datapts[:, 1], datapts[:, 2], color="red")
# plt.show()
