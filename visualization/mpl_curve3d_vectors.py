# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""
import os
from geomdl import BSpline
from geomdl import utilities

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

# Set evaluation delta
curve.delta = 0.001

# Set up the NURBS curve
curve.read_ctrlpts_from_txt("../curve3d/ex_curve3d02.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaulate curve
curve.evaluate()

#
# Multiple vector evaluation after v3.0.7
#

# List of parametric coordinates to be evaluated
u_list = (0.0175, 0.075, 0.375, 0.535, 0.65, 0.85, 0.975)

# Evaluate tangents, normals and binormals, respectively
curvetans = curve.tangents(u_list=u_list, normalize=True)
curvenorms = curve.normals(u_list=u_list, normalize=True)
curvebinorms = curve.binormals(u_list=u_list, normalize=True)

#
# Multiple vector evaluation prior to v3.0.7
#

# # Store tangent vectors in a list for plotting
# curvetans = []
#
# # Evaluate curve tangent at u = 0.0175
# ct1 = curve.tangent(0.0175, normalize=True)
# curvetans.append(ct1)
#
# # Evaluate curve tangent at u = 0.075
# ct2 = curve.tangent(0.075, normalize=True)
# curvetans.append(ct2)
#
# # Evaluate curve tangent at u = 0.375
# ct3 = curve.tangent(0.375, normalize=True)
# curvetans.append(ct3)
#
# # Evaluate curve tangent at u = 0.535
# ct4 = curve.tangent(0.535, normalize=True)
# curvetans.append(ct4)
#
# # Evaluate curve tangent at u = 0.65
# ct5 = curve.tangent(0.65, normalize=True)
# curvetans.append(ct5)
#
# # Evaluate curve tangent at u = 0.85
# ct6 = curve.tangent(0.85, normalize=True)
# curvetans.append(ct6)
#
# # Evaluate curve tangent at u = 0.975
# ct7 = curve.tangent(0.975, normalize=True)
# curvetans.append(ct7)

# # Store normal vectors in a list for plotting
# curvenorms = []
#
# # Evaluate curve normal at u = 0.0175
# cn1 = curve.normal(0.0175, normalize=True)
# curvenorms.append(cn1)
#
# # Evaluate curve normal at u = 0.075
# cn2 = curve.normal(0.075, normalize=True)
# curvenorms.append(cn2)
#
# # Evaluate curve normal at u = 0.375
# cn3 = curve.normal(0.375, normalize=True)
# curvenorms.append(cn3)
#
# # Evaluate curve normal at u = 0.535
# cn4 = curve.normal(0.535, normalize=True)
# curvenorms.append(cn4)
#
# # Evaluate curve normal at u = 0.65
# cn5 = curve.normal(0.65, normalize=True)
# curvenorms.append(cn5)
#
# # Evaluate curve normal at u = 0.85
# cn6 = curve.normal(0.85, normalize=True)
# curvenorms.append(cn6)
#
# # Evaluate curve normal at u = 0.975
# cn7 = curve.normal(0.975, normalize=True)
# curvenorms.append(cn7)

# # Store binormal vectors in a list for plotting
# curvebinorms = []
#
# # Evaluate curve binormal vector at u = 0.0175
# cbn1 = curve.binormal(0.0175, normalize=True)
# curvebinorms.append(cbn1)
#
# # Evaluate curve binormal vector at u = 0.075
# cbn2 = curve.binormal(0.075, normalize=True)
# curvebinorms.append(cbn2)
#
# # Evaluate curve binormal vector at u = 0.375
# cbn3 = curve.binormal(0.375, normalize=True)
# curvebinorms.append(cbn3)
#
# # Evaluate curve binormal vector at u = 0.535
# cbn4 = curve.binormal(0.535, normalize=True)
# curvebinorms.append(cbn4)
#
# # Evaluate curve binormal vector at u = 0.65
# cbn5 = curve.binormal(0.65, normalize=True)
# curvebinorms.append(cbn5)
#
# # Evaluate curve binormal vector at u = 0.85
# cbn6 = curve.binormal(0.85, normalize=True)
# curvebinorms.append(cbn6)
#
# # Evaluate curve binormal vector at u = 0.975
# cbn7 = curve.binormal(0.975, normalize=True)
# curvebinorms.append(cbn7)

#
# Control Points, Curve and Tangent Vector Plotting using Matplotlib
#

# Arrange control points and evaluated curve points for plotting
ctrlpts = np.array(curve.ctrlpts)
curvepts = np.array(curve.curvepts)

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
