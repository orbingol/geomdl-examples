#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""

from geomdl import fitting
from geomdl.visualization import VisMPL as vis


# Data set
points = ((-5, -5, 0), (-2.5, -5, 0), (0, -5, 0), (2.5, -5, 0), (5, -5, 0),
          (-5, 0, 3), (-2.5, 0, 3), (0, 0, 3), (2.5, 0, 3), (5, 0, 3),
          (-5, 5, 0), (-2.5, 5, 0), (0, 5, 0), (2.5, 5, 0), (5, 5, 0))
size_u = 3
size_v = 5
degree_u = 2
degree_v = 3

# # Data set - flipped
# points = ((-5, -5, 0), (-5, 0, 3), (-5, 5, 0),
#           (-2.5, -5, 0), (-2.5, 0, 3), (-2.5, 5, 0),
#           (0, -5, 0), (0, 0, 3), (0, 5, 0),
#           (2.5, -5, 0), (2.5, 0, 3), (2.5, 5, 0),
#           (5, -5, 0), (5, 0, 3), (5, 5, 0))
# size_u = 5
# size_v = 3
# degree_u = 3
# degree_v = 2

# Do global surface interpolation
surf = fitting.interpolate_surface(points, size_u, size_v, degree_u, degree_v)

# Plot the interpolated surface
surf.delta = 0.05
surf.vis = vis.VisSurface()
surf.render()

# # Visualize data and evaluated points together
# import numpy as np
# import matplotlib.pyplot as plt
# evalpts = np.array(surf.evalpts)
# pts = np.array(points)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter(evalpts[:, 0], evalpts[:, 1], evalpts[:, 2])
# ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], color="red")
# plt.show()
