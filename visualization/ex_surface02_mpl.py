# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2017

    Tested with:
    * Python v3.6.2
    * NumPy v1.13.3
    * Matplotlib v2.1.0
"""
import math
import numpy as np
import matplotlib
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Read surface and control points, @ref: https://stackoverflow.com/a/13550615
cpgrid = np.genfromtxt('ctrlpts02_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])
surf = np.genfromtxt('surfpts02_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])

# Arrange control points grid for plotting, @ref: https://stackoverflow.com/a/21352257
cols = cpgrid['x'].shape[0]
Xc = cpgrid['x'].reshape(-1, cols)
Yc = cpgrid['y'].reshape(-1, cols)
Zc = cpgrid['z'].reshape(-1, cols)

# Arrange surface points array for plotting
X = surf['x']
Y = surf['y']
Z = surf['z']

# Plot colors array
colors = ['red', 'green']

# Start plotting of the surface and the control points grid
fig = plt.figure(figsize=(10.67, 8), dpi=96)
ax = fig.gca(projection='3d')

# Control points as a scatter plot (use mode='wireframe' while saving CSV file)
ax.plot_wireframe(Xc, Yc, Zc, color=colors[0])

# Surface points as a triangulated surface plot (use mode='linear' while saving CSV file)
ax.plot_trisurf(X, Y, Z, cmap=cm.winter)

# Add legend to 3D plot, @ref: https://stackoverflow.com/a/20505720
scatter1_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color=colors[0], marker='o')
scatter2_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color=colors[1], marker='^')
ax.legend([scatter1_proxy, scatter2_proxy], ['Control Grid', 'Surface Triplot'], numpoints=1)

# Display the 3D plot
plt.show()
