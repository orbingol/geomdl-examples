# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2018

    Creates a 3-dimensional curve and plots tangent vectors
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
curve.ctrlpts = exchange.import_txt("../curve3d/ex_curve3d01.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.001

# Evaulate curve
curve.evaluate()

#
# Tangent Vector Evaluation
#

# Store tangent vectors in a list for plotting
curvetan = []

# Evaluate curve tangent at u = 0.0175
ct1 = operations.tangent(curve, 0.0175, normalize=True)
curvetan.append(ct1)

# Evaluate curve tangent at u = 0.075
ct2 = operations.tangent(curve, 0.075, normalize=True)
curvetan.append(ct2)

# Evaluate curve tangent at u = 0.375
ct3 = operations.tangent(curve, 0.375, normalize=True)
curvetan.append(ct3)

# Evaluate curve tangent at u = 0.535
ct4 = operations.tangent(curve, 0.535, normalize=True)
curvetan.append(ct4)

# Evaluate curve tangent at u = 0.65
ct5 = operations.tangent(curve, 0.65, normalize=True)
curvetan.append(ct5)

# Evaluate curve tangent at u = 0.85
ct6 = operations.tangent(curve, 0.85, normalize=True)
curvetan.append(ct6)

# Evaluate curve tangent at u = 0.975
ct7 = operations.tangent(curve, 0.975, normalize=True)
curvetan.append(ct7)

#
# Control Points, Curve and Tangent Vector Plotting using Matplotlib
#

# Arrange control points and evaluated curve points for plotting
ctrlpts = np.array(curve.ctrlpts)
curvepts = np.array(curve.evalpts)

# Convert tangent list into a NumPy array
ctarr = np.array(curvetan)

# Draw the control points polygon, the 3D curve and the tangent vectors
fig = plt.figure(figsize=(10.67, 8), dpi=96)
ax = Axes3D(fig)

# Plot 3D lines
ax.plot(ctrlpts[:, 0], ctrlpts[:, 1], ctrlpts[:, 2], color='black', linestyle='-.', marker='o')
ax.plot(curvepts[:, 0], curvepts[:, 1], curvepts[:, 2], color='green', linestyle='-')

# Plot tangent vectors
ax.quiver(ctarr[:, 0, 0], ctarr[:, 0, 1], ctarr[:, 0, 2], ctarr[:, 1, 0], ctarr[:, 1, 1], ctarr[:, 1, 2], color='blue')

# Add legend to 3D plot, @ref: https://stackoverflow.com/a/20505720
ctrlpts_proxy = matplotlib.lines.Line2D([0], [0], linestyle='-.', color='black', marker='o')
curvepts_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='green', marker='o')
tangent_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='blue', marker='>')
ax.legend([ctrlpts_proxy, curvepts_proxy, tangent_proxy], ['Control Points', 'Curve', 'Tangents'], numpoints=1)

# Display the 3D plot
plt.show()
