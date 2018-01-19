# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2017-2018

    Tested with:
    * Python v3.6.2
    * NumPy v1.13.3
    * Matplotlib v2.1.0
"""
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Read surface and control points, @ref: https://stackoverflow.com/a/13550615
cpgrid = np.genfromtxt('ctrlpts01_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])
surf = np.genfromtxt('surfpts01_orig.csv', delimiter=',', skip_header=1, names=['x', 'y', 'z'])

# Arrange control points grid for plotting, @ref: https://stackoverflow.com/a/21352257
Xc = cpgrid['x'].reshape(-1, cpgrid['x'].shape[0])
Yc = cpgrid['y'].reshape(-1, cpgrid['x'].shape[0])
Zc = cpgrid['z'].reshape(-1, cpgrid['x'].shape[0])

# Arrange surface points array for plotting, @ref: https://stackoverflow.com/a/21352257
X = surf['x'].reshape(-1, surf['x'].shape[0])
Y = surf['y'].reshape(-1, surf['x'].shape[0])
Z = surf['z'].reshape(-1, surf['x'].shape[0])

# Plot colors array
colors = ['gray', 'brown']

# Start plotting of the surface and the control points grid
fig = plt.figure(figsize=(10.67, 8), dpi=96)
ax = fig.gca(projection='3d')

# Control points as a wireframe plot (use mode='wireframe' while saving CSV file)
ax.plot_wireframe(Xc, Yc, Zc, color=colors[0])

# Surface points as a wireframe plot (use mode='wireframe' while saving CSV file)
ax.plot_wireframe(X, Y, Z, color=colors[1])

# Add legend to 3D plot, @ref: https://stackoverflow.com/a/20505720
plot1_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color=colors[0], marker='o')
plot2_proxy = matplotlib.lines.Line2D([0], [0], linestyle='none', color=colors[1], marker='o')
ax.legend([plot1_proxy, plot2_proxy], ['Control Points', 'Surface'], numpoints=1)

# Display the 3D plot
plt.show()
