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
import os
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Read surface and control points, @ref: https://stackoverflow.com/a/13550615
cpgrid = np.genfromtxt('ctrlpts03_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])
surf = np.genfromtxt('surfpts03_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])

# Reshape surface points array for plotting, @ref: https://stackoverflow.com/a/21352257
cols = surf['x'].shape[0]
X = surf['x'].reshape(-1, cols)
Y = surf['y'].reshape(-1, cols)
Z = surf['z'].reshape(-1, cols)

# Start plotting of the surface and the control points grid
fig = plt.figure(figsize=(10.67, 8), dpi=96)
ax = fig.gca(projection='3d')

# Control points as a scatter plot (use mode='linear' while saving CSV file)
ax.scatter(cpgrid['x'], cpgrid['y'], cpgrid['z'], color='blue', s=50, depthshade=True)

# Surface points as a wireframe plot (use mode='wireframe' while saving CSV file)
ax.plot_wireframe(X, Y, Z, color='green')

# Set axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 1)

# Add legend to 3D plot, @ref: https://stackoverflow.com/a/20505720
scatter1_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='blue', marker='o')
scatter2_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color='green', marker='o')
ax.legend([scatter1_proxy, scatter2_proxy], ['Control Points', 'Surface Wireframe'], numpoints=1)

# Display the 3D plot
plt.show()
