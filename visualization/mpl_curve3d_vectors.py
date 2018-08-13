# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2018

    Creates a 3-dimensional curve and plots tangent, normal and binormal vectors
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange
from geomdl import operations

import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#
# Curve Evaluation
#

# Create a BSpline curve instance
curve = BSpline.Curve()

# Set degree
curve.degree = 3

# Set control points
curve.ctrlpts = exchange.import_txt("../curve3d/ex_curve3d02.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.001

# Evaulate curve
curve.evaluate()

#
# Multiple vector evaluation after v3.0.7
#

# List of parametric coordinates to be evaluated
u_list = (0.0175, 0.075, 0.375, 0.535, 0.65, 0.85, 0.975)

# Evaluate tangents, normals and binormals, respectively
curvetans = [[] for _ in range(len(u_list))]
curvenorms = [[] for _ in range(len(u_list))]
curvebinorms = [[] for _ in range(len(u_list))]
for idx, u in enumerate(u_list):
    curvetans[idx] = operations.tangent(curve, u, normalize=True)
    curvenorms[idx] = operations.normal(curve, u, normalize=True)
    curvebinorms[idx] = operations.binormal(curve, u, normalize=True)

#
# Control Points, Curve and Tangent Vector Plotting using Matplotlib
#

# Arrange control points and evaluated curve points for plotting
ctrlpts = np.array(curve.ctrlpts)
curvepts = np.array(curve.evalpts)

# Convert tangent, normal and binormal vector lists into NumPy arrays
ctarr = np.array(curvetans)
cnarr = np.array(curvenorms)
cbnarr = np.array(curvebinorms)

# Draw the control points polygon, the 3D curve and the vectors
fig = plt.figure(figsize=(10.67, 8), dpi=96)
ax = Axes3D(fig)

# Plot 3D lines
ax.plot(ctrlpts[:, 0], ctrlpts[:, 1], ctrlpts[:, 2], color='black', linestyle='-.', marker='o', linewidth=1)
ax.plot(curvepts[:, 0], curvepts[:, 1], curvepts[:, 2], color='brown', linestyle='-', linewidth=2)

# Plot tangent vectors
ax.quiver(ctarr[:, 0, 0], ctarr[:, 0, 1], ctarr[:, 0, 2], ctarr[:, 1, 0], ctarr[:, 1, 1], ctarr[:, 1, 2],
          color='blue', length=2.5)

# Plot normal vectors
ax.quiver(cnarr[:, 0, 0], cnarr[:, 0, 1], cnarr[:, 0, 2], cnarr[:, 1, 0], cnarr[:, 1, 1], cnarr[:, 1, 2],
          color='red', length=2.5)

# Plot binormal vectors
ax.quiver(cbnarr[:, 0, 0], cbnarr[:, 0, 1], cbnarr[:, 0, 2], cbnarr[:, 1, 0], cbnarr[:, 1, 1], cbnarr[:, 1, 2],
          color='green', length=2.5)

# Add legend to 3D plot, @ref: https://stackoverflow.com/a/20505720
ctrlpts_proxy = matplotlib.lines.Line2D([0], [0], linestyle='-.', color='black', marker='o')
curvepts_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='brown', marker='o')
tangent_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='blue', marker='>')
normal_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='red', marker='>')
binormal_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='green', marker='>')
ax.legend([ctrlpts_proxy, curvepts_proxy, tangent_proxy, normal_proxy, binormal_proxy],
          ['Control Points', 'Curve', 'Tangents', 'Normals', 'Binormals'], numpoints=1)

# Display the 3D plot
plt.show()
